import itertools

a = [1]

for i in range(30):
	out = ""
	for k, g in itertools.groupby(str(a[i])):
		g = list(g)
		out += "%s%s" % (len(g), g[0])
	a.append(out)
	val = int(out)

print len(a[30])
