import sys
from stats import get_num_words, get_num_chars, sorted_dicts

def get_book_text(filepath):
    with open(filepath) as file:
        return file.read()

def main():
    if len(sys.argv) == 2:
        path = sys.argv[1]
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    text = get_book_text(path)

    char_counts_dict = get_num_chars(text)
    sorted_char_counts = sorted_dicts(char_counts_dict)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(get_num_words(text))
    print("--------- Character Count -------")
    for dict_pair in sorted_char_counts:
        if not dict_pair["char"].isalpha():
            continue
        char = dict_pair["char"]
        num = dict_pair["num"]
        print(f"{char}: {num}")

main()