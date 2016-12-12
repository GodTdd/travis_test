import os
import sys

print 'start here too'

print os.environ.get('SAUCE_ACCESS_KEY')
print os.environ.get('SAUCE_USERNAME')

print 'end'

sys.exit(0)
