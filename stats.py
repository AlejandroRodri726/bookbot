def get_num_words(text):
    words = text.split()
    num_words = len(words)
    return f"Found {num_words} total words"

def get_num_chars(text):
    char_dict = {}
    for char in text:
        if char.isalpha():
            char = char.lower()

        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict

def sort_on(items):
    return items["num"]

def sorted_dicts(dicts):
    dicts_list = []
    for key in dicts:
        dicts_list.append({"char": key, "num": dicts[key]})
    dicts_list.sort(key=sort_on, reverse=True)
    return dicts_list