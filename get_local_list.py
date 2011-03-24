#!/usr/bin/python

""" proof of concept to take a basedir, traverse into
it and get a list of files, prepending any subdirs where
necessary, but not prepending the basedir
"""

import os
#MYBASEDIR = "/home/xbmc/scripts/cftest/objectdir"
MYBASEDIR = "/home/xbmc/scripts/cftest/objectdir"

# traverse into our basedir
os.chdir(MYBASEDIR)

# get a list of all files, and subdir/files
mylist = []
for dirname, dirnames, filenames in os.walk('./'):
    for filename in filenames:
        mylist.append(os.path.join(dirname, filename))

# syntactically neater way of iterating an old list
# and making replacements while dumping the elements
# onto a new list
newlist = [str.replace(file, './', '') for file in mylist]

# other way to do the same
# for file in mylist:
    # newlist = str.replace(file, './', '')

# print them out to see
for file in newlist:
    print file
