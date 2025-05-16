def get_word_count(text):
    return len(text.split())


def get_char_count(text):
    text = text.lower()
    count = {}
    for char in text:
        if char in count:
            count[char] = count[char] + 1
        else:
            count[char] = 1

    return count


