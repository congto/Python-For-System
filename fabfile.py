#!/usr/bin/env python
#Thao tac voi localhost
from fabric.api import local
def uptime():
	local('uptime')
	#local('uname -rms') hoac #local('hostname')
#
#Thao tac voi host tu xa
from fabric.api import run
def host_type():
# Uptime
	run("uptime")
# Hostname
	run("hostname")
# Create a directory (i.e. folder)
	run("mkdir /tmp/trunk/")
	run("ls -l >> /tmp/trunk/test.txt")