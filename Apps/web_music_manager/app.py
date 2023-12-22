import os

from flask import Flask, render_template, request, jsonify, session

secret_key = os.urandom(24)
app = Flask(__name__, static_url_path='/static')
app.secret_key = secret_key
server_storage = {}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_folders')
def get_folders():
    music_folder = 'music_folders'  # Adjust this to the actual path of your music folder
    folders = [folder for folder in os.listdir(music_folder) if os.path.isdir(os.path.join(music_folder, folder))]
    return jsonify(folders=folders)

@app.route('/select_folder/<folder_name>', methods=['POST'])
def select_folder(folder_name):
    session['selected_folder'] = folder_name
    server_storage['selected_folder'] = folder_name
    return folder_name

@app.route('/update_volume', methods=['POST'])
def update_volume():
    volume_value = request.form.get('volume')
    # Handle the volume update here
    return 'Volume updated ' + volume_value

@app.route('/update_duration', methods=['POST'])
def update_duration():
    duration_value = request.form.get('duration')
    # Handle the duration update here
    return 'Duration updated ' + duration_value

@app.route('/store_data', methods=['POST'])
def store_data():
    request_data: dict = request.get_json()
    server_storage[request_data['key']] = request_data['value']
    return 'Data stored successfully'

@app.route('/get_data/<key>', methods=['GET'])
def get_data(key):
    value = server_storage.get(key)
    data = {
        key: value,
    }
    return jsonify(data)
    # return jsonify({key: value})

if __name__ == '__main__':
    app.run()
