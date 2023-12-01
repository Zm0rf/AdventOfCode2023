import re
from data import prod_data as run_data
#from data import test_data2 as run_data

split_data = run_data.strip().split("\n")
solution = 0

conversions = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}

for i, d in enumerate(split_data):
    mods = []
    #Find first position of all conversions
    for k, v in conversions.items():
        mods += [(m.start(), v) for m in re.finditer(k, d)]

    #Replace conversions
    for mod in mods:
        d = d[:mod[0]] + mod[1] + d[mod[0] + 1:]

    first_num = ""
    last_num = ""

    #Find first number
    for x in range(0, len(d)):
        if d[x].isdigit():
            first_num = d[x]
            break
    
    #Find second number
    for x in range(len(d)-1, -1, -1):
        if d[x].isdigit():
            last_num = d[x]
            break
    
    #Append to solution
    solution += int(str(first_num + last_num))

print(f"Final solution: {solution}")
