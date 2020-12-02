valid_passwords = 0
with open("day02\data.txt") as my_file:
    for line in my_file:
        n, (c, _), password = line.split(' ')
        pos1, pos2 = n.split("-")
        sum_of_n = 0
        arr = [char for char in password]
        pos1_int = int(pos1) - 1
        pos2_int = int(pos2) - 1
        if arr[pos1_int] == c and arr[pos2_int] != c:
            valid_passwords += 1
        elif arr[pos2_int] == c and arr[pos1_int] != c:
            valid_passwords += 1
        elif arr[pos1_int] == c and arr[pos2_int] == c:
            pass

print(valid_passwords)