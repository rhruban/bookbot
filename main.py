from stats import get_word_count, get_char_count


def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()

    return file_contents


def main():
    text = get_book_text("books/frankenstein.txt")
    word_count = get_word_count(text)
    char_count = get_char_count(text)
    print(f"{word_count} words found in the document")
    print(char_count)


main()
