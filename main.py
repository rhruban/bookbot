import sys
from stats import get_word_count, get_char_count, sort_char_count


def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()

    return file_contents


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1) 

    print("============ BOOKBOT ============")

    file_path = sys.argv[1]
    print(f"Analyzing book found at {file_path}...")

    text = get_book_text(file_path)
    word_count = get_word_count(text)
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")

    char_count = get_char_count(text)
    sorted_char_count = sort_char_count(char_count)
    print("--------- Character Count -------")
    for dict in sorted_char_count:
        if dict["char"].isalpha():
            print(f"{dict['char']}: {dict['num']}")

    print("============= END ===============")
    


main()
