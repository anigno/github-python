import http.server
import socketserver
from threading import Thread

port =5555
ip='10.108.102.29'

class MyRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        contentLength=int(self.headers['Content-Length'])
        print(self.path,self.rfile.read(contentLength))

        return  self.path



handler=http.server.SimpleHTTPRequestHandler

def httpThreadStart():
    with socketserver.TCPServer((ip, port), MyRequestHandler) as httpd:
        print('serving')
        httpd.serve_forever()
        print('started')


t1=Thread(target=httpThreadStart)
t1.start()
t1.join()



