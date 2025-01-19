from abc import ABC, abstractmethod
# Class for other herotypes to inherit from


class Hero(ABC):
  spell_power = 0
  str = 0 
  agi = 0
  hp = 0
  mana = 0
  level = 1
  ability = ''
  origin = ''
  classes = ''
  items = []

  
  
  def __init__(self, name):
    self.name = name
    self.spell_power = 0
    self.str = 0
    self.agi = 0
    self.hp = 0
    self.mana = 0
    self.level = 1
    self.origin = ''
    self.classes = ''
    self.items = []

  @classmethod
  def __init_subclass__(cls, **kwargs):
      super().__init_subclass__(**kwargs)
      if not hasattr(cls, 'architype'):
          raise TypeError(f"{cls.__name__} must define the class attribute 'architype'")


  def level_up(self):
    self.level += 1
  
  @abstractmethod
  def attack(self):
    # Placeholder for attack method
    pass
   
  @abstractmethod 
  def cast_spell(self):
    # Placeholder for cast spell method
    pass

  @abstractmethod
  def ability_cast(self):
    # Placeholder for ability cast method
    pass

  @abstractmethod
  def level_up(self):
    # Placeholder for level up method
    pass