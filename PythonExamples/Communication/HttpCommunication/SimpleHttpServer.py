import http.server


class MyHandler(http.server.BaseHTTPRequestHandler):
    def do_PUT(self):       # Update
        self.answer('PUT')

    def do_POST(self):      # Create
        self.answer('POST')

    def do_DELETE(self):    # Delete
        self.answer('DELETE')

    def do_GET(self):       # Read
        self.answer('GET')

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Allow','GET, OPTIONS')
        self.send_header('Access-Control-Allow-Origin','*')
        self.send_header('Access-Control-Allow-Headers','X-Request, X-Requested-With')
        self.send_header('Content-Length','0')
        self.end_headers()
        print('OPTIONS')

    def answer(self,funcName:str):
        self.send_response(200)
        self.send_header('content-type','application/json')
        self.send_header('content-type','text/html')
        self.end_headers()
        self.wfile.write(b'{"key1":"value2"}')
        print(funcName,self.path)



if __name__== '__main__':
    server=http.server.HTTPServer(('10.108.102.29',8080),MyHandler)
    print('Server started',server.server_address)
    server.serve_forever()