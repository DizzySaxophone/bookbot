def get_word_count():
	with open("/home/dizzy/boot.dev/bookbot/books/frankenstein.txt") as word:
		word_contents = word.read()
		Word_count = word_contents.split()
		print(f"{len(Word_count)} words found in the document")
#		print(word_contents)
#	return f"{len(Word_count)} words found in the document"
get_word_count()

def get_letter_count():
	with open("/home/dizzy/boot.dev/bookbot/books/frankenstein.txt") as letter:
		letter_contents = letter.read()
		lower_case = letter_contents.lower()
		letter_dict = {}
		for letters in lower_case:
			if letters.isalpha():
				if letters in letter_dict:
					letter_dict[letters] += 1
				else:
					letter_dict[letters] = 1
		#print(f"'{letters}': {letter_dict[f"'{letters}'"]}")
		print(letter_dict)
get_letter_count()