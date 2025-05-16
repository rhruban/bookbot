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


def sort_on(dict):
    return dict["num"]


def sort_char_count(char_dict):
    char_list = []
    for key, value in char_dict.items():
        char_list.append({"char": key, "num": value})
    
    char_list.sort(reverse=True, key=sort_on)
    # print(char_list)
    return char_list


