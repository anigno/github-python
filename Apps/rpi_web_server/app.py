from flask import Flask, render_template, request
import RPi.GPIO as GPIO

app = Flask(__name__)

# Set up GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Define GPIO pins
button_pin = 18
slider_pin = 21

GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(slider_pin, GPIO.OUT)

# Define routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/button', methods=['POST'])
def button():
    if GPIO.input(button_pin) == GPIO.LOW:
        return 'Button pressed!'
    else:
        return 'Button released.'

@app.route('/slider', methods=['POST'])
def slider():
    slider_value = request.form['slider']
    GPIO.output(slider_pin, int(slider_value))
    return 'Slider set to ' + slider_value

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
