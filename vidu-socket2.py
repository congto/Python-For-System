#!/use/bin/python
#Source: http://pymotw.com/2/socket/addressing.html
import socket

for host in ["pythonvietnam.info",
		"vdc.com.vn", 
	    "www.dantri.com.vn",
		"tothanhcong.info"]:
    print host
    try:
        hostname, aliases, addresses = socket.gethostbyname_ex(host)
        print 'Hostname:', hostname
        print 'Addresses:', addresses
    except socket.error, msg:
        print '%15s : ERROR: %s' % (host, msg)
    print