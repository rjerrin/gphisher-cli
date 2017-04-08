#!/usr/bin/python

import os                   # For operating system related call e.g [os.listdir()]
import sys
import argparse



from PyQt4 import QtCore, QtGui

# Set Working directory'
if 'core' not in os.listdir(os.getcwd()):
    variable = sys.argv[0]
    direc = variable.replace('ghost.py',"")
    os.chdir(direc)

from core.ghost_dns  import *

if __name__ == '__main__':
     parser = argparse.ArgumentParser()
     parser.add_argument('-n', '--name_server',type=str, dest="ns_server", help="Domain name or IP address of the nameserver to be used")
#     parser.add_argument('-h', '--host_name',type=str, dest="host_name", help="hostname to be resolved for")
     parser.add_argument('-i', '--ip_address',type=str, dest="ip_address", help="ip address to be resolved for")
     arguments = parser.parse_args()

     
     if arguments.ip_address:
         dns_instance = Ghost_DNS_Server()
         dns_instance.interface = "fxp0"
         dns_instance._dns_mode= "SINGLE"
         dns_instance.single = arguments.ip_address
         dns_instance.run()

         

     

