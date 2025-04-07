def get_word_count():
	with open("/home/dizzy/boot.dev/bookbot/books/frankenstein.txt") as word:
		word_contents = word.read()
		Word_count = word_contents.split()
		print(f"Found {len(Word_count)} total words")
#		print(word_contents)
#	return f"{len(Word_count)} words found in the document"
get_word_count()
letter_dict = {"a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0, "h": 0, "i": 0, "j": 0, "k": 0, "l": 0, "m": 0, "n": 0, "o": 0, "p": 0, "q": 0, "r": 0, "s": 0, "t": 0, "u": 0, "v": 0, "w": 0, "x": 0, "y": 0, "z": 0, "æ": 0,"ë": 0, "â": 0, "ê": 0, "ô": 0}
def get_letter_count():
	with open("/home/dizzy/boot.dev/bookbot/books/frankenstein.txt") as letter:
		print("--------- Character Count -------")
		letter_contents = letter.read()
		lower_case = letter_contents.lower()
		#letter_dict = {}
		for letters in lower_case:
			if letters.isalpha():
				if letters in letter_dict:
					letter_dict[letters] += 1
		#print(f"'{letters}': {letter_dict[f"'{letters}'"]}")
		#print(letter_dict)
		#def sort_on(letter_dict):
		#	return letter_dict[int]
		#letter_dict.sorted(reverse=True, value=sort_on)
		for i in sorted(letter_dict, key=letter_dict.get, reverse=True):
			print(f"{i}: {letter_dict[i]}")
get_letter_count()

#def sort_on(letter_dict):
#	return letter_dict[int]
#sort(letter_dict)
#letter_dict.sort(reverse=True, key=sort_on)
#print(letter_dict)