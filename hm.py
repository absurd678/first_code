class Hero:
    def __init__(self):
        self.data = {}

    def call(self):  
        if self.data[0] == "R'lyeh":
           print("""
                 What a big mistake...
                 """)
           return False
        else:
            print("Your current position is ", self.data[0])
            return True

    def change_position(self, city):
        for num in Point.CITIES:
            if city == num:
                idx = Point.CITIES.index(num)
                self.data.setdefault(Point.CITIES[idx], Point.POSITIONS[idx])
    def clean(self):
        self.data = {}


class Point:
    CITIES = ["r'lyeh", "salem", "arkham", "kingsport", "innsmouth", "boston"]
    POSITIONS = [1500, 10, 20, 30, 60, 40]
    def __init__(self):
        self.locations = {}

    def define_lists(self):
        self.distances = []
        self.cities = []
        for value in self.locations.values():
            self.distances.append(value)
        for city in self.locations.keys():
            self.cities.append(city)

    def current_location(self):  # Defines the nearest cities
        self.define_lists()
        distances = self.distances
        curr_idx = distances.index(min(distances))
        curr_city = self.cities[curr_idx]
        self.change_pos(curr_city)  # Delete nearest to choose another later
        return curr_city

    def change_pos(self, city):   # Removing the chosen city  from dict
        distances = self.distances
        ODD_IDX = self.cities.index(city)
        self.cities.remove(self.cities[ODD_IDX]) 
        distances.remove(distances[ODD_IDX])  
        self.locations = self.delete_items()
        for round in range(len(distances)):
            self.locations.setdefault(self.cities[round], distances[round])
        return self.locations

    def delete_items(self):  # For creating the new dict without trashed city
        self.locations = {}
        return self.locations
    def fill_dict(self):
        for round in range(len(Point.CITIES)):
            self.locations.setdefault(Point.CITIES[round], Point.POSITIONS[round])
        return self.locations

if __name__=='__main__':
    print("You've played the module")
