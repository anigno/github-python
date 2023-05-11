import json
import threading
import time

from enums import *
from flask import Flask, render_template, request
import os
import math
from random import randint, seed
from threading import Thread
from pygame import mixer

class WebServerApp:
    SERVING_ALL_ADDRESSES = '0.0.0.0'
    SERVING_PORT_DEFAULT = 5000

    def __init__(self, serving_ip=SERVING_ALL_ADDRESSES, serving_port=SERVING_PORT_DEFAULT):
        self.serving_ip = serving_ip
        self.serving_port = serving_port
        self.app = Flask('SoundsManager')
        self.add_rules()
        self.counter = 0
        self.triggered_time = 0
        self.params = {
            'main_message': 'hello from web server',
            'secondary_message': 'Idle'}
        self.selected_sound = SelectedSound.MUSIC
        self.playing_mode = PlayingMode.STOPPED
        self.volume = 5
        self.selected_duration = 100
        self.main_thread = threading.Thread(target=self.main_thread_start)

    def add_rules(self):
        self.app.add_url_rule("/", view_func=self.index, methods=['POST', 'GET'])
        self.app.add_url_rule("/constructions", view_func=self.constructions, methods=['POST', 'GET'])
        self.app.add_url_rule("/dogs", view_func=self.dogs, methods=['POST', 'GET'])
        self.app.add_url_rule("/frequencies", view_func=self.frequencies, methods=['POST', 'GET'])
        self.app.add_url_rule("/music", view_func=self.music, methods=['POST', 'GET'])
        self.app.add_url_rule("/play", view_func=self.play, methods=['POST', 'GET'])
        self.app.add_url_rule("/stop", view_func=self.stop, methods=['POST', 'GET'])
        self.app.add_url_rule("/trigger", view_func=self.trigger, methods=['POST', 'GET'])
        self.app.add_url_rule("/volume", view_func=self.volume, methods=['POST', 'GET'])
        self.app.add_url_rule("/duration", view_func=self.duration, methods=['POST', 'GET'])

    def start(self):
        self.main_thread.start()
        self.app.run(debug=True, host=self.serving_ip, port=self.serving_port)

    def main_thread_start(self):
        while True:
            time.sleep(1)
            self.counter += 1
            self.triggered_time -= 1
            if self.triggered_time < 0:
                self.triggered_time = 0
            if self.playing_mode is PlayingMode.TRIGGERED and self.triggered_time <= 0:
                with self.app.app_context():
                    self.stop()

    def index(self):
        self.params['secondary_message'] = \
            f'{self.playing_mode.name} {self.selected_sound.name} [V: {self.volume}] ' \
            f'[D: {self.seconds_to_time_str(self.selected_duration)}] ' \
            f'[T: {self.seconds_to_time_str(self.triggered_time)}]'
        return render_template('index.html', params=self.params)

    def constructions(self):
        self.selected_sound = SelectedSound.CONSTRUCTION
        return self.index()

    def dogs(self):
        self.selected_sound = SelectedSound.DOGS
        return self.index()

    def frequencies(self):
        self.selected_sound = SelectedSound.FREQUENCIES
        return self.index()

    def music(self):
        self.selected_sound = SelectedSound.MUSIC
        return self.index()

    def play(self):
        self.playing_mode = PlayingMode.PLAYING
        self.triggered_time = 0
        return self.index()

    def stop(self):
        self.playing_mode = PlayingMode.STOPPED
        self.triggered_time = 0
        return self.index()

    def trigger(self):
        self.playing_mode = PlayingMode.TRIGGERED
        self.triggered_time = self.selected_duration
        # get values from request params
        selected_sound_value = self.get_request_param('selected_sound')
        if selected_sound_value:
            self.selected_sound = SelectedSound(int(selected_sound_value))
        trigger_duration = self.get_request_param('trigger_duration')
        if trigger_duration:
            self.triggered_time = int(trigger_duration)

        return self.index()

    def volume(self):
        self.volume = request.form['volume_slider']
        self.params['volume'] = self.volume
        return self.index()

    def duration(self):
        self.selected_duration = int(math.pow(int(request.form['duration_slider']), 2))
        self.params['duration'] = int(math.sqrt(self.selected_duration))
        return self.index()

    def get_request_param(self, param_name, is_force_get=True):
        if request.method == 'POST' and not is_force_get:
            return request.form[param_name]
        else:
            return request.args.get(param_name, default=None)

    def get_directories(self, path) -> dict:
        directories = {}
        for item in os.listdir(path):
            full_path = os.path.join(path, item)
            if os.path.isdir(full_path):
                directories[full_path] = {}
                directories[full_path] = self.get_directories(full_path)
            else:
                directories[full_path] = None
        return directories

    def play_random_track(self, folder) -> str:
        file = self.select_random_file(folder)
        mixer.music.load(file)
        mixer.music.play()
        return file

    def seconds_to_time_str(self, seconds) -> str:
        s = f'{seconds // 60}:{seconds % 60:02}'
        return s

if __name__ == '__main__':
    ws = WebServerApp()
    dirs = ws.get_directories('sounds')
    json_dumps = json.dumps(dirs, indent=4)
    print(json_dumps)
