from heroes.hero import Hero

class Zephon(Hero):
    origin = 'Wind'
    
    def __init__(self, name):
        super().__init__(name)
        self.name = 'Zephon'
        # Stats - Lower HP but high armor/resist as mentioned
        self.str = 25
        self.agi = 35  # Higher AGI for Wind unit
        self.max_hp = 450  # Lower HP as specified
        self.hp = self.max_hp
        self.armor = 0.40  # High armor
        self.magic_resist = 0.45  # Unusually high magic resist     
        # Mana
        self.mana = 0
        self.max_mana = 6
        self.starting_mana = 0
        # Core Stats
        self.origin = 'Wind'
        self.classes = 'Tank'
        self.ability = self.ability_name()
        self.level_cost = 6
        self.buy_price = 1  # 1-cost unit

    def ability_name(self):
        return "Cyclone Guard"

    def ability_cast(self, targets):
        # Heals self and deals wind damage to random targets
        if not targets:
            return f"{self.name}'s {self.ability} found no targets!"
        
        # Heal scaling with level
        heal_percent = 0.02 if self.level == 1 else 0.03 if self.level == 2 else 0.04
        heal_amount = self.max_hp * heal_percent
        self.hp = min(self.max_hp, self.hp + heal_amount)
        
        # Damage scaling with level
        damage_percent = 0.05 if self.level == 1 else 0.07 if self.level == 2 else 0.09
        base_damage = self.agi * damage_percent
        
        # Hit up to 3 random targets
        import random
        hits = min(len(targets), 3)
        random_targets = random.sample(targets, hits)
        total_damage = 0
        
        for target in random_targets:
            actual_damage = target.take_magic_damage(base_damage)
            total_damage += actual_damage
        
        return f"{self.name} uses {self.ability}, healing for {heal_amount:.0f} HP and dealing {total_damage:.0f} wind damage to {hits} random targets!"

    def level_up(self):
        print(f"{self.name} has leveled up!")
        self.level += 1
        self.level_cost = (self.level_cost * 2) + (self.level_cost / 2)
        # Stat Changes
        self.str += (20 * self.level)
        self.agi += (30 * self.level)
        self.max_hp += (400 * self.level)
        self.armor += (0.03 * self.level)
        self.magic_resist += (0.03 * self.level) 