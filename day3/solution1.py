#from data import test_data as run_data
from data import prod_data as run_data
from termcolor import colored

class PartNumber(object):
    def __init__(self, part_number, x1, x2, y):
        self.is_part = False
        self.part_number = int(part_number)
        self.x1 = x1
        self.x2 = x2
        self.y = y

    def print(self):
        print(f"PartNumber {self.is_part}  {self.part_number}  @  {self.y} {self.x1} to {self.x2}")

    def validate(self, symboles):
        self.is_part = False
        for symbole in symboles:
            if self.y-1 <= symbole.y <= self.y+1 and \
                symbole.x >= self.x1-1 and \
                symbole.x <= self.x2+1:
                self.is_part = True
                break

class Symbole(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def print(self):
        print(f"Symbole @ {self.y} {self.x}")

class Solver(object):
    def __init__(self):
        self.parts = []
        self.symboles = []

    def parse_schematic(self, schematic):
        for y, row in enumerate(schematic):
            num_x = -1
            for x, char in enumerate(row):
                #print(f"{char} @ {y} {x}")
                if not char.isdigit() and char != ".":
                    self.symboles.append(Symbole(x, y))

                if char.isdigit() and num_x == -1:
                    num_x = x
                elif not char.isdigit() and num_x != -1:
                    self.parts.append(PartNumber(row[num_x:x].strip(), num_x, x-1, y))
                    num_x = -1
                #elif num_x != -1 and x == len(row):
                    #num_x = -1
            if num_x != -1:
                self.parts.append(PartNumber(row[num_x:len(row)].strip(), num_x, len(row)-1, y))

        #for sym in self.symboles:
            #sym.print()
        for part in self.parts:
            part.validate(self.symboles)
            #part.print()

    def print_board(self, schematic):
        print(f"Number of rows: {len(schematic)}")
        for y, row in enumerate(schematic):
            # Fix row
            parts = [part for part in self.parts if part.y == y]
            x = 0
            while x < len(row):
                cont = True
            #for x in range(len(row)):
                for part in parts:
                    if part.x1 == x:
                        if part.is_part:
                            print(colored(str(part.part_number), 'green'), end="")
                        else:
                            print(colored(str(part.part_number), 'red'), end="")
                        x = part.x2+1
                        cont = False
                if cont:
                    print(row[x], end="")
                    x += 1
            print("")

    def sum(self):
        ret = 0
        for part in self.parts:
            if part.is_part:
                ret += part.part_number
        return ret

if __name__=='__main__':
    solver = Solver()

    solver.parse_schematic(run_data.strip().split("\n"))
    print(solver.sum())
    #solver.print_board(run_data.strip().split("\n"))
