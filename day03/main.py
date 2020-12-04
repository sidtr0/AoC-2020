arr = []
with open("day03\data.txt") as my_file:
    for line in my_file:
        to_append = line.split('\n')
        arr.append(to_append[0])

def count_trees(x, y):
    xa = 0
    ya = 0
    trees = 0
    while ya < len(arr):
        if arr[ya][xa % len(arr[0])] == "#":
            trees += 1
        xa += x
        ya += y
    return trees

print(count_trees(1, 1) * count_trees(3, 1) * count_trees(5, 1) * count_trees(7, 1) * count_trees(1, 2))