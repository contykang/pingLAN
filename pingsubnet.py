# /usr/bin/python3.5/python3
# code=utf-8

import os
import socket
import struct

from builtins import input

def str2uint(str):
    # 得到始终是正数
    return socket.ntohl(struct.unpack("I", socket.inet_aton(str))[0])


def str2int(str):
    uint = socket.ntohl(struct.unpack("I", socket.inet_aton(str))[0])
    # 先得到负数，再转换一下
    return struct.unpack("i", struct.pack('I', uint))[0]


def num2str(ip):
    if ip < 0:
        ip = struct.unpack("I", struct.pack('i', ip))[0]
    return socket.inet_ntoa(struct.pack('I', socket.htonl(ip)))

network_addr = input("Please enter the network address: ")
subnet_mask = int(input("Please enter the subnet mask length: "),10)


start_addr = str2uint(network_addr)
#start_addr_bin = bin(start_addr)
#netaddr_bin = start_addr_bin[0:subnet_mask]


fill_ones = ''
for i in range(subnet_mask,32):
    fill_ones=fill_ones+'1'

fill_ones_dec=int(fill_ones,2)


last_addr = start_addr+fill_ones_dec



for j in range (start_addr+1,last_addr-1):
    ip = num2str(j)
    result = os.system('ping -c 2 -W 10 '+ ip)
    if result == 0:
        print (ip,' is up!')
    else:
        print(ip, 'is down!')












