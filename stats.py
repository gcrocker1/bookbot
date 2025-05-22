def count_words(text):
    num_words = len(text.split())
    return num_words

def count_characters(text):
    character_counts = {}
    for char in text.lower():
        if char not in character_counts.keys():     # If we've not encountered the char before, add it to dict with count of 1
            character_counts[char] = 1
        else:                                   # Otherwise, just increment the count
            character_counts[char] += 1
    return character_counts

def sort_on(dict):
    return dict["num"]

def sort_dict(character_counts):
    sorted_dict_list = []
    for key, value in character_counts.items():
        sorted_dict_list.append({"char": key, "num": value})
    sorted_dict_list.sort(reverse=True, key=sort_on)
    return sorted_dict_list