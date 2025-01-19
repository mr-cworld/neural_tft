from heroes.hero import Hero

class Crepus(Hero):
    origin = 'Dark'
    
    def __init__(self, name):
        super().__init__(name)
        self.name = 'Crepus'
        # Stats - High agi ranger
        self.str = 35
        self.agi = 70
        self.max_hp = 550
        self.hp = self.max_hp
        self.armor = 0.20
        self.magic_resist = 0.20     
        # Mana
        self.mana = 0
        self.max_mana = 7
        self.starting_mana = 0
        # Core Stats
        self.origin = 'Dark'
        self.classes = 'Ranger'
        self.ability = self.ability_name()
        self.level_cost = 7
        self.buy_price = 2  # 2-cost unit

    def ability_name(self):
        return "Twilight Arrow"

    def ability_cast(self, targets):
        # Physical damage based on agi and target's magic resist
        if not targets:
            return f"{self.name}'s {self.ability} found no targets!"
        
        multiplier = 1.2 if self.level == 1 else 1.5 if self.level == 2 else 1.8
        base_damage = self.agi * multiplier
        mr_bonus = targets[0].magic_resist * 0.3  # 30% of target's MR as bonus damage
        
        actual_damage = targets[0].take_physical_damage(base_damage + (base_damage * mr_bonus))
        
        # Gain AGI on kill
        agi_gain = 2 if self.level == 1 else 4 if self.level == 2 else 6
        if not targets[0].is_alive():
            self.agi += agi_gain
            return f"{self.name} uses {self.ability}, dealing {actual_damage:.0f} damage and gaining {agi_gain} AGI from the kill!"
        
        return f"{self.name} uses {self.ability}, dealing {actual_damage:.0f} damage to {targets[0].name}!"

    def level_up(self):
        print(f"{self.name} has leveled up!")
        self.level += 1
        self.level_cost = (self.level_cost * 2) + (self.level_cost / 2)
        # Stat Changes
        self.str += (30 * self.level)
        self.agi += (60 * self.level)
        self.max_hp += (450 * self.level)
        self.armor += (0.02 * self.level)
        self.magic_resist += (0.02 * self.level) 