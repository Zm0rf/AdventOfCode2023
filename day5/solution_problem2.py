#from data import test_data as run_data
from data import prod_data as run_data

class Map(object):
    def __init__(self, source, dest, diff):
        self.source = source
        self.dest = dest
        self.diff = diff

    def check(self, value):
        return self.source <= value <= (self.source+(self.diff-1))

    def get_dest(self, value):
        return self.dest+(value-self.source)

    def print_map(self):
        for x in range(self.diff):
            print(f"{self.source+x} : {self.dest+x}")

class SeedRange(object):
    def __init__(self, start, length):
        self.start = start
        self.length = length

    def range(self):
        ret = []
        for x in range(self.start, self.start+self.length, 1):
            ret.append(x)
        return ret

    def range2(self):
        return range(self.start, self.start+self.length, 1)

class Solver(object):
    def __init__(self):
        self.seeds = []
        self.seed_to_soil = []
        self.soil_to_fertilizer = []
        self.fertilizer_to_water = []
        self.water_to_light = []
        self.light_to_temperature = []
        self.temperature_to_humidity = []
        self.humidity_to_location = []


    def parse_data(self, data):
        target_map = None
        for row in data:
            #Parse seeds
            if "seeds:" in row:
                seed_data = [int(seed) for seed in row.split(":")[1].split(" ") if seed != ""]
                for x in range(0, len(seed_data), 2):
                    self.seeds.append(SeedRange(int(seed_data[x]), int(seed_data[x+1])))

                #print(f"Seeds: {self.seeds}")
            #Parse seed-to-soil
            elif "seed-to-soil map:" in row:
                #print("Switching to seed-to-soil")
                target_map = self.seed_to_soil
            elif "soil-to-fertilizer map:" in row:
                #print("Switching to seed-to")
                target_map = self.soil_to_fertilizer
            elif "fertilizer-to-water map:" in row:
                target_map = self.fertilizer_to_water
            elif "water-to-light map:" in row:
                target_map = self.water_to_light
            elif "light-to-temperature map:" in row:
                target_map = self.light_to_temperature
            elif "temperature-to-humidity map:" in row:
                target_map = self.temperature_to_humidity
            elif "humidity-to-location map:" in row:
                target_map = self.humidity_to_location
            elif row != "":
                #print(f"Parsing value: {row}")
                splits = row.strip().split(" ")
                target_map.append(Map(int(splits[1]), int(splits[0]), int(splits[2])))
                #for x in range(int(splits[2])):
                    #target_map[int(splits[1])+x] = int(splits[0])+x

    def get_dest(self, value, source_map):
        #print(f"Checking value: {value}")
        for m in source_map:
            if m.check(value):
                #print(f"Returning: {m.get_dest(value)}")
                return m.get_dest(value)
        #print(f"Returning: {value}")
        return value

    def get_all_seed_ranges(self):
        ret = []
        for seed_range in self.seeds:
            #print(seed_range.range())
            ret += [seed_range.range2()]
        return ret

    def find_lowest_seed(self):
        ret = -1
        #print(self.get_all_seeds())
        print(f"Checking ranges: {self.get_all_seed_ranges()}")
        for r in self.get_all_seed_ranges():
            print(f"Checking range: {r}")
            for seed in r:
                #print(f"Checking seed: {seed}")
                soil = self.get_dest(seed, self.seed_to_soil)
                #print(f"Soil: {soil}")
                fertilizer = self.get_dest(soil, self.soil_to_fertilizer)
                #print(f"Fertilizer: {fertilizer}")
                water = self.get_dest(fertilizer, self.fertilizer_to_water)
                #print(f"Water: {water}")
                light = self.get_dest(water, self.water_to_light)
                #print(f"Light: {light}")
                temperature = self.get_dest(light, self.light_to_temperature)
                #print(f"Temperature: {temperature}")
                humidity = self.get_dest(temperature, self.temperature_to_humidity)
                #print(f"Humidity: {humidity}")
                location = self.get_dest(humidity, self.humidity_to_location)
                #print(f"Location: {location}")
                if location < ret or ret == -1:
                    ret = location
                #print(" ")
        return ret

    def print(self):
        print(f"Seeds:  {self.seeds}")
        for m in self.seed_to_soil:
            m.print_map()


if __name__=='__main__':
    solver = Solver()
    solver.parse_data(run_data.strip().split("\n"))
    #solver.print()
    print(solver.find_lowest_seed())
