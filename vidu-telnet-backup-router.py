#!/usr/bin/python
#Source: http://eayd.in/?p=273
#
import telnetlib, datetime

now = datetime.datetime.now()

host = "10.10.10.2" # your router ip
username = "cong" # the username
password = "123"
enable = "cisco"
filename_prefix = "cisco-backup"

tn = telnetlib.Telnet(host)
tn.read_until("Username:")
tn.write(username+"\n")
tn.read_until("Password:")
tn.write(password+"\n")
tn.write("terminal length 0"+"\n")
tn.write("sh run"+"\n")
tn.write("exit"+"\n")
output=tn.read_all()

filename = "%s_%.2i-%.2i-%i_%.2i-%.2i-%.2i.txt" % #Khong xuong dong cho nay
(filename_prefix,now.day,now.month,now.year,now.hour,now.minute,now.second)

fp=open(filename,"w")
fp.write(output)
fp.close()