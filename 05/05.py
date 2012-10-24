import pickle
import sys

p = pickle.load(open("banner.p"))

for l in p:
	for i in l:
		sys.stdout.write(i[0] * i[1])
	sys.stdout.write("\n")
