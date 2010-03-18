import re

def main():
	index = processQuotes('test', processIndex())
	file = open('index.txt', 'w')

	for key in index.keys():
		file.write(key + index[key] + '\n')
		

def processQuotes(index, keywordIndex):
	file = open('quotesEdited.txt', 'r')
	lines = file.readlines()
	quote = ()
	chapters = []
	authorlist = []
	booklist = dict()

	for line in lines:
		if(line.startswith('(')):
			#comment ignore
			continue

		elif(line.startswith(' ')):
			#new quote or part of a quote
			quote = quote + (line,)

		elif(line.startswith('_')):
			#source for quote
			book = line.strip('_\n') + ':' #all books end with :
			chapter = (book,) + quote
			quote = ()
			#print(chapter)
			chapters.append(chapter)
			

		elif(line.endswith('_\n')):
			#part of a chopped book title
			continue

		else:
			#new author
			#remove meta-data from author
			author = re.sub('_[A-Za-z]*_','',line)
			
			#check for false positives
			if(re.search('[a-z]', author) != None and
					re.search('[:]', author) == None):
				continue

			#format authorname
			author = re.sub('[^A-Za-z]','',author)

			#author added to list
			authorlist.append(author)	
			
			for chapter in chapters:
				#handle books
				booklist[chapter[0]] = author
				#handle keywords
				#I need to find the quote that
				# matches the key from keywords
	
			#write out the last book of quotes
			writeAuthor(author, chapters)
			chapters = []

	return booklist		


def writeAuthor(author, chapters):
	#this code takes a book of quotes and an Author
	# and writes out the Author's file
	file=open('chapters/'+ author, 'w')	

	for chapter in chapters:
		for line in chapter:
			file.write(line)


def processIndex():
	keywords = dict()
	index = open('keywords.txt', 'r')
	lines = index.readlines()
	k = 0
	
	for line in lines:
		if(line.endswith('.\n')):
			#quote or key and quote
			if(not line.startswith(' ')):
				#key and quote
				temp = line.split(' ',1)
				keywords[temp[1].lower()] = temp[0].strip(',\n').lower()
			else:
				keywords[line.lower()] = key
				#quote
		elif(not line.isspace()):
			#key or whitespace
			key = line.strip(',\n').lower()
		#else: just whitespace

	return keywords


if __name__ == "__main__":
    main()

