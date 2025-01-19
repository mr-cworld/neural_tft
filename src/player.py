#player that holds the heros and makes decisions, will be ran by the ai

class Player():
    MAX_BENCH_SIZE = 5
    MAX_HEALTH = 100
    SELL_RETURN_RATE = 0.8
    XP_BUY_COST = 4
    BASE_ROUND_GOLD = 3

    def __init__(self, hero, ai):
        self.board = []
        self.bench = []
        self.gold = 0
        self.experience = 0
        self.level = 1
        self.win_streak = 0
        self.health = self.MAX_HEALTH
        self.origins = {}
        self.classes = {}
        
    # Hero Related Methods

    def add_hero(self, hero, to_bench=True):
        if to_bench:
            if len(self.bench) >= 5:
                return f"Error: Bench is full (max 5)"
            self.bench.append(hero)
        else:
            if len(self.board) >= self.level:
                return f"Error: Board is full (max {self.level})"
            self.board.append(hero)
    
    def remove_hero(self, hero):
        if hero in self.bench:
            self.bench.remove(hero)
        elif hero in self.board:
            self.board.remove(hero)
        else:
            return f"Error: Hero {hero} not found"

    def level_up_hero(self, hero):
        if hero not in self.bench and hero not in self.board:
            return f"Error: Hero {hero} not found"
            
        if hero.level == 1:
            if self.gold >= hero.level_cost:
                self.gold -= hero.level_cost
                hero.level_up()
        elif hero.level == 2:
            if self.gold >= hero.level_cost:
                self.gold -= hero.level_cost
                hero.level_up()
        else:
            return f"Error: Hero {hero} is already max level"

    def buy_hero(self, hero):
        if self.gold >= hero.cost:
            if len(self.bench) >= 5:
                return f"Error: Bench is full (max 5)"
            self.gold -= hero.cost
            self.add_hero(hero, to_bench=True)
        else:
            return f"Error: Not enough gold"

    def sell_hero(self, hero):
        if hero not in self.bench and hero not in self.board:
            return f"Error: Hero {hero} not found"
        self.gold += int(hero.cost * self.SELL_RETURN_RATE)
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
       self.gold += 3
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
        for hero in self.board:
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

    def swap_hero(self, hero, target):
        self.bench.remove(hero)
        self.board.remove(target)  
        self.board.append(hero)  
        self.bench.append(target)  
        return f"Hero {hero} has been swapped with {target}"

  #Methods for checking if player has any alive heroes / removing dead ones

    def is_alive(self) -> bool:
        """Check if the player has any heroes on their board"""
        return len(self.board) > 0
    
    def has_living_heroes(self) -> bool:
        """Check if the player has any heroes with HP > 0"""
        return any(hero.hp > 0 for hero in self.board)

    def remove_dead_heroes(self):
        """Remove any heroes with 0 or less HP from the board"""
        self.board = [hero for hero in self.board if hero.hp > 0]

    # Need a method that saves team state at end of each round to json, final export will be team at each stage stiched to a giant json file, and then we can make it like backpack battles
    #back pack battles pog

