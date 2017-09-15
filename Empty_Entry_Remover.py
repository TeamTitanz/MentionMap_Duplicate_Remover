from __future__ import print_function

import os

# enter file input name
mentionMap = 'mapAll.txt'

# get Current path of this file
currentPath = os.getcwd()

# Start reading the file in separate lines
with open(currentPath + '/' + mentionMap) as f:
    lines = f.readlines()
    # stripping the newline character
    lines = [x.strip() for x in lines]

# create new file to add non empty entries
f = open('newMentionMap.txt', 'w')

# removing entries which doesn not have any references
for line in lines:
    if (';') in line:
        print(line, file=f)
