from heroes.hero import Hero

class Umbra(Hero):
    origin = 'Dark'
    
    def __init__(self, name):
        super().__init__(name)
        self.name = 'Umbra'
        # Stats - Strong bruiser with good defenses
        self.str = 55
        self.agi = 40
        self.max_hp = 750
        self.hp = self.max_hp
        self.armor = 0.30
        self.magic_resist = 0.30     
        # Mana
        self.mana = 0
        self.max_mana = 7
        self.starting_mana = 0
        # Core Stats
        self.origin = 'Dark'
        self.classes = 'Bruiser'
        self.ability = self.ability_name()
        self.level_cost = 8
        self.buy_price = 3  # 3-cost unit

    def ability_name(self):
        return "Nightfall Cleave"

    def ability_cast(self, targets):
        # Damage based on str and target's armor with heal on kill
        if not targets:
            return f"{self.name}'s {self.ability} found no targets!"
        
        multiplier = 1.0 if self.level == 1 else 1.3 if self.level == 2 else 1.6
        base_damage = self.str * multiplier
        
        # Add bonus damage based on target's armor
        armor_bonus = targets[0].armor * 0.2  # 20% of target's armor as bonus damage
        total_damage = base_damage + (base_damage * armor_bonus)
        
        # Deal damage to primary target
        actual_damage = targets[0].take_physical_damage(total_damage)
        
        # Heal on kill
        heal_percent = 0.02 if self.level == 1 else 0.03 if self.level == 2 else 0.04
        if not targets[0].is_alive():
            heal_amount = self.max_hp * heal_percent
            self.hp = min(self.max_hp, self.hp + heal_amount)
            return f"{self.name} uses {self.ability}, dealing {actual_damage:.0f} damage and healing for {heal_amount:.0f} from the kill!"
        
        return f"{self.name} uses {self.ability}, dealing {actual_damage:.0f} damage to {targets[0].name}!"

    def level_up(self):
        print(f"{self.name} has leveled up!")
        self.level += 1
        self.level_cost = (self.level_cost * 2) + (self.level_cost / 2)
        # Stat Changes
        self.str += (45 * self.level)
        self.agi += (35 * self.level)
        self.max_hp += (650 * self.level)
        self.armor += (0.02 * self.level)
        self.magic_resist += (0.02 * self.level) 