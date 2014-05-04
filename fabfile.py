#!/usr/bin/env python
#Thao tac voi localhost
from fabric.api import local
def uptime():
	local("uptime")
	#local('uname -rms')
	#local('hostname')
#
#Thao tac voi host tu xa
from fabric.api import run, env 
def host_remote():
	env.user="root"
# Kiem tra thoi gian Uptime
	run("uptime")
# Kiem tra ten may
#	run("hostname")
# Tao thu muc
#	run("mkdir /tmp/trunk/")
#	run("ls -l >> /tmp/trunk/test.txt")



