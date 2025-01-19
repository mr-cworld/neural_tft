from heroes.hero import Hero
import random

class Charion(Hero):
    origin = 'Fire'
    
    def __init__(self, name):
        super().__init__(name)
        self.name = 'Charion'
        # Stats - Strong bruiser with spell scaling
        self.str = 60
        self.agi = 40
        self.spell_power = 45
        self.max_hp = 800
        self.hp = self.max_hp
        self.armor = 0.30
        self.magic_resist = 0.30     
        # Mana
        self.mana = 0
        self.max_mana = 8
        self.starting_mana = 0
        # Core Stats
        self.origin = 'Fire'
        self.classes = 'Bruiser'
        self.ability = self.ability_name()
        self.level_cost = 9
        self.buy_price = 4  # 4-cost unit

    def ability_name(self):
        return "Eruption Slam"

    def ability_cast(self, targets):
        # Multiple casts when low HP
        if not targets:
            return f"{self.name}'s {self.ability} found no targets!"
        
        # Base damage scales with str and spell power
        base_damage = self.str + (0.5 * self.spell_power)
        multiplier = 1.0 if self.level == 1 else 1.2 if self.level == 2 else 1.4
        damage = base_damage * multiplier
        
        # Number of casts increases when below 50% HP
        num_casts = 1
        if self.hp < (self.max_hp * 0.5):
            num_casts = 1 if self.level == 1 else 2 if self.level == 2 else 3
        
        # Hit up to 3 random targets per cast
        total_damage = 0
        hits_per_cast = min(len(targets), 3)
        
        for _ in range(num_casts):
            random_targets = random.sample(targets, hits_per_cast)
            for target in random_targets:
                actual_damage = target.take_physical_damage(damage)
                total_damage += actual_damage
        
        return f"{self.name} uses {self.ability}, casting {num_casts} times and dealing {total_damage:.0f} total damage to {hits_per_cast} targets per cast!"

    def level_up(self):
        print(f"{self.name} has leveled up!")
        self.level += 1
        self.level_cost = (self.level_cost * 2) + (self.level_cost / 2)
        # Stat Changes
        self.str += (50 * self.level)
        self.agi += (35 * self.level)
        self.spell_power += (40 * self.level)
        self.max_hp += (700 * self.level)
        self.armor += (0.02 * self.level)
        self.magic_resist += (0.02 * self.level) 