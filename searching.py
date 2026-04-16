from pathlib import Path
import json


def read_data(file_name, field):
    # get current working directory path
    cwd_path = Path.cwd()
    
    file_path = cwd_path / file_name
    with open(file_name, 'r') as file:
        data = json.load(file)
    if field in data:
        return data[field]
    else:
        return None


def linear_search(sequence, searched_number = 2):
    positions = []
    count = 0
    i = 0
    for number in sequence:
        if number == searched_number:
            count += 1
            positions.append(i)
        i += 1
    return positions, count



def main():
    sequential_data = read_data('sequential.json', 'unordered_numbers')
    print(sequential_data)
    searching_number = linear_search([2,4,5,8,30,26,5,4,5,5,4,8], 5)
    print(searching_number)


if __name__ == "__main__":
    main()
