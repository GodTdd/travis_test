import os
import sys

print 'start'
f = open('super_secret.txt.enc', 'r')
for line in f.readlines():
    print line
f.close()
print os.environ.get('SAUCE_ACCESS_KEY')
print os.environ.get('SAUCE_USERNAME')

print 'end'

sys.exit(0)
