import socket
sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.connect(('192.168.0.90',3000))
qq='hello'
sock.send(qq.encode('utf-8'))
ww=sock.recv(1024)
print(ww.decode('utf-8'))