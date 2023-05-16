from flask import Flask

class MyServer:
    def __init__(self):
        self.app = Flask('SoundsManager')

    def start(self):
        self.app.run(debug=False, host='0.0.0.0', port=5000)

if __name__ == '__main__':
    s=MyServer()
    s.start()