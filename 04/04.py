import urllib
import re
import sys

base = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%s"

next_nothing = "12345" #first run
next_nothing = "8022" #new instructions
next_nothing = "63579" #new new

for i in range(400):
	print next_nothing
	data = urllib.urlopen(base % next_nothing).read()
	try:
		next_nothing = re.search('([0-9]+)', data).group(0)
	except:
		print data
		sys.exit(0)

