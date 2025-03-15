def count_words(text):
    return len(text.split())

def count_chars(text):
    res = {}

    for char in text.lower():
        if char in res:
            res[char] += 1
        else:
            res[char] = 1
    return res

def sort_dict(dictionary):
    return dict(sorted(dictionary.items(), key=lambda item: item[1], reverse=True))
