#!/usr/bin/python2	


import commands	


x = commands.getstatusoutput("sudo yum install iscsi-initiator-utils")

p = commands.getstatusoutput("iscsiadm --mode discoverydb --type sendtargets --portal 192.168.42.151 --discover") 

x = commands.getstatusoutput("iscsiadm --mode node --targetname snake --portal 192.168.42.151:3260 --login")

raw_input() 

			