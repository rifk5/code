#!/usr/bin/python3

import socket 
import sys
from struct import * 
import base64
import binascii

try: 
    s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_RAW)
except socket.error as msg:
    print(msg)
    sys.exit()

packet = ""

src_ip = "10.10.0.40"
dst_ip = "172.16.1.15"

ip_ver_ihl  = 69
ip_tos      = 96
ip_len      = 0
ip_id       = 1984
ip_frag     = 0
ip_ttl      = 64
ip_proto    = 16
ip_check    = 0
ip_srcadd   = socket.inet_aton(src_ip)
ip_dstadd   = socket.inet_aton(dst_ip)

# PACK
ip_header = pack("!BBHHHBBH4s4s", ip_ver_ihl, ip_tos, ip_len, ip_id, ip_frag, ip_ttl, ip_proto, ip_check, ip_srcadd, ip_dstadd)

message = b"Delarosa"
hidden_msg = binascii.hexlify(message)

packet = ip_header + hidden_msg
s.sendto(packet, (dst_ip, 0))

