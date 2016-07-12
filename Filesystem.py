# !/usr/bin/python
# -*- coding: utf-8 -*- 
#
#    POC - Filesystem Interactivity items
#
#    @author: Matt Jouques
#

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
print "\n * Hostname: " + osDetails[1]                                               # Gets system Hostname
print "\n * Platform: " + osDetails[0] + " " + osDetails[4]                          # Gets OS type and Architecture

# Directory Information
curDir = os.getcwdu()                                                                # Gets current working directory
curDirList = os.listdir(curDir)                                                      # Gets current directory list
print "\n * Current Directory: " + os.getcwdu()                                      # Prints current directory
print '\n'.join(curDirList)                                                          # Prints list of current directory contents

# Get current user & Home Directory
import pwd

user = pwd.getpwuid( os.getuid() )[ 0 ]                                              # Gets the current user uid
from os.path import expanduser                                                       # Gets username for uid
home = expanduser("~")                                                               # Gets current users home directory  
print "\n * Current User is: " + user
print "\n * Users home directory: " + home

# Changing Directories
os.chdir(home)                                                                       # Changes to users home directory
homeDirList = os.listdir(home)                                                       # Gets current directory list
print '\n'.join(homeDirList)                                                         # Prints list of home directory contents

# Temporary folder & files
import tempfile
print "\n * Temporary files & Folders"
print tempfile.gettempdir()                                                          # prints the current temporary directory
f = tempfile.TemporaryFile()
f.write('Write something into temporary file')
f.seek(0)                                                                            # return to beginning of file
print f.read()                                                                       # reads data back from the file
f.close()                                                                            # temporary file is automatically deleted here

# Create a file in Home Directory
newFile = home + "/newfile.txt"
print "\n * Creating and writing to %s" % newFile
file = open(newFile, "w")                                                            # Creates a file in current directory (home in this case) - Note: Overwrites existing file
file.write("This is the first line of text \n")                                      # Adds this line to the file with a new line command at the end
file.write("and another line \n")                                                    # Adds another line to the file with a new line command
file.close()                                                                         # Closes the file

# Read a files contents
file = open(newFile, 'r')                                                            # Open a file to read
print "\n * Newfile contents are\n" + file.read()                                    # Read the contents
file = open(newFile, 'r')                         
print "\nThe first 4 characters of this file are: " + file.read(4)                   # Read first 4 char from file
file = open(newFile, 'r')
print "\nThe first line of this file is: " + file.readline()                         # Read each line in turn
print "\nThe second line of this file is: " + file.readline()                        # Read each line in turn
file = open(newFile, 'r')
fileAsList = file.readlines()                                                        # Read file contents and store in a list
print "\nThe file lines stored in a list are: "
print fileAsList                    
print "\nLooping through the list:"
for line in fileAsList:                                                              # Loop though the contents of the list
    print line,
print "\nLooping through the file contents:"
file = open(newFile, 'r')     
for line in file:                                                                    # Loop through each line of the file in turn
    print line,
file.close()                                                                         # Close the file (make sure it is closed)

# Change File ownership and permissions
import platform
curOS = platform.system()                                                            # Gets the OS / Plaftorm
if curOS == "Windows":                                                               # Detect Windows and 
    print "\n * Windows Detected... skipping file permissions section"
else:
    from os import stat
    from pwd import getpwuid
    print "\n * Current File Owner is: " + getpwuid(stat(newFile).st_uid).pw_name    # Get current file ownership
    
    #import grp
    #uid = pwd.getpwnam("nobody").pw_uid                                             # get uid for nobody user
    #gid = grp.getgrnam("nogroup").gr_gid                                            # get gid for nogroup
    #os.chown(newFile, uid, gid)                                                     # Change permissions on newfile.txt - TODO - DOes not work - insufficient permissions, don't want to sudo
    #print "Current File Owner is now: " + getpwuid(stat(newFile).st_uid).pw_name    # Get current file ownership

# Change file name
renamedFile = home + "/renamedFile"                                                  # Set New filename
os.rename(newFile, renamedFile)                                                      # Rename the file

# File Properties
import time
print "file created at %s" % time.ctime(os.path.getctime(renamedFile))               # Get the created date for the file
print "file modified at %s" % time.ctime(os.path.getmtime(renamedFile))              # Get the modified date for the file


# utime - Change the modified time of a file




    
