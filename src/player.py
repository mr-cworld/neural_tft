#player that holds the heros and makes decisions, will be ran by the ai

class Player():
    def __init__(self, hero, ai):
        self.heroes = []
        self.gold = 0
        self.experience = 0
        self.level = 1
        
    # Hero Related Methods

    def add_hero(self, hero):
        self.heroes.append(hero)
    
    def remove_hero(self, hero):
        self.heroes.remove(hero)

    def level_up_hero(self, hero):
        if hero.level == 1:
          if self.gold > hero.level_cost:
            self.gold -= hero.level_cost
            hero.level_up()
        if hero.level == 2:
          if self.gold > hero.level_cost:
            self.gold -= hero.level_cost
            hero.level_up()

    def buy_hero(self, hero):
        if self.gold > hero.cost:
            self.gold -= hero.cost
            self.add_hero(hero)

    def sell_hero(self, hero):
        self.gold += hero.cost
        self.remove_hero(hero)
  
    def buy_xp(self):
        if self.gold > 4:
            self.gold -= 4
            self.experience += 4
            self.check_level_up()  
    
    def get_xp(self):
      self.experience += 2
      self.check_level_up()

    # User Exp Related Methods
    # Create a table dictionary for level up experience requirements

    def level_up(self):       
      self.level += 1
      self.experience = 0

    level_up_table = {1:0, 2:2, 3:6, 4:10, 5:20, 6:36, 7:56, 8:80, 9:100, 10:120}
    
    def check_level_up(self):
      if self.experience >= self.level_up_table[self.level]:
        self.level_up()
        return True
      return False