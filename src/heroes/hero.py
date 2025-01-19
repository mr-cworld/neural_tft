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
          raise TypeError(f"{cls.__name__} must define the class attribute 'origin'")

  def level_up(self):
    self.level += 1
  
  def add_item(self, item):
    self.items.append(item)
  
  def remove_item(self, item):
    self.items.remove(item)

  def attack(self):
    base_damage = (self.str * 2) + self.agi
    self.mana += 1
    return base_damage

  def take_phys_damage(self, damage):
    mitigated_damage = damage * (1 - self.armor)
    actual_damage = min(self.hp, mitigated_damage)
    self.hp -= actual_damage
    self.mana += 1
    return actual_damage
  
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

  def is_alive(self) -> bool:
    """Check if the hero is still alive"""
    return self.hp > 0

  def find_target(self, enemy_player):
    """Find a target on the enemy's board based on class priority.
    Args:
        enemy_player: The enemy player object containing their board/heroes
    Returns:
        Hero: The target hero, or None if no valid target found
    """
    target_priority = ['Tank', 'Bruiser', 'Fighter', 'Support', 'Mage']
    
    # Assume enemy_player has a property like 'board' or 'heroes' containing live heroes
    alive_enemies = [hero for hero in enemy_player.heroes if hero.is_alive()]
    
    if not alive_enemies:
      return None
      
    # Check each class in priority order
    for target_class in target_priority:
      possible_targets = [hero for hero in alive_enemies if target_class in hero.classes]
      if possible_targets:
        return possible_targets[0]  # Return first hero of that class found
    
    # If no priority target found, return first alive enemy
    return alive_enemies[0]
