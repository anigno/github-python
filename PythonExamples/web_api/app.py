from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample data to store the list of todos
todo_list = []

# Route to create a new todo
@app.route('/todos', methods=['POST'])
def create_todo():
    data = request.get_json()
    task = data.get('task')

    if not task:
        return jsonify({'error': 'Task is required'}), 400

    new_todo = {'task': task}
    todo_list.append(new_todo)

    return jsonify({'message': 'Todo created successfully', 'todo': new_todo}), 201

# Route to get all todos
@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify({'todos': todo_list})

# Route to get a specific todo by ID
@app.route('/todos/<int:todo_id>', methods=['GET'])
def get_todo(todo_id):
    todo = None
    for t in todo_list:
        if t['id'] == todo_id:
            todo = t
            break

    if todo:
        return jsonify({'todo': todo})
    else:
        return jsonify({'error': 'Todo not found'}), 404

# Route to update a todo by ID
@app.route('/todos/<int:todo_id>', methods=['PUT'])
def update_todo(todo_id):
    data = request.get_json()
    new_task = data.get('task')

    for t in todo_list:
        if t['id'] == todo_id:
            t['task'] = new_task
            return jsonify({'message': 'Todo updated successfully', 'todo': t})

    return jsonify({'error': 'Todo not found'}), 404

# Route to delete a todo by ID
@app.route('/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    for t in todo_list:
        if t['id'] == todo_id:
            todo_list.remove(t)
            return jsonify({'message': 'Todo deleted successfully'})

    return jsonify({'error': 'Todo not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
