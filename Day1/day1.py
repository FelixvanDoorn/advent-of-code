with open("input.txt", "r") as file:
    lines = file.readlines()

num_lines = [int(l.replace("\n", "")) for l in lines]
result = sum(num_lines)
print(result)
