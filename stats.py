def get_word_count():
	with open("/home/dizzy/boot.dev/bookbot/books/frankenstein.txt") as word:
		word_contents = word.read()
		Word_count = word_contents.split()
		return len(Word_count)
letter_dict = {}
def get_letter_count():
	with open("/home/dizzy/boot.dev/bookbot/books/frankenstein.txt") as letter:
		letter_contents = letter.read()
		lower_case = letter_contents.lower()
		for letters in lower_case:
			if letters.isalpha():
				if letters in letter_dict:
					letter_dict[letters] += 1
				else:
					letter_dict[letters] = 1
def sort():
	sorted_words = []
	get_letter_count()
	for char, count in letter_dict.items():
		if char.isalpha():
			sorted_words.append({"char": char, "count": count})
	sorted_words.sort(reverse=True, key=lambda x: x["count"])
	return sorted_words