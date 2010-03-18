
out = ()

file = open('quotes.txt', 'r')
lines = file.readlines()
flag = bool(0)

for line in lines:
	if line.startswith(' '):
		if not flag:
			temp = line,
			out = out + temp
	elif line.startswith('['):
		flag = bool(1)
	elif line.startswith('FOOTNOTE'):
		flag = bool(1)
	elif line.startswith('\n'):
		flag = flag
	else:
		flag = bool(0)
		temp = line,
		out = out + temp

file = open('quotesEdited.txt', 'w')	

for line in out:
	file.write(line.rstrip('[]1234567890-\n'))
	file.write('\n')
	

