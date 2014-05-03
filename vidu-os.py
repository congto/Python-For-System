#!/use/bin/python
#
import os
print "Duong dan file",'\t' '\t', os.getcwd() 	#Hien thi duong dan hien tai
#os.system("tree") 	#Thu hien lenh dir trong Windows
os.system("ls -l")	#Thuc hien lenh ls -l trong Linux 
##Doi ten cua file	
#print os.rename("D:\Feedback cuoi ky.doc", "D:\phanhoi.doc")

##Hien thi kich thuoc cua file - mac dinh theo bytes
print "Kich thuoc file",'\t', os.path.getsize("D:\phanhoi.doc"), "bytes"

#Kiem tra su ton tai cua mot file
print os.path.exists("D:\phanhoi.doc")
