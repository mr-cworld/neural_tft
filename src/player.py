#player that holds the heros and makes decisions, will be ran by the ai

class Player():
    def __init__(self, hero, ai):
        self.heroes = []
        self.gold = 0
        self.experience = 0
        self.level = 1
        self.win_streak = 0
        self.health = 100
        self.origins = {}
        self.classes = {}
        
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
        if hero.level == 3:
           return f"Error: Hero {hero} is already max level"
        

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
    
    # Gold Related Methods

    def earn_interest(self):
      interest = max(5,int(self.gold / 10))
      self.gold += interest
      return f"Earned {interest} gold in interest"
    
    def round_end_gold(self):
       self.earn_interest()
       self.gold += 5
       if self.win_streak > 3:
          self.gold += 1
          if self.win_streak > 5:
            self.gold += 1
            if self.win_streak > 7:
              self.gold += 1
              
    # Methods for win/lossing rounds

    def win_round(self):
      self.win_streak += 1
      self.round_end_gold()

    def lose_round(self):
      self.win_streak = 0
      self.round_end_gold()

    # Methods for taking/healing damage

    def take_damage(self, damage):
      self.health -= damage
      if self.health <= 0:
        return "Game Over"
      #TODO - add a endgame method/way to AI to know it lost
      return f"Player took {damage} damage, health is now {self.health}"
    
    def heal_damage(self, heal):
      self.health += heal
      if self.health > 100:
        self.health = 100
      return f"player healed for {heal} health, health is now {self.health}"


    # Method for checking what origins and classes our heroes are, and how many of each we have

    def check_heroes(self):
      origins = {}
      classes = {}
      for hero in self.heroes:
        if hero.origin in origins:
          origins[hero.origin] += 1
        else:
          origins[hero.origin] = 1
        if hero.classes in classes:
          classes[hero.classes] += 1
        else:
          classes[hero.classes] = 1
      
      self.classes = classes
      self.origins = origins
      return origins, classes


    # Need a method that saves team state at end of each round to json, final export will be team at each stage stiched to a giant json file, and then we can make it like backpack battles
    #back pack battles pog
