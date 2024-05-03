def main():
    path = "books/frankenstein.txt"
    book = open_book_path(path)
    dict = character_count(book)
    print_report(path, book, dict)


def open_book_path(path):
    with open(path) as f:
        return f.read()
    

def number_of_words(book):
    return len(book.split())

def character_count(book):
    char_dict = {}
    for char in book.lower():
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict

def print_report(path, book, dict):
    print("--- Begin report of " + path + " ---\n" +
          str(number_of_words(book)) + " words found in the document")





main()