# main.py
from stats import get_num_words, char_count, dict_sort
import sys
if len(sys.argv)!=2:
    print("Usage: python3 main.py <path_to_book>") 
    sys.exit(1)


def get_book_text(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


def main():
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    num_char = char_count(text)
    sorted_list = dict_sort(num_char)
    for item in sorted_list:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")


main()
