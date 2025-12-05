def count_book_words(book_text):
    list_of_words = book_text.split()
    n_words = len(list_of_words)
    return n_words

def count_characters(book_text):
    lower_cased_text = book_text.lower()

    #iterates over the text and populates the dict to be returned
    char_dict = {}
    for char in lower_cased_text:
        if char not in char_dict:
            char_dict[char] = 1
        else:
            char_dict[char] += 1
    return char_dict

def sort_on(item):
    return item["num"]

def sort_dict(char_d):
    sorted_dict_list = []
    current_dict = {}
    #populates sorted_dict_list with the dictionaries, one for each index
    for d_item in char_d:
        current_dict["char"] = d_item
        current_dict["num"] =  char_d[d_item]
        sorted_dict_list.append(
            {
                "char"  :   current_dict["char"],
                "num"   :   current_dict["num"]
            }
        )
    
    sorted_dict_list.sort(reverse=True, key=sort_on)

    return sorted_dict_list