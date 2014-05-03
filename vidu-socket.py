#!/use/bin/python
#
import socket
###Tra ve domain name cua di chi 8.8.8.8 (Fully Qualified Domain Name)
print "FQDN 8.8.8.8: ", socket.getfqdn("8.8.8.8") 
print ''
###Kiem tra IP Address may chu pythonvietnam.info
print "Dia chi IP cua PTVN: ", socket.gethostbyname_ex("pythonvietnam.info")
print ''
print "Ten may cua ban: ", socket.gethostname()
remoteServer    = raw_input("Enter a remote host to scan: ")
remoteServerIP  = socket.gethostbyname(remoteServer)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print sock.connect_ex((remoteServer, 80))

# name = raw_input('Nhap ten web: ')
# try:
    # host = socket.gethostbyname(name)
    # print host
# except socket.gaierror:
    # print "Khong tim thay trang web: ", name