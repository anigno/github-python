from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample data to store the list of todos
todo_list = []

# Route to create a new todo
@app.route('/', methods=['GET'])
def route():
    return 'hello'

if __name__ == '__main__':
    app.run(debug=True)
