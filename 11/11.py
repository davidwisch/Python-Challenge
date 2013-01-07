import Image

im = Image.open("cave.jpg")
imdat = im.load()

out = Image.new(im.mode, (im.size[0]/2, im.size[1]/2), None)
outdat = out.load()

for x in range(1,im.size[0],2):
	for y in range(1,im.size[1],2):
		outdat[x/2,y/2] = imdat[x,y]

out.save("out.jpg")
