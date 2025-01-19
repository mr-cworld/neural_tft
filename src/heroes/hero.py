from abc import ABC, abstractmethod
# Class for other herotypes to inherit from


class Hero(ABC):
  spell_power = 0
  str = 0 
  agi = 0
  hp = 0
  mana = 0
  level = 1
  
  def __init__(self, name):
    self.name = name
    self.spell_power = 0
    self.str = 0
    self.agi = 0
    self.mana = 0
    self.armor = 0.01 # WILL BE A FLOAT LIKE .35
    self.magic_resist = 0.01 # WILL BE A FLOAT like .35
    self.level = 1
    self.origin = ''
    self.classes = ''
    self.items = []
    self.max_hp = 0
    self.hp = self.max_hp
    self.max_mana = 0
    self.starting_mana = 0
    self.level_cost = 0
    self.buy_price = 0
    self.ability = self.ability_name()

  @classmethod
  def __init_subclass__(cls, **kwargs):
      super().__init_subclass__(**kwargs)
      if not hasattr(cls, 'origin'):
          raise TypeError(f"{cls.__name__} must define the class attribute 'architype'")

  def level_up(self):
    self.level += 1
  
  def add_item(self, item):
    self.items.append(item)
  
  def remove_item(self, item):
    self.items.remove(item)

  def check_cast(self):
    if self.mana >= self.max_mana:
      self.ability_cast()
      self.mana = 0
  
  def attack(self):
    self.mana += 1
    self.check_cast()
    return (self.str * 2) + self.agi

  def take_phys_damage(self, damage):
    hit = damage * (1 - self.armor)
    self.hp -= hit
    self.mana += 1
    self.check_cast()
  
  def take_magic_damage(self, damage):
    hit = damage * (1 - self.magic_resist)
    self.hp -= hit

  @abstractmethod
  def ability_cast(self):
    # Placeholder for ability cast method
    pass

  @abstractmethod
  def level_up(self):
    # Placeholder for level up method
    pass

  @abstractmethod
  def ability_name(self):
    # Placeholder for ability name method
    pass

  #Battle Prep Commands

  def reset_hero(self):
    self.hp = self.max_hp
    self.mana = self.starting_mana
