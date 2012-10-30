import data

f_filename = "first.txt"
s_filename = "second.txt"

ff_obj = open(f_filename, "w")
sf_obj = open(s_filename, "w")
plot_obj = open("plotfile.gnuplot", "w")

for i in range(0, len(data.first), 2):
	ff_obj.write("%s %s\n" % (data.first[i], data.first[i+1]))

for i in range(0, len(data.second), 2):
	sf_obj.write("%s %s\n" % (data.second[i], data.second[i+1]))

#...plot files with gnuplot or equivalent
plot_obj.write("plot '%s' with lines, '%s' with lines\n" %(
	f_filename,
	s_filename
))

ff_obj.close()
sf_obj.close()
plot_obj.close()
