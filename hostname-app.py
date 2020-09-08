from flask import Flask, request
import socket
# Comment for Github version log
app = Flask(__name__)

def get_request_info(path):
    host_name = socket.gethostname()
    host_ip = socket.gethostbyname(host_name)
    data = '------------------------ \n' \
           'You accessed to path "{}"\n' \
           'Access Server URL : {} \n' \
           'Container Hostname : {} \n' \
           'Container IP : {} \n' \
           'Original IP with Proxy : {}\n' \
           'Static string : {}\n\n' \
           '------------------------ \n' \
           'Flask received HTTP header : \n'\
           '{}\n' \
           'remote_addr : {}\n' \
           '------------------------\n'.format(request.path, request.base_url, host_name, host_ip,
             request.environ.get('HTTP_X_REAL_IP'), path, request.headers, request.remote_addr)
    return data

@app.route('/')
def path_root():
    return get_request_info('/')

@app.route('/color')
def path_color():
    return get_request_info('/color')

@app.route('/color/red')
def path_color_red():
    return get_request_info('/color/red')

@app.route('/color/blue')
def path_color_blue():
    return get_request_info('/color/blue')

if __name__ == '__main__':
    app.run(host='0.0.0.0')
