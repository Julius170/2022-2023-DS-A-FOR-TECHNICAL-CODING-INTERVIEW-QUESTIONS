# STACKS


ops = ["5", "2", "C", "D", "+"]
# ops = ["5", "-2", "4", "C", "D", "9", "+", "+"]
arr = []
for i in ops:
    if i == "D":
        prev = arr[-1]
        print(arr)
        arr.append(prev * prev)
    elif i == "C":
        arr.pop()
        print(arr)
    elif i== "+":
        arr.append(arr[-1] + arr[-2])
        print(arr)
    else:
        arr.append(int(i))
        print(arr)

print(arr[-1])