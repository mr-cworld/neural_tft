from heroes.hero import Hero
import random

class Ashira(Hero):
    origin = 'Fire'
    
    def __init__(self, name):
        super().__init__(name)
        self.name = 'Ashira'
        # Stats - Powerful mage with high spell power
        self.str = 35
        self.agi = 35
        self.spell_power = 85
        self.max_hp = 650
        self.hp = self.max_hp
        self.armor = 0.20
        self.magic_resist = 0.20     
        # Mana
        self.mana = 0
        self.max_mana = 9
        self.starting_mana = 0
        # Core Stats
        self.origin = 'Fire'
        self.classes = 'Mage'
        self.ability = self.ability_name()
        self.level_cost = 10
        self.buy_price = 5  # 5-cost legendary unit

    def ability_name(self):
        return "Inferno Burst"

    def ability_cast(self, targets):
        # High AOE damage with max HP burn
        if not targets:
            return f"{self.name}'s {self.ability} found no targets!"
        
        base_damage = self.spell_power * 1.8
        burn_percent = 0.03 if self.level == 1 else 0.05 if self.level == 2 else 0.08
        
        # Hit 1-4 random targets
        hits = min(len(targets), random.randint(1, 4))
        total_damage = 0
        for i in range(hits):
            actual_damage = targets[i].take_magic_damage(base_damage)
            burn_damage = targets[i].max_hp * burn_percent
            actual_burn = targets[i].take_magic_damage(burn_damage)
            total_damage += (actual_damage + actual_burn)
        
        return f"{self.name} uses {self.ability}, dealing {total_damage:.0f} total damage to {hits} targets!"

    def level_up(self):
        print(f"{self.name} has leveled up!")
        self.level += 1
        self.level_cost = (self.level_cost * 2) + (self.level_cost / 2)
        # Stat Changes - Strong spell power scaling
        self.str += (30 * self.level)
        self.agi += (30 * self.level)
        self.spell_power += (75 * self.level)
        self.max_hp += (550 * self.level)
        self.armor += (0.02 * self.level)
        self.magic_resist += (0.02 * self.level) 