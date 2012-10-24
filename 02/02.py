import code

chars = {}

for char in code.code:
	o = char
	if o in chars:
		chars[o] += 1
	else:
		chars[o] = 1

out = ""
for key,value in chars.iteritems():
	if value == 1: #a bunch of chars exist only once
		out += key

print out
