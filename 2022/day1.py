# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 08:19:12 2022

@author: iaala
"""
with open(
    r"C:\Users\iaala\python_projects\advent_of_code\2022\inputs\day1.txt"
) as file:
    days_input = [item.strip() for item in file.readlines()]
size = len(days_input)
idx_list = [idx + 1 for idx, val in enumerate(days_input) if val == ""]

results = [
    days_input[i:j]
    for i, j in zip([0] + idx_list, idx_list + ([size] if idx_list[-1] != size else []))
]

inted = []
for calorie_list in results:
    temp_list = []
    for item in calorie_list:
        try:
            temp_list.append(int(item))
        except ValueError:
            pass
    inted.append(sum(temp_list))
print(max(inted))
sum(sorted(inted)[-3:])
