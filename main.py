import sys
from stats import count_words
from stats import count_chars
from stats import sort_dict_list

def get_book_text(filepath):
    with open(filepath) as f:
        contents = f.read()
    return contents

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        text = get_book_text(sys.argv[1])

    num_words = count_words(text)
    num_chars = count_chars(text)
    sorted_dict_list = sort_dict_list(num_chars)

    print(f"============ BOOKBOT ============\nAnalyzing book found at {sys.argv[1]}...\n----------- Word Count ----------\nFound {num_words} total words\n--------- Character Count -------")
    for dict in sorted_dict_list:
        print(f"{dict["character"]}: {dict["count"]}")
    print("============= END ===============")

main()