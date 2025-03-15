def count_words(text):
    return len(text.split())

def count_chars(text):
    dict = {}

    for char in text.lower():
        if char in dict:
            dict[char] += 1
        else:
            dict[char] = 1
    return dict
