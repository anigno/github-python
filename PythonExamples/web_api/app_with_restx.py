from flask import Flask
from flask_restx import Api, Resource, fields

app = Flask(__name__)

# Create an API instance
api = Api(app, version='1.0', title='Todo API', description='A simple Todo API')

# Define a namespace for the API
ns = api.namespace('todo_api', description='Todo list operations')

# Define a model for the Todo item
todo_model = api.model('Todo', {
    'id': fields.Integer(readonly=True, description='The task unique identifier'),
    'task': fields.String(required=True, description='The task details')
})

# Sample data to store the list of todos
todo_list = []

# Route to create a new todo
@ns.route('/create')
class TodoCreate(Resource):
    @api.doc('create_todo', description='create new TODO item')
    @api.expect(todo_model)
    def post(self):
        data = api.payload
        task = data.get('task')
        if not task:
            return {'error': 'Task is required'}, 400
        new_todo = {'id': len(todo_list) + 1, 'task': task}
        todo_list.append(new_todo)
        return {'message': 'Todo created successfully', 'todo': new_todo}, 201

@ns.route('/list')
class TodoList(Resource):
    @api.doc('get_todos', description='get the TODO list')
    def get(self):
        return {'todos': todo_list}

# Route to get, update, and delete a specific todo by ID
@ns.route('/<int:id>')
@api.doc(params={'id': 'The task identifier'}, description='operations on one TODO item')
class TodoReadUpdateDelete(Resource):
    @api.doc(description='get todo')
    def get(self, id):
        todo = next((t for t in todo_list if t['id'] == id), None)
        if todo:
            return {'todo': todo}
        else:
            return {'error': 'Todo not found'}, 404

    @api.doc(description='update todo')
    @api.expect(todo_model)
    def put(self, id):
        data = api.payload
        new_task = data.get('task')

        for t in todo_list:
            if t['id'] == id:
                t['task'] = new_task
                return {'message': 'Todo updated successfully', 'todo': t}

        return {'error': 'Todo not found'}, 404

    @api.doc(description='delete todo')
    def delete(self, id):
        global todo_list
        todo_list = [t for t in todo_list if t['id'] != id]
        return {'message': 'Todo deleted successfully'}, 204

if __name__ == '__main__':
    app.run(debug=True)
