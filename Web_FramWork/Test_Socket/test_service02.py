from wsgiref.simple_server import make_server

def application(environ,start_response):
    start_response('200 OK',[('Content_Type','text/html')])
    return [b'<h1>hello,web!</h1>']
httpd = make_server('',8080,application)
print('Serving HTTP on port 8080...')
httpd.serve_forever()