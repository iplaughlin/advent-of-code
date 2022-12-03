# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 08:19:12 2022

@author: iaala
"""
with open(
    r"C:\Users\iaala\python_projects\advent_of_code\2022\inputs\day2.txt"
) as file:
    days_input = [item.strip().split() for item in file.readlines()]
# played
"A"
"B"
"C"

# played
"X"
"Y"
"Z"


{"A": "Rock", "B": "Paper", "C": "Scissors"}
{"X": "Rock", "Y": "Paper", "Z": "Scissors"}


def result(opponent_choice, your_choice):
    if opponent_choice == "A" and your_choice == "X":
        return score(your_choice, "draw")
    elif opponent_choice == "A" and your_choice == "Y":
        return score(your_choice, "win")
    elif opponent_choice == "A" and your_choice == "Z":
        return score(your_choice, "loss")
    if opponent_choice == "B" and your_choice == "X":
        return score(your_choice, "loss")
    elif opponent_choice == "B" and your_choice == "Y":
        return score(your_choice, "draw")
    elif opponent_choice == "B" and your_choice == "Z":
        return score(your_choice, "win")
    if opponent_choice == "C" and your_choice == "X":
        return score(your_choice, "win")
    elif opponent_choice == "C" and your_choice == "Y":
        return score(your_choice, "loss")
    elif opponent_choice == "C" and your_choice == "Z":
        return score(your_choice, "draw")


def score(your_choice, win_loss_draw):
    scores = {"X": 1, "Y": 2, "Z": 3}
    if win_loss_draw == "win":
        outcome = 6
    elif win_loss_draw == "loss":
        outcome = 0
    elif win_loss_draw == "draw":
        outcome = 3
    return scores[your_choice.upper()] + outcome


test = [["A", "Y"], ["B", "X"], ["C", "Z"]]
for item in test:
    print(result(item[0], item[1]))
results = []
for item in days_input:
    results.append(result(item[0], item[1]))
print(sum(results))


def pick_your_choice(opponent_choice, round_end):
    if opponent_choice == "A" and round_end == "X":
        return score("Z", "loss")
    elif opponent_choice == "A" and round_end == "Y":
        return score("X", "draw")
    elif opponent_choice == "A" and round_end == "Z":
        return score("Y", "win")
    if opponent_choice == "B" and round_end == "X":
        return score("X", "loss")
    elif opponent_choice == "B" and round_end == "Y":
        return score("Y", "draw")
    elif opponent_choice == "B" and round_end == "Z":
        return score("Z", "win")
    if opponent_choice == "C" and round_end == "X":
        return score("Y", "loss")
    elif opponent_choice == "C" and round_end == "Y":
        return score("Z", "draw")
    elif opponent_choice == "C" and round_end == "Z":
        return score("X", "win")


for item in test:
    print(pick_your_choice(item[0], item[1]))
results2 = []
for item in days_input:
    temp = pick_your_choice(item[0], item[1])
    results2.append(pick_your_choice(item[0], item[1]))
print(sum(results2))
