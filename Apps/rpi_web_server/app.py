from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/button', methods=['POST'])
def button():
    return 'Button pressed!'

@app.route('/slider', methods=['POST'])
def slider():
    slider_value = request.form['slider']
    return 'Slider set to ' + slider_value

@app.route('/play', methods=['GET'])
def play():
    return render_template('index.html')
    # return 'play'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
