# import asyncore
# import socket
# import os
# import json

# # import device

# # dev = device.Device()

# class RPCHandler(asyncore.dispatcher_with_send):

#     def handle_read(self):
#         message = self.recv(1024)
#         if message:
#             # self.send(message)
#             print message
#             try:
#                 obj = json.loads(message)
#                 on = obj["on"]
#                 illuminant = obj["illuminant"]
#                 power = obj["power"]    
#                 # dev.change(on, illuminant, power)
#                 self.send(message)
#             except:
#                 pass

# class RPCServer(asyncore.dispatcher):

#     def __init__(self, location):
#         asyncore.dispatcher.__init__(self)
#         self.create_socket(socket.AF_UNIX, socket.SOCK_STREAM)
#         self.set_reuse_addr()
#         self.bind(location)
#         self.listen(5)
#         self.state = {'illuminant':5000, 'power':100, 'on': True, 'temperature':{'temp1':25.0, 'temp2':25.0}}
    
#     def handle_accept(self):
#         pair = self.accept()
#         if pair is not None:
#             sock, addr = pair
#             # print 'Incoming connection from %s' % repr(addr)
#             handler = RPCHandler(sock)

# if os.path.exists('/tmp/rpc.sock') == True:
#     os.remove('/tmp/rpc.sock')

# server = RPCServer('/tmp/rpc.sock')
# print 'start background process.'
# asyncore.loop()


# # import socket
# # import os
# # import json

# # class RPCSocketServer(object):
# #     def __init__(self):
# #         self.socket_file = '/tmp/rpc.sock'
# #         self.serversocket = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
# #         self.serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)

# #     def Run(self):
# #         if os.path.exists(self.socket_file) == True:
# #             os.remove(self.socket_file)

# #         self.serversocket.bind(self.socket_file)
# #         self.serversocket.listen(5)

# #         while True:
# #             conn, addr = self.serversocket.accept()
# #             print 'Client connection accepted ', addr
# #             while True:
# #                 try:
# #                     data = json.dumps({'on':True, 'illuminant': 6500, 'power': 100})
# #                     print 'Server sent:', data
# #                     conn.send(data)
# #                 except socket.error, msg:
# #                     print 'Client connection closed', addr
# #                     break
# #         conn.close()

# # if __name__ == "__main__":
# #     s = RPCSocketServer()
# #     s.Run()
        
