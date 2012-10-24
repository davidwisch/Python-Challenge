import code

import re

r = re.findall('[a-z]([A-Z]{3}[a-z][A-Z]{3})[a-z]', code.code)

out = ""
for result in r:
	out += re.search('([a-z])', result).group(0)

print out
