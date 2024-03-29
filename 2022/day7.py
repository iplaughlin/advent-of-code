# -*- coding: utf-8 -*-

with open(
    r"C:\Users\iaala\python_projects\advent-of-code\2022\inputs\day7.txt"
) as file:
    days_input = [item.strip() for item in file.readlines()]
test_input = [
    "$ cd /",
    "$ ls",
    "dir a",
    "14848514 b.txt",
    "8504156 c.dat",
    "dir d",
    "$ cd a",
    "$ ls",
    "dir e",
    "29116 f",
    "2557 g",
    "62596 h.lst",
    "$ cd e",
    "$ ls",
    "584 i",
    "$ cd ..",
    "$ cd ..",
    "$ cd d",
    "$ ls",
    "4060174 j",
    "8033020 d.log",
    "5626152 d.ext",
    "7214296 k",
]


from pathlib import Path


def get_dir_tree(commands: list[str]) -> dict:
    level = Path("")
    dir_tree = {}
    for entry in commands:
        if "$ cd" in entry:
            if ".." in entry:
                level = level.parent
            else:
                direc_name = entry[5:]
                level = level / direc_name
                if level not in dir_tree:
                    dir_tree[level] = []
        elif "dir" in entry:
            _, direc_name = entry.split(" ")
            dir_tree[level].append(level / direc_name)
        elif entry[0].isnumeric():
            file_size, file_name = entry.split(" ")
            dir_tree[level].append((file_name, int(file_size)))
    return dir_tree


def total_dir_size(dir_path: Path, dir_tree: dict) -> int:
    total_size = 0
    for object in dir_tree[dir_path]:
        if isinstance(object, tuple):
            total_size += object[1]
        elif isinstance(object, Path):
            total_size += total_dir_size(object, dir_tree)
    return total_size


def get_dir_sizes(dir_tree: dict) -> dict:
    return {dir: total_dir_size(dir, dir_tree) for dir in dir_tree}


def part_1(dir_sizes: dict, threshold: int) -> int:
    return sum(dir_size for dir_size in dir_sizes.values() if dir_size < threshold)


def part_2(dir_sizes: dict, max_disk_space: int, required_disk_space: int) -> None:
    total_space_used = dir_sizes[Path("/")]
    initial_free_space = max_disk_space - total_space_used
    clearable_space = required_disk_space - initial_free_space

    min_removeable_dir = (max_disk_space, Path("Random/Path"))

    for dir in dir_sizes:
        if dir_sizes[dir] >= clearable_space:
            if dir_sizes[dir] < min_removeable_dir[0]:
                min_removeable_dir = (dir_sizes[dir], dir)
    return min_removeable_dir[0]


dir_tree = get_dir_tree(days_input)
dir_sizes = get_dir_sizes(dir_tree)

part_1_ans = part_1(dir_sizes, threshold=100_000)
print(part_1_ans)

part_2_ans = part_2(
    dir_sizes, max_disk_space=70_000_000, required_disk_space=30_000_000,
)
print(part_2_ans)
