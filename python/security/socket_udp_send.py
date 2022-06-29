#!/usr/bin/python3

import socket

message = b"scripts"
ip_addr = "localhost"
port = 10000

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
s.sendto(message, (ip_addr, port))
data, conn = s.recvfrom(1024)

print(data.decode("utf-8"))
