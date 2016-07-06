#! /usr/bin/python2	


import commands,os	


z = commands.getstatusoutput("showmount -e 192.168.42.151");	

yt = z[1]	

yt = yt[:-2]	

yt=yt.split(":")	

yt=yt[1]	

yt=yt.strip()	

os.system("mkdir /home/1_GarimaTheGreat")	

os.system("mount 192.168.42.151:"+yt+" /home/1_GarimaTheGreat")	

			