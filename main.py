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

def sort_on(dict):
    return dict["num"]

def dict_to_sorted_list(dict):
    dict_list = []
    for char, num in dict.items():
        new_dict = {'char': char, 'num': num}
        dict_list.append(new_dict)
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list


def print_report(path, book, dict):
    dict_list = dict_to_sorted_list(dict)
    print("--- Begin report of " + path + " ---\n" +
          str(number_of_words(book)) + " words found in the document\n")
    for item in dict_list:
        if item["char"].isalpha():
            print("The '" + item["char"] + "' character was found " + str(item["num"]) + " times." )
    print("--- End report ---")

main()