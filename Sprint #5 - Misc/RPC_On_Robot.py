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

def take_picture(filename='picture.jpg',view=False,S=10):
    from pylab import imread
    if BP:
        a=os.system("fswebcam -s brightness=100%% -r 1600x900 --no-banner -S %d '%s'" % (S,filename))
        print(a)

    arr=imread(filename)
    return to_string(arr)



# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)


port=8001
name='localhost'
# Create server

try:
    with MyXMLRPCServer((name,port),
                            requestHandler=RequestHandler,allow_none=True) as server:

        print("Starting server...",name,port,"...")
        server.register_introspection_functions()

        server.register_function(move_forward)
        server.register_function(move_backward)
        server.register_function(turn_robot_left_90)
        server.register_function(turn_robot_right_90)
        server.register_function(turn_robot_left_45)
        server.register_function(turn_robot_right_45)
        server.register_function(arm_up)
        server.register_function(arm_down)

        server.register_function(take_picture)

        # Run the server's main loop
        server.serve_forever()

except KeyboardInterrupt:
    pass

print("done.")
