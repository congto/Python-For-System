#!/usr/bin/env python
import socket
import subprocess
import sys
from datetime import datetime

# Xoa man hinh trong LINUX
#subprocess.call("clear", shell=True)
# Xoa man hinh trong WINDOWS
subprocess.call("cls", shell=True)

# Nhap dia chi may chu
remoteServer    = raw_input("Nhap may chu can scan: ")
remoteServerIP  = socket.gethostbyname(remoteServer)

# Hien thi ra dong thong bao
print "-" * 60
print "Xin vui long doi, dang Scan may chu co dia chi", remoteServerIP
print "-" * 60

# Gan t1 bang thoi gian hien tai
t1 = datetime.now()
#listport = [21,22,25,80,43,558,795]
#Scan tu port 1 den port 1024, dung try ... except de xu ly loi
try:
    for port in range(1,1025):  
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((remoteServerIP, port))
        if result == 0:
            print "Port {}: \t Open".format(port)
        sock.close()

except KeyboardInterrupt:
    print "Ban da nhan Ctrl+C"
    sys.exit()

except socket.gaierror:
    print "Khong phan giai duoc ten mien, dang thoat ..."
    sys.exit()

except socket.error:
    print "Khong the ket noi den may chu"
    sys.exit()

# Gan thoi gian hien tai bang t2 (sau khi Scan)
t2 = datetime.now()

# Tong thoi gian Scan
total =  t2 - t1

# Hien thi ra man hinh
print "Tong thoi gian Scan la:", total