# import urllib.request
#
#
# def conntect(host="http://google.com"):
#     try:
#         urllib.request.urlopen(host)
#         return True
#     except:
#         return False
#
#
# print("connected" if conntect() else "not connected")


import socket

IPaddress = socket.gethostbyname(socket.gethostname())
if IPaddress == "127.0.0.1":
    print("No internet, your localhost is " + IPaddress)
else:
    print("Connected, with the IP address: " + IPaddress)
