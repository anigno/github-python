import os
import socket
import time
import urllib.parse
from http.server import HTTPServer, BaseHTTPRequestHandler
from queue import Queue
from random import randint, seed
from threading import Thread

from pygame import mixer

queue = Queue()
MUSIC_FOLDER = '_music'
ALARM_FOLDER = '_alarm'
ALARM_PLAY_TIME = 60 * 60 * 10 * 1  # 1/10 of a second
is_playing = False
is_alarming = False
alarm_play_count = 0
play_volume = 8
system_message = ''
played_file = ''
REFRESH_WEB_SECS = 3

class RequestHandler(BaseHTTPRequestHandler):

    def set_activity(self):
        path = self.get_path_folder(self.path)
        params = self.get_params(self.path)
        if path:
            queue.put(path)

    def create_html(self) -> bytes:
        global is_alarming, is_playing, system_message
        play_mode = 'Idle'
        if is_playing:
            play_mode = f'Playing: {played_file}'
        if is_alarming:
            play_mode = f'Playing: {played_file}] [Alarm: {alarm_play_count // 10}'
        system_message = f'[{play_mode}][V: {play_volume}]'
        b_Html = b'<html>' \
                 b'<head>' \
                 b'<META http-equiv=\"refresh\" content=\"' + \
                 str(REFRESH_WEB_SECS).encode() + b';URL=/\">' \
                                                  b'</head>' \
                                                  b'<body>' \
                                                  b'<p style="font-size:40px; text-align: center">' \
                 + system_message.encode() + \
                 b'</p>' \
                 b'<p style="font-size:40px; text-align: center"><a href="/construction">Construction</a> </p>' \
                 b'<p style="font-size:40px; text-align: center"><a href="/dogs">Dogs</a> </p>' \
                 b'<p style="font-size:40px; text-align: center"><a href="/freq">Frequencies</a> </p>' \
                 b'<p style="font-size:40px; text-align: center"><a href="/music">Music</a> </p>' \
                 b'<p style="font-size:40px; text-align: center"><a href="/stop">Stop</a> </p>' \
                 b'<p style="font-size:40px; text-align: center"><a href="/vp">[V+]</a>   <a href="/vm">[V-]</a> </p>' \
                 b'</body>' \
                 b'</html>'
        return b_Html

    def set_headers(self):
        self.send_response(200)
        self.send_header('content-type', 'text/html')
        self.end_headers()

    def do_POST(self):
        self.set_headers()

    def do_GET(self):
        self.set_activity()
        self.set_headers()
        b_Html = self.create_html()
        self.wfile.write(b_Html)

    @staticmethod
    def get_params(path):
        parsed = urllib.parse.urlparse(path)
        params_dict = urllib.parse.parse_qs(parsed.query)
        return params_dict

    @staticmethod
    def get_path_folder(path):
        parsed = urllib.parse.urlparse(path)
        return parsed.path[1:]

class Server:
    def __init__(self, ip=None, port=5000):
        self.queue = Queue()
        local_address = ip if ip else self.get_local_ip()
        self.server = HTTPServer((local_address, port), RequestHandler)
        self.server_thread = Thread(target=self.server.serve_forever)
        self.server_thread.daemon = True
        mixer.init()
        seed(time.time())

    @staticmethod
    def get_local_ip():
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip_address = s.getsockname()[0]
        s.close()
        return ip_address

    # @staticmethod
    # def get_local_addresses():
    #     addresses = [address_info[4][0] for address_info in socket.getaddrinfo(socket.gethostname(), None)
    #                  if address_info[0] == socket.AddressFamily.AF_INET]
    #     return addresses

    def start(self):
        global is_playing, is_alarming, alarm_play_count, ALARM_PLAY_TIME, play_volume, played_file
        self.server_thread.start()
        while True:
            time.sleep(0.100)
            if not queue.empty():
                command = queue.get().upper()

                if command == 'PLAY':
                    is_playing = True
                    is_alarming = False
                    alarm_play_count = 0
                if command == 'ALARM':
                    is_playing = False
                    is_alarming = True
                if command == 'STOP':
                    is_playing = False
                    is_alarming = False
                    alarm_play_count = 0
                    if mixer.music.get_busy():
                        mixer.music.stop()
                if command == 'TRIGGER':
                    if is_alarming:
                        alarm_play_count = ALARM_PLAY_TIME
                if command == 'VP':
                    play_volume += 1
                    if play_volume > 10:
                        play_volume = 10
                if command == 'VM':
                    play_volume -= 1
                    if play_volume < 1:
                        play_volume = 1

            if is_playing:
                mixer.music.set_volume(play_volume / 10)
                if not mixer.music.get_busy():
                    played_file = self.play_random_track(MUSIC_FOLDER)

            # if is_alarming:
            #     mixer.music.set_volume(play_volume / 10)
            #     if not mixer.music.get_busy():
            #         played_file = self.play_random_track(ALARM_FOLDER)

            if is_alarming:
                mixer.music.set_volume(play_volume / 10)
                if alarm_play_count > 0:
                    alarm_play_count -= 1
                    if not mixer.music.get_busy():
                        played_file = self.play_random_track(ALARM_FOLDER)
                else:
                    mixer.music.stop()

    def play_random_track(self, folder) -> str:
        file = self.select_random_file(folder)
        mixer.music.load(file)
        mixer.music.play()
        return file

    def select_random_file(self, folder: str) -> str:
        files = self.get_all_files(folder)
        n = randint(0, len(files) - 1)
        # print(f'file n:{n} {files}')
        file = files[n]
        return file

    def get_all_files(self, folder: str, file_list: list = None):
        if file_list is None: file_list = list()
        for root, folders, files in os.walk(folder):
            for file in files:
                if '.mp3' in file:
                    file_list.append(os.path.join(root, file))
            for folder in folders:
                self.get_all_files(folder, file_list)
        return file_list

if __name__ == '__main__':
    server = Server(ip=None, port=5000)
    print(f'serving address {server.server.server_address}')
    server.start()
