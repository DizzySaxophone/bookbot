import sys
if len(sys.argv) != 2:
    print("Usage: python3 main.py <filename>")
    sys.exit(1)
print("============ BOOKBOT ============")
print(f"Analyzing book found at {sys.argv[1]}...")
print("----------- Word Count ----------")
from stats import get_word_count
print (f"Found {get_word_count()} total words")
print("--------- Character Count -------")
from stats import sort
for i in sort():
    print(f"{i['char']}: {i['count']}")
print("============= END ===============")