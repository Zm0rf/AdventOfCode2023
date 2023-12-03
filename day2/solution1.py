from data import prod_data as run_data
#from data import test_data as run_data
import re

def get_dict_value(d, v, default=0):
    if v in d:
        return d[v]
    return default

class Reveal(object):
    def __init__(self, data):
        self.red = int(get_dict_value(data, "red"))
        self.green = int(get_dict_value(data, "green"))
        self.blue = int(get_dict_value(data, "blue"))
        self.total = self.red + self.green + self.blue

    def print(self):
        print( f"{self.red} {self.green} {self.blue}  = {self.total}")
       
    def validate(self, validator) -> bool:
        if self.red <= validator["red"] and \
            self.green <= validator["green"] and \
            self.blue <= validator["blue"] and \
            self.total <= validator["total"]:
            return True
        return False

class Game(object):
    def __init__(self, data):
        self.id = -1
        self.reveals = []
        self.is_valid = True
        self.min_red = 0
        self.min_blue = 0
        self.min_green = 0

        self.parse_data(data)

    def print(self):
        print(f"######Game {self.id} ##########")
        for r in self.reveals:
            r.print()

    def get_min_cube_values(self, reveal):
        if reveal.red > 0 and reveal.red > self.min_red:
            self.min_red = reveal.red
        if reveal.blue > 0 and reveal.blue > self.min_blue:
            self.min_blue = reveal.blue
        if reveal.green > 0 and reveal.green > self.min_green:
            self.min_green = reveal.green


    def parse_data(self, data):
        #Get id
        split_data = data.split(":")
        self.id = int(split_data[0].split(" ")[1])

        #Parse reveal data
        reveal_data = split_data[1].split(";")
        for x, reveal in enumerate(reveal_data):
            dict_data = {
                "green": 0,
                "red": 0,
                "blue": 0
            }
            colors = reveal.split(",")
            for color in colors:
                parts = color.strip().split(" ")
                dict_data[parts[1]] = int(parts[0])
            self.reveals.append(Reveal(dict_data))

    def validate(self, validator):
        self.is_valid = True
        for x, rev in enumerate(self.reveals):
            if not rev.validate(validator):
                self.is_valid = False
                break

    def power(self):
        self.min_red = 0
        self.min_blue = 0
        self.min_green = 0
        for rev in self.reveals:
            self.get_min_cube_values(rev)
        #print(f"Game {self.id}   {self.min_red}  {self.min_green}  {self.min_blue}")
        return self.min_red * self.min_green * self.min_blue

class Solver(object):
    def __init__(self):
        self.games = []
        

    def load_data(self, data):
        for d in data:
            self.games.append(Game(d))

    def print_all_games(self):
        for g in self.games:
            g.print()

    def validate(self, validator):
        #Calculate total
        validator["total"] = validator["red"] + validator["green"] + validator["blue"]
        for g in self.games:
            g.validate(validator)

    def solve(self):
        ret = 0
        for g in self.games:
            if g.is_valid:
                #print(f"Game {g.id} is valid")
                ret += g.id
        return ret

    def power(self):
        ret = 0
        for g in self.games:
            #print(f"Power of game {g.id} = {g.power()}")
            ret += g.power()
        return ret

if __name__=='__main__':
    s = Solver()
    s.load_data(run_data.strip().strip().split("\n"))
    #s.print_all_games()
    s.validate({
        "red": 12,
        "green": 13,
        "blue": 14
        })
    print(f"Solve: {s.solve()}")
    print(f"Power: {s.power()}")
