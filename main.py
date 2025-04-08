import sys
sys.argv
print("============ BOOKBOT ============")
print("Analyzing book found at books/frankenstein.txt...")
print("----------- Word Count ----------")
from stats import get_word_count
print (f"Found {get_word_count()} total words")
print("--------- Character Count -------")
#from stats import get_letter_count
#print()
from stats import sort
for i in sort():
    print(f"{i['char']}: {i['count']}")
print("============= END ===============")
#from stats import sort