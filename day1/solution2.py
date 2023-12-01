import re
from data import prod_data as run_data

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

    #Remove not numbers
    d = "".join([x for x in list(d) if x.isdigit()])
    solution += int(d[0] + d[-1])

print(f"Final solution: {solution}")
