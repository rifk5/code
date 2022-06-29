#!/usr/bin/python3

import socket

message = b"Jenny"
ip_addr = "172.16.1.15"
port = 5309

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
s.connect((ip_addr, port))
s.send(message)
data, conn = s.recvfrom(1024)

print(data.decode("utf-8"))
s.close()
