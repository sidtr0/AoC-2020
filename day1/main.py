arr = []
with open("day1\data.txt") as my_file:
    for line in my_file:
        
        arr.append(int(line.split('\n')[0]))

print(arr)

for i in arr:
    for x in arr:
        for y in arr:
            if i + x + y == 2020:
                print(i*x*y)
            else:
                pass