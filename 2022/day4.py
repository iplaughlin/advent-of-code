# -*- coding: utf-8 -*-

with open(
    r"C:\Users\iaala\python_projects\advent-of-code\2022\inputs\day4.txt"
) as file:
    days_input = [item.strip() for item in file.readlines()]
test_input = [
    "2-4,6-8",
    "2-3,4-5",
    "5-7,7-9",
    "2-8,3-7",
    "6-6,4-6",
    "2-6,4-8",
]

x = 0
for item in days_input:
    part1, part2 = item.split(",")
    a, b = part1.split("-")
    c, d = part2.split("-")
    first = list(range(int(a), int(b) + 1))
    second = list(range(int(c), int(d) + 1))
    if set(first).issubset(second):
        print(first, second)

        x += 1
    elif set(second).issubset(first):
        print(first, second)
        x += 1
x = 0
for item in days_input:
    part1, part2 = item.split(",")
    a, b = part1.split("-")
    c, d = part2.split("-")
    first = list(range(int(a), int(b) + 1))
    second = list(range(int(c), int(d) + 1))
    if set(first).intersection(second):
        print(set(first).intersection(second))

        x += 1
