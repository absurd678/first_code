# Welcome to Move! game!
# In this game the player is allowed to choose one of two nearest locations and get the small task
# The forbidden location is the Ctulhu's grave - the R'lyeh
# Here the main attributes are dictionaries, in case of its usefulness for this game
# The class-composite is here, the components are in modules
import hm
import content

class HM_Hero(hm.Hero):
    def died(self):
        print(
              """
              Y̴̗͙͇͒̒̓O̸̖͎͎̾Ụ̶̟̲̝͑̓͊ ̷͙͖͝D̶͓̤͔̤͋̌̓I̴̛̥̘͉̻̓̈È̵̹͕̻͈̻́͗D̴͎̜̲̟͉̊͛
              """
        )
    def saved(self):
        print("""
              You've succeed all Ctulchu's challenges!
              """)

    def find_nearest(self, other):
        cities = []
        for i in range(2):
            cities.append(other.current_location())
        for city in cities:
            self.change_position(city)

    def suggest(self):  # Doesn't real matter
        rep = 'Which city force? ( '
        for cities, values in self.data.items():
            rep += cities + "/"
        rep += ")"
        return rep  # for the question

    def odd_variant(self, other):
        city_chosen = str(input(self.suggest())).lower()  # Condition
        for city, value in self.data.items():
            if city != city_chosen:
                other.return_city(city, value)
        self.clean()
        self.data.setdefault(0, city_chosen)

class HM_Locations(hm.Point):
    def reached(self):
        cities = 0
        for keys, values in self.locations.items():
            cities += 1
        if cities < 2:
            return False
        else:
            return True
    def return_city(self, city, value):
        self.locations.setdefault(city, value)

class Content(content.Victorina):
    def reached(self):
        return self.quiz == {}

class Game:
    def __init__(self):
        self.player = HM_Hero()
        self.locations = HM_Locations()
        self.content = Content()
    def game(self):
        self.content.fill_variants()
        self.locations.fill_dict()
        while not self.content.reached():
            self.player.clean()
            self.player.find_nearest(self.locations)
            self.player.odd_variant(self.locations)
            if self.player.call():
                self.content.ask_question()
                if not self.locations.reached():
                    self.locations.fill_dict()
                if self.content.reached():
                    self.player.saved()
                    break
            else:  # If you've chosen the R'lyeh...
                self.player.died()
                break
game = Game()
game.game()

