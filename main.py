#book_contents = ""
def get_book_text():
	with open("/Users/andrewjohnson/workspace/github.com/dizzysaxophone/bookbot/bookbot/books/frankenstein.txt") as book:
		book_contents = book.read()
#		print(book_contents)
get_book_text()

def get_word_count():
	with open("/Users/andrewjohnson/workspace/github.com/dizzysaxophone/bookbot/bookbot/books/frankenstein.txt") as word:
		word_contents = word.read()
		Word_count = word_contents.split()
		print(f"{len(Word_count)} words found in the document")
#		print(word_contents)
get_word_count()
