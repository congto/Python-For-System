#!/usr/bin/env python
#Thao tac voi localhost
from fabric.api import local
from fabric.api import run, env 

def uptime():
	local("uptime")
	local('uname -rms')
	local('hostname')

#Thao tac voi host tu xa
def host_remote():
	env.user="root"
# Thuc thi cac lenh
	run("hostname")
	run("mkdir /tmp/trunk/")
	run("ls -l >> /tmp/trunk/test.txt")

#Trien khai web
def install_web():
	env.user="root"
	run("yum -y install httpd wget")
	run("/etc/rc.d/init.d/iptables stop")
	run("/etc/rc.d/init.d/httpd start")
	run("rm -f index.html")
	run("wget https://raw.githubusercontent.com/tothanhcong/scripts/master/index.html")
	run("cp index.html /var/www/html/")
	run("/etc/rc.d/init.d/httpd restart")
#Ket thuc