#!/usr/bin/python
import sys
import re
input_file=open(sys.argv[1])
# Change the regex to what you want and make the groups 
regex=re.compile(r'[0-9]+.*<([0-9]+\.[0-9]+)>')
for line in input_file:
        m=regex.match(line)
        if m:
                print m.group(1)

