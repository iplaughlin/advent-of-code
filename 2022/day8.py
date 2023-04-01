# -*- coding: utf-8 -*-

with open(
    r"C:\Users\iaala\python_projects\advent-of-code\2022\inputs\day8.txt"
) as file:
    days_input = [item.strip() for item in file.readlines()]
test_input = [
    "30373",
    "25512",
    "65332",
    "33549",
    "35390",
]

to_matrix = [[int(part) for part in item] for item in days_input]

R, C = len(to_matrix), len(to_matrix[0])

ans1, ans2 = 0, 0
for r in range(R):
    for c in range(C):
        visible = not any(to_matrix[r][cc] >= to_matrix[r][c] for cc in range(0, c))
        visible |= not any(
            to_matrix[r][cc] >= to_matrix[r][c] for cc in range(c + 1, C)
        )
        visible |= not any(to_matrix[rr][c] >= to_matrix[r][c] for rr in range(0, r))
        visible |= not any(
            to_matrix[rr][c] >= to_matrix[r][c] for rr in range(r + 1, R)
        )
        ans1 += int(visible)
        score = abs(
            c
            - next(
                (
                    cc
                    for cc in range(c - 1, -1, -1)
                    if to_matrix[r][cc] >= to_matrix[r][c]
                ),
                0,
            )
        )
        score *= abs(
            c
            - next(
                (cc for cc in range(c + 1, C) if to_matrix[r][cc] >= to_matrix[r][c]),
                C - 1,
            )
        )
        score *= abs(
            r
            - next(
                (
                    rr
                    for rr in range(r - 1, -1, -1)
                    if to_matrix[rr][c] >= to_matrix[r][c]
                ),
                0,
            )
        )
        score *= abs(
            r
            - next(
                (rr for rr in range(r + 1, R) if to_matrix[rr][c] >= to_matrix[r][c]),
                R - 1,
            )
        )
        ans2 = max(ans2, score)
print(f"part 1: {ans1}")
print(f"part 2: {ans2}")
