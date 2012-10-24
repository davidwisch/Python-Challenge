code = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

def trans(char):
	o = ord(char)
	#lower case ASCII values
	if o >= 97 and o <= 122:
		if o + 2 > 122:
			o = 97 + (o + 1 - 122) #+1 since we're recycling from 97
		else:
			o += 2
		return chr(o)
	else:
		return char

#apply this to the URL (/map.html)
code_trans = ""
for char in "map":
	code_trans += trans(char);

print code_trans
