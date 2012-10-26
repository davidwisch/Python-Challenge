import sys
import re

import Image

im = Image.open("oxygen.png")
imdat = im.load()

vals = []
x = 0
while x < im.size[0]:
	if imdat[x, 47][0] != imdat[x, 47][1] != imdat[x, 47][2]:
		break;
	vals.append(imdat[x, 47][0])
	x += 7

msg = "".join(map(chr, vals))
print msg

#extract the message
msg = eval(re.search("(\[.*\])", msg).group(0))

print "".join(map(chr, msg))
