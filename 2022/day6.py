# -*- coding: utf-8 -*-

with open(
    r"C:\Users\iaala\python_projects\advent-of-code\2022\inputs\day6.txt"
) as file:
    days_input = [item.strip() for item in file.readlines()]
test_input = [
    "mjqjpqmgbljsphdztnvjfqwrcgsmlb",
    "bvwbjplbgvbhsrlpgdmjqwftvncz",
    "nppdvjthqldpwncqszvftbrmjlhg",
    "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg",
    "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw",
]


def find_position(text_input, size_of_window=4, offset=0):
    window = text_input[offset : size_of_window + offset]
    if len(set(window)) != len(window):
        result = find_position(
            text_input, offset=offset + 1, size_of_window=size_of_window
        )
    else:
        result = offset + size_of_window
    return result


for item in days_input:

    print(find_position(item[1500:], size_of_window=14) + 1500)
