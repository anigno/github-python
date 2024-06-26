import json
import logging
import math
import os
import random
import threading
import time
from random import seed
from flask import Flask, render_template, request, redirect, url_for
from pygame import mixer

from common.utils import get_hash_code
from enums import *
from logging_provider.logging_initiator_base import LoggingInitiatorBase
from logging_provider.logging_initiator_by_code import LoggingInitiatorByCode

class WebServerApp:
    SERVING_ALL_ADDRESSES = '0.0.0.0'
    SERVING_PORT_DEFAULT = 5000
    SOUNDS_FOLDER = 'sounds'

    def __init__(self, serving_ip=SERVING_ALL_ADDRESSES, serving_port=SERVING_PORT_DEFAULT):
        self.correct_hash = "efbd1f26a54875e39972ccf7fa21a34f2491c850b2eba9636cb5478e595897b5"
        self.logged_in = False
        self.serving_ip = serving_ip
        self.serving_port = serving_port
        LoggingInitiatorByCode('logs')
        self.logger = logging.getLogger(LoggingInitiatorBase.FILE_SYSTEM_LOGGER)
        self.logger.info('App started')
        self.app = Flask('SoundsManager')

        # self.app.config['SERVER_NAME'] = '192.168.1.29:5000'
        # self.app.config['APPLICATION_ROOT'] = '/'
        # self.app.config['PREFERRED_URL_SCHEME'] = 'http'

        self.add_rules()
        self.counter = 0
        self.triggered_time = 0
        self.params = {
            'main_message': 'hello from web server',
            'secondary_message': 'Idle'}
        self.selected_sound = SelectedSound.MUSIC1
        self.playing_mode = PlayingMode.STOPPED
        self.playing_volume = 5
        self.selected_duration = 100
        mixer.init()
        mixer.music.set_volume(0.5)
        seed(time.time())
        self.main_thread = threading.Thread(target=self.main_thread_start, daemon=True)

    def add_rules(self):
        self.app.add_url_rule('/login', 'login', self.login, methods=['GET', 'POST'])
        self.app.add_url_rule('/logout', 'logout', self.logout)
        self.app.add_url_rule("/", view_func=self.render_index, methods=['POST', 'GET'])
        self.app.add_url_rule("/constructions", view_func=self.constructions, methods=['POST', 'GET'])
        self.app.add_url_rule("/dogs", view_func=self.dogs, methods=['POST', 'GET'])
        self.app.add_url_rule("/frequencies", view_func=self.frequencies, methods=['POST', 'GET'])
        self.app.add_url_rule("/music1", view_func=self.music, methods=['POST', 'GET'])
        self.app.add_url_rule("/music2", view_func=self.music2, methods=['POST', 'GET'])
        self.app.add_url_rule("/music3", view_func=self.music3, methods=['POST', 'GET'])
        self.app.add_url_rule("/play", view_func=self.play, methods=['POST', 'GET'])
        self.app.add_url_rule("/stop", view_func=self.stop, methods=['POST', 'GET'])
        self.app.add_url_rule("/trigger", view_func=self.trigger, methods=['POST', 'GET'])
        self.app.add_url_rule("/volume", view_func=self.volume, methods=['POST', 'GET'])
        self.app.add_url_rule("/duration", view_func=self.duration, methods=['POST', 'GET'])

    def start(self):
        self.main_thread.start()
        self.app.run(debug=False, host=self.serving_ip, port=self.serving_port)

    def main_thread_start(self):
        while True:
            try:
                time.sleep(1)
                self.counter += 1
                self.triggered_time -= 1
                if self.triggered_time < 0:
                    self.triggered_time = 0
                if self.playing_mode is PlayingMode.TRIGGERED and self.triggered_time <= 0:
                    with self.app.app_context():
                        self.stop()
                        self.logger.info('trigger stop')

                if self.playing_mode in (PlayingMode.PLAYING, PlayingMode.TRIGGERED):
                    with self.app.app_context():
                        self.ensure_playing()
                if self.playing_mode is PlayingMode.STOPPED:
                    self.stop_playing()
                    self.playing_mode = PlayingMode.IDLE
                    self.logger.info('stopped playing')
            except Exception as ex:
                self.logger.exception(ex.args)

    def login(self):
        if request.method == 'POST':
            password = request.form['password']
            password_hash = get_hash_code(password)
            if password_hash == self.correct_hash:
                self.logged_in = True
                return redirect(url_for('render_index'))
            else:
                return render_template('login.html', error="Invalid credentials")
        return render_template('login.html')

    def logout(self):
        self.logged_in = False
        return redirect(url_for('login'))

    def render_index(self):
        if not self.logged_in:
            return redirect(url_for('login'))
        self.params['secondary_message'] = \
            f'[{self.playing_mode.name}] [{self.selected_sound.name} ' \
            f'[T: {self.seconds_to_time_str(self.triggered_time)}]'
        self.params['volume'] = self.playing_volume
        self.params['duration'] = int(math.sqrt(self.selected_duration))
        self.params['duration_string'] = self.seconds_to_time_str(self.selected_duration)
        return render_template('index.html', params=self.params)

    def constructions(self):
        self.selected_sound = SelectedSound.CONSTRUCTION
        return self.render_index()

    def dogs(self):
        self.selected_sound = SelectedSound.DOGS
        return self.render_index()

    def frequencies(self):
        self.selected_sound = SelectedSound.FREQUENCIES
        return self.render_index()

    def music(self):
        self.selected_sound = SelectedSound.MUSIC1
        return self.render_index()

    def music2(self):
        self.selected_sound = SelectedSound.MUSIC2
        return self.render_index()

    def music3(self):
        self.selected_sound = SelectedSound.MUSIC3
        return self.render_index()

    def play(self):
        self.playing_mode = PlayingMode.PLAYING
        self.triggered_time = 0

        client_ip = request.headers.get('X-Real-IP') or request.headers.get('X-Forwarded-For')
        if not client_ip:
            client_ip = request.remote_addr + ' *'

        self.logger.info(f'play requested by {client_ip}')
        return self.render_index()

    def stop(self):
        self.playing_mode = PlayingMode.STOPPED
        self.triggered_time = 0
        return self.render_index()

    def trigger(self):
        self.playing_mode = PlayingMode.TRIGGERED
        self.triggered_time = self.selected_duration
        # get values from request params is passed from other client
        selected_sound_value = self.get_request_param('selected_sound')
        if selected_sound_value:
            self.selected_sound = SelectedSound(int(selected_sound_value))
        trigger_duration = self.get_request_param('trigger_duration')
        if trigger_duration:
            self.triggered_time = int(trigger_duration)

        return self.render_index()

    def volume(self):
        self.playing_volume = request.form['volume_slider']
        self.params['volume'] = self.playing_volume
        mixer.music.set_volume(int(self.playing_volume) / 10)
        return self.render_index()

    def duration(self):
        self.selected_duration = int(math.pow(int(request.form['duration_slider']), 2))
        self.params['duration'] = int(math.sqrt(self.selected_duration))
        return self.render_index()

    def ensure_playing(self):
        try:
            if mixer.music.get_busy():
                return
            file = self.get_next_sound_file()
            mixer.music.load(file)
            self.params['main_message'] = f'playing {file}'
            mixer.music.play()
        except Exception as ex:
            self.logger.exception(ex)
        finally:
            pass

    def get_next_sound_file(self) -> str:
        sound_directories = self.get_directories(WebServerApp.SOUNDS_FOLDER)
        sounds_path = os.path.join(WebServerApp.SOUNDS_FOLDER, self.selected_sound.name).lower()
        selected_sounds_list = list(sound_directories[sounds_path].keys())
        next_sound_index = random.randint(0, len(selected_sounds_list) - 1)
        return selected_sounds_list[next_sound_index]

    def stop_playing(self):
        mixer.music.stop()
        self.params['main_message'] = f'stopped'

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

    def seconds_to_time_str(self, seconds) -> str:
        s = f'{seconds // 60}:{seconds % 60:02}'
        return s

if __name__ == '__main__':
    os.path.join('a', 'b')
    ws = WebServerApp()
    dirs = ws.get_directories('sounds')
    json_dumps = json.dumps(dirs, indent=4)
    print(json_dumps)
