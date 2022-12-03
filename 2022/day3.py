# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 07:28:29 2022

@author: iaala
"""
import string

with open(
    r"C:\Users\iaala\python_projects\advent_of_code\2022\inputs\day3.txt"
) as file:
    days_input = [item.strip() for item in file.readlines()]
test_input = [
    "vJrwpWtwJgWrhcsFMMfFFhFp",
    "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
    "PmmdzqPrVvPwwTWBwg",
    "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
    "ttgJtRGJQctTZtZT",
    "CrZsJsPPZsGzwwsLwLmpwMDw",
]

values = []
for item in days_input:
    part1, part2 = (
        item[slice(0, len(item) // 2)],
        item[slice(len(item) // 2, len(item))],
    )
    out = list({item for item in part1 if item in part2})
    print(out)
    if out[0] in string.ascii_lowercase:
        values.append(string.ascii_lowercase.index(out[0]) + 1)
    if out[0] in string.ascii_uppercase:
        values.append(string.ascii_uppercase.index(out[0]) + 27)
print(sum(values))

import string

string.lowercase.index("b")


def divide_chunks(l, n):
    for i in range(0, len(l), n):
        yield l[i : i + n]


n = 3

second_half = list(divide_chunks(days_input, n))

values2 = []
for group in second_half:
    ruck1, ruck2, ruck3 = group
    out = list(set(ruck1).intersection(ruck1, ruck2, ruck3))
    if out[0] in string.ascii_lowercase:
        values2.append(string.ascii_lowercase.index(out[0]) + 1)
    if out[0] in string.ascii_uppercase:
        values2.append(string.ascii_uppercase.index(out[0]) + 27)
print(sum(values2))
