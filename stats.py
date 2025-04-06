def get_word_count():
	with open("/home/dizzy/boot.dev/bookbot/books/frankenstein.txt") as word:
		word_contents = word.read()
		Word_count = word_contents.split()
		print(f"{len(Word_count)} words found in the document")
#		print(word_contents)
#	return f"{len(Word_count)} words found in the document"
get_word_count()