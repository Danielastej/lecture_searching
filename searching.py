import os
import json

from setuptools.dist import sequence

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
    with open(file_name, "r") as file:
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

if __name__ == '__main__':
    my_list = [1, 2, 5, 7]
    searched_number = 5
    found_numbers = linear_search(my_list, searched_number)
    print(found_numbers)