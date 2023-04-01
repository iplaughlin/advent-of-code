# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 05:09:18 2022

@author: iaala
"""
with open(
    r"C:\Users\iaala\python_projects\advent-of-code\2022\inputs\day5.txt"
) as file:
    days_input = [item.strip() for item in file.readlines()]
test_input = [
    "move 1 from 2 to 1",
    "move 3 from 1 to 3",
    "move 2 from 2 to 1",
    "move 1 from 1 to 2",
]

stacks_input = list(
    open(r"C:\Users\iaala\python_projects\advent-of-code\2022\inputs\day5_a.txt")
)

test_stack_input = list(["    [D]    ", "[N] [C]    ", "[Z] [M] [P]", " 1   2   3"])


stack1 = []
stack2 = []
stack3 = []
stack4 = []
stack5 = []
stack6 = []
stack7 = []
stack8 = []
stack9 = []
for item in reversed(stacks_input[:-1]):
    out = [part for part in item]
    stack1.append("".join(out[0:3]).strip())
    stack2.append("".join(out[4:7]).strip())
    stack3.append("".join(out[8:11]).strip())
    stack4.append("".join(out[12:15]).strip())
    stack5.append("".join(out[16:19]).strip())
    stack6.append("".join(out[20:23]).strip())
    stack7.append("".join(out[24:27]).strip())
    stack8.append("".join(out[28:31]).strip())
    stack9.append("".join(out[32:35]).strip())
cleaned = []
for stack in [stack1, stack2, stack3, stack4, stack5, stack6, stack7, stack8, stack9]:
    print(stack)
    stack = [item for item in stack if item != ""]
    print("stack is", stack)
    cleaned.append(stack)
test_stack_input = [["[Z]", "[N]"], ["[M]", "[C]", "[D]"], ["[P]"]]


def parse_input(text_input):
    words = [item for item in text_input.split()]
    items = int(words[1])
    from_ = int(words[3])
    to_ = int(words[5])
    return items, from_, to_


def move_item(list_input, from_stack, to_stack):
    in_movement = list_input[from_stack - 1][-1:]
    print("moving", in_movement)
    list_input[from_stack - 1] = list_input[from_stack - 1][:-1]
    list_input[to_stack - 1].extend(in_movement)
    return list_input


for item in days_input:
    number, from_, to_ = parse_input(item)
    print(number, from_, to_)
    for repetition in range(1, number + 1):
        cleaned = move_item(cleaned, from_, to_)
    for item in cleaned:
        print(item[-1])


def move_item_9001(list_input, from_stack, to_stack, number_to_move):
    in_movement = list_input[from_stack - 1][-number_to_move:]
    print("moving", in_movement)
    list_input[from_stack - 1] = list_input[from_stack - 1][:-number_to_move]
    list_input[to_stack - 1].extend(in_movement)
    return list_input


for item in days_input:
    number, from_, to_ = parse_input(item)
    print(number, from_, to_)
    cleaned = move_item_9001(cleaned, from_, to_, number)
for item in cleaned:
    print(item[-1])
