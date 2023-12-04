#from data import test_data as run_data
from data import prod_data as run_data
import math

class Card(object):
    def __init__(self, data, solver):
        d = data.split(":")[0].split(" ")
        self.id = int(d[len(d)-1])
        self.solver = solver
        self.copy = 1
        
        numbers = data.split(":")[1].split("|")

        self.winning_numbers = [x for x in numbers[0].strip().split(" ") if x.isdigit()]
        self.my_numbers = [x for x in numbers[1].strip().split(" ") if x.isdigit()]
        self.num_my_winning_numbers = 0
        self.points = 0

    def calculate(self):
        self.num_my_winning_numbers = len([n for n in self.my_numbers if n in self.winning_numbers])
        #if self.num_my_winning_numbers > 0:
            #self.points = int(1*math.pow(2,self.num_my_winning_numbers-1))
        #print(f"Card {self.id} has {self.points} points from {self.num_my_winning_numbers}")
        #print(f"Card {self.id} [{self.copy}] has {self.num_my_winning_numbers}")
        for x in range(self.id+1, self.num_my_winning_numbers+self.id+1):
            #print(f"Increasing card {x} with {self.copy}")
            self.solver.cards[x].copy += self.copy


class Solver(object):
    def __init__(self, data):
        self.cards = dict()
        for row in data:
            d = row.split(":")[0].split(" ")
            i = int(d[len(d)-1])
            self.cards[i] = Card(row, self)

        for k,v in self.cards.items():
            v.calculate()

    def calculate(self):
        num = 0
        for k, card in self.cards.items():
            num += card.copy
        return num

if __name__=='__main__':
    solver = Solver(run_data.strip().split("\n"))
    print(solver.calculate())

