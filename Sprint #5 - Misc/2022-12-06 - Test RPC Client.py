import xmlrpc.client
import ssl

from time import sleep

def to_string(arr):
    import json
    s=json.dumps(arr.tolist())
    return s

def from_string(s):
    import json
    from numpy import array
    arr=array(json.loads(s))
    return arr


def take_picture():
    s=server.take_picture()
    arr=from_string(s)
    return arr
    

context = ssl.SSLContext()
server=xmlrpc.client.ServerProxy('http://localhost:8001', context=context)    

arr=take_picture()
print(arr.shape)

