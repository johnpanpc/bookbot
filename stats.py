def count_words(text):
    list_words = text.split()
    return len(list_words)

def count_chars(text):
    char_dict = {}
    for char in text:
        if char.lower() in char_dict:
            char_dict[char.lower()] += 1
        else:
            char_dict[char.lower()] = 1
    return char_dict

def sort_dict_list(dict):
    def sort_on(dict):
        return dict["count"]
    
    list_dict = []

    for key in dict:
        temp_dict = {}
        temp_dict["character"] = key
        temp_dict["count"] = dict[key]
        list_dict.append(temp_dict)

    list_dict.sort(reverse=True, key=sort_on)

    return list_dict