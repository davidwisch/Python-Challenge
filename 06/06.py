import zipfile
import re

zfile = zipfile.ZipFile("channel.zip")

#according to readme, start at 90052
next_nothing = "90052"

comments_collected = ""
while True:
	f = zfile.open("%s.txt" % next_nothing)
	data = f.read()
	comments_collected += zfile.getinfo("%s.txt" % next_nothing).comment
	try:
		next_nothing = re.search('([0-9]+)', data).group(0)
	except:
		print data
		break

#eventual hint was to collect the comments
print comments_collected
