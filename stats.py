def get_num_words(text) :
    return len(text.split())

def freaquency(text):
    character = {}
    for char in text.lower():
        if char not in character:
            character[char] = 1
        else:
            character[char] += 1
    
    return character

def sort_on(items):
    return items["num"]

def sort_dict(unsorted):
    sorted_items = []
    for key, value in unsorted.items():
        sorted_items.append({"char" : key, "num" : value})
    
    sorted_items.sort(reverse=True, key=sort_on)

    return sorted_items