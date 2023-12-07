from data import test_data as run_data

class Race(object):
    def __init__(self, time):
        self.max_time = time
        self.required_distance = 0
        self.solutions = []


    def solve(self):
        min_speed = self.required_distance


    def print(self):
        print(f"{self.max_time}  - {self.required_distance}")


class Solver(object):
    def __init__(self, data):
        self.races = []
        for row in data:
            splits = row.split(":")
            if splits[0] == "Time":
                #Parse Times
                times = [time for time in splits[1].strip().split(" ") if time != ""]
                for time in times:
                    self.races.append(Race(time))

            elif splits[0] == "Distance":
                #Parse distances
                distances = [dist for dist in splits[1].strip().split(" ") if dist != ""]
                for x, distance in enumerate(distances):
                    self.races[x].required_distance = distance

    def print(self):
        for race in self.races:
            race.print()
        

if __name__=='__main__':
    solver = Solver(run_data.strip().split("\n"))
    solver.print()
