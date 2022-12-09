from my_robot_functions import *

def to_string(arr):
    import json
    s=json.dumps(arr.tolist())
    return s

def from_string(s):
    import json
    from numpy import array
    arr=array(json.loads(s))
    return arr

from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler

class MyXMLRPCServer(SimpleXMLRPCServer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.register_function(self.quit)
    
    def quit(self):
        self._BaseServer__shutdown_request = True
        return 0

left,right=Motors("ab")

def take_picture2(filename='picture.jpg',S=10):
    if BP:
        a=os.system("fswebcam -s brightness=100%% -r 1600x900 --no-banner -S %d '%s'" % (S,filename))
        print(a)

    return os.path.abspath(filename)

def take_picture(filename='picture.jpg',view=False,S=10):
    from pylab import imread
    import pickle
    if BP:
        a=os.system("fswebcam -s brightness=100%% -r 1600x900 --no-banner -S %d '%s'" % (S,filename))
        print(a)

    arr=imread(filename)
    return pickle.dumps(arr)    



def move_forward(arg):
    left.power=50
    right.power=50
    
    Wait(arg)
    left.power=0
    right.power=0
    
def move_backward(arg):
    left.power=-50
    right.power=-50
    
    Wait(arg)
    left.power=0
    right.power=0
    
def stop():
    left.power=0
    right.power=0

def position():
    return [left.position,right.position]


# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)


port=8080
name='10.2.2.30'
# Create server

try:
    server=MyXMLRPCServer((name,port),
                            requestHandler=RequestHandler,allow_none=True)

    print("Starting server...",name,port,"...")
    server.register_introspection_functions()

    server.register_function(move_forward)
    server.register_function(move_backward)
    server.register_function(position)
    server.register_function(stop)

    server.register_function(take_picture)
    server.register_function(take_picture2)

    # Run the server's main loop
    server.serve_forever()

except KeyboardInterrupt:
    pass

Shutdown()
print("done.")
