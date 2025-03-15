import sys
from stats import count_words, count_chars, sort_dict

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    
    return file_contents


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book = sys.argv[1]
    text = get_book_text(book)
    num_words = count_words(text)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    sorted_dict = sort_dict(count_chars(text))
    for key in sorted_dict:
        if key.isalpha():
            print(f"{key}: {sorted_dict[key]}")
    print("============= END ===============")




main()
