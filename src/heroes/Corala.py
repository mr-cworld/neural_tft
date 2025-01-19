from heroes.hero import Hero
import random

class Corala(Hero):
    origin = 'Water'
    
    def __init__(self, name):
        super().__init__(name)
        self.name = 'Corala'
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
        self.origin = 'Water'
        self.classes = 'Ranger'
        self.ability = self.ability_name()
        self.level_cost = 8
        self.buy_price = 3  # 3-cost unit

    def ability_name(self):
        return "Arc Shot"

    def ability_cast(self, targets):
        # Multi-target damage with mana refund on crit
        if not targets:
            return f"{self.name}'s {self.ability} found no targets!"
        
        multiplier = 0.9 if self.level == 1 else 1.1 if self.level == 2 else 1.3
        damage = self.agi * multiplier
        mana_refund = 1 if self.level == 1 else 2 if self.level == 2 else 3
        
        hits = min(len(targets), 2)
        total_damage = 0
        crits = 0
        
        for i in range(hits):
            # 25% crit chance
            is_crit = random.random() < 0.25
            actual_damage = targets[i].take_magic_damage(damage * (1.5 if is_crit else 1.0))
            total_damage += actual_damage
            if is_crit:
                crits += 1
                self.mana += mana_refund
            
        return f"{self.name} uses {self.ability}, dealing {total_damage:.0f} damage to {hits} targets and gaining {crits * mana_refund} mana from {crits} crits!"

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