from heroes.hero import Hero

class Tempia(Hero):
    origin = 'Wind'
    
    def __init__(self, name):
        super().__init__(name)
        self.name = 'Tempia'
        # Stats - Lower base agi but high scaling
        self.str = 35
        self.agi = 50  # Lower base AGI as specified
        self.max_hp = 600
        self.hp = self.max_hp
        self.armor = 0.20
        self.magic_resist = 0.20     
        # Mana - High cost as specified
        self.mana = 2
        self.max_mana = 9
        self.starting_mana = 2
        # Core Stats
        self.origin = 'Wind'
        self.classes = 'Ranger'
        self.ability = self.ability_name()
        self.level_cost = 9
        self.buy_price = 4  # 4-cost unit

    def ability_name(self):
        return "Hurricane Arrow"

    def ability_cast(self, targets):
        # Single powerful shot with level scaling
        if not targets:
            return f"{self.name}'s {self.ability} found no targets!"
        
        # High scaling with AGI
        multiplier = 1.4 if self.level == 1 else 1.8 if self.level == 2 else 2.3
        damage = self.agi * multiplier
        
        # Find highest AGI target (prioritizes enemy rangers/assassins)
        target = max(targets, key=lambda x: x.agi)
        actual_damage = target.take_physical_damage(damage)
        
        # Bonus damage if target has high AGI
        if target.agi > 50:
            bonus_damage = target.take_physical_damage(damage * 0.25)  # 25% bonus damage
            actual_damage += bonus_damage
            return f"{self.name} uses {self.ability}, dealing {actual_damage:.0f} damage to high-AGI target {target.name}!"
        
        return f"{self.name} uses {self.ability}, dealing {actual_damage:.0f} damage to {target.name}!"

    def level_up(self):
        print(f"{self.name} has leveled up!")
        self.level += 1
        self.level_cost = (self.level_cost * 2) + (self.level_cost / 2)
        # Stat Changes - Very high agi scaling
        self.str += (30 * self.level)
        self.agi += (65 * self.level)
        self.max_hp += (500 * self.level)
        self.armor += (0.02 * self.level)
        self.magic_resist += (0.02 * self.level) 