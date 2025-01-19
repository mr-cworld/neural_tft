from heroes.hero import Hero

class Terran(Hero):
  origin = 'Earth'
  
  def __init__(self, name):
      super().__init__(name)
      self.name = 'Terran'
      #Stats
      self.str = 55
      self.agi = 25
      self.max_hp = 555
      self.hp = self.max_hp
      self.armor = 0.35
      self.magic_resist = 0.35     
      # Mana
      self.mana = 2
      self.max_mana = 7
      self.starting_mana = 2
      #Core Stats
      self.origin = 'Earth'
      self.classes = 'Tank'
      self.ability = self.ability_name() # if I wanted to create self.ability()?
      self.level_cost = 6
      self.buy_price = 1

  def ability_name(self):
     return "Stone Aegis Heal"

  def ability_cast(self, targets):
    # Physical damage with armor reduction
    if not targets:
        return f"{self.name}'s {self.ability} found no targets!"
        
    multiplier = 1.0 if self.level == 1 else 1.2 if self.level == 2 else 1.4
    damage = self.str * multiplier
    armor_reduction = 0.05 if self.level == 1 else 0.10 if self.level == 2 else 0.15
    
    # Apply damage and armor reduction to primary target
    actual_damage = targets[0].take_phys_damage(damage)
    
    # Apply armor reduction
    old_armor = targets[0].armor
    targets[0].armor = max(0, targets[0].armor - armor_reduction)
    
    return f"{self.name} uses {self.ability}, dealing {actual_damage:.0f} damage and reducing {targets[0].name}'s armor by {(old_armor - targets[0].armor):.0%}!"


  def level_up(self):
    print(f"{self.name} has leveled up!")
    #Level Up
    self.level += 1
    self.level_cost = (self.level_cost * 2) + (self.level_cost / 2)
    #Stat Changes
    self.str += (35 * self.level)
    self.agi += (12 * self.level)
    self.max_hp += (600 * self.level)
    self.armor += (0.03 * self.level)
    self.magic_resist = (0.03 * self.level)    


  """
     def __init__(self, name):
    self.name = name
    self.spell_power = 0
    self.str = 0
    self.agi = 0
    self.hp = 0
    self.mana = 0
    self.max_mana = 0
    self.level = 1
    self.origin = ''
    self.classes = ''
    self.items = []
    self.max_hp = 0

   """