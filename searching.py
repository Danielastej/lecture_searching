import os
import json


# get current working directory path
cwd_path = os.getcwd()


def read_data(file_name, field):
    """
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param field: (str), field of a dict to return
    :return: (list, string),
    """
    file_path = os.path.join(cwd_path, file_name)
    with open(file_path, "r") as file:
        data = json.load(file)
    if field in data.keys():
        return data[field]
    else:
        print(f'field {field} not exist.')
        return None

def linear_search(list_of_numbers, number):
    list_of_idxs = []
    for idx, element in enumerate(list_of_numbers):
        if element == number:
            list_of_idxs.append(idx)
        else:
            pass
    return {"positions": list_of_idxs, "count": len(list_of_idxs)}


def main():
    json_filename = "sequential.json"
    my_data = read_data(json_filename, "unordered_numbers")
    print(my_data)
    found_numbers_linear = linear_search(my_data,0)

def pattern_search(sequence, pattern):
    set_of_idx = set()
    pattern_length = len(pattern)
    for idx in range(0, len(sequence) - pattern_length):
        pattern_similarity = 0
        for idx_pattern, pattern_element in enumerate(pattern):
            if sequence[idx + idx_pattern] == pattern_element:
                pattern_similarity = pattern_similarity + 1
            else:
                break
        if pattern_similarity == pattern_length:
            set_of_idx.add(idx + pattern_length // 2 - 1)
        else:
            pass
    return set_of_idx

def pattern_search_while(sequence, pattern):
    pos = set()
    index = 0
    while index < len(sequence) - len(pattern):
        if sequence[index:index + len(pattern)] == pattern:
            pos.add(index)
        index = index + 1
    return pos

def binary_search(sequence, number):
    left = 0
    right = len(sequence) - 1
    while right >= left:
        middle = (left + right) // 2
        print(sequence[middle])
        if sequence[middle] == number:
            return middle
        elif sequence[middle] > number:
            return middle - 1
        elif sequence[middle] < number:
            left = middle + 1
    return None

if __name__ == '__main__':
    main()
    my_list = [1, 2, 5, 7]
    searched_number = 5
    found_numbers = linear_search(my_list, searched_number)
    print(found_numbers)