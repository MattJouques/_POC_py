#
# -*- coding: utf-8 -*- 
#
#    POC - Filesystem Interactivity
#
#    @author: Matt Jouques
#

# Config


import os
import sys

# Check code version
req_version = 2.7
cur_version = float('.'.join(map(str, sys.version_info[0:2:1])))
if cur_version < req_version:
    print "Your Python interpreter is too old %s Please consider upgrading to a version greater than %s." % (cur_version, req_version)
else:
    print "Python version ok"

# Get Operating System Details
osDetails = os.uname()
print "Hostname: " + osDetails[1]                           # Gets system Hostname
print "Platform: " + osDetails[0] + " " + osDetails[4]      # Gets OS type and Architecture

# Directory Information
curDir = os.getcwdu()                                       # Gets current working directory
print "Current Directory: " + os.getcwdu()                  # Prints current directory
print '\n'.join(os.listdir(curDir))                         # Prints list of current directory contents


# utime - Change the modified time of a file



    
