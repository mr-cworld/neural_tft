from heroes.hero import Hero

class Solwyn(Hero):
    origin = 'Light'
    
    def __init__(self, name):
        super().__init__(name)
        self.name = 'Solwyn'
        # Stats - Strong fighter with utility
        self.str = 60
        self.agi = 45
        self.max_hp = 700
        self.hp = self.max_hp
        self.armor = 0.30
        self.magic_resist = 0.30     
        # Mana
        self.mana = 0
        self.max_mana = 8
        self.starting_mana = 0
        # Core Stats
        self.origin = 'Light'
        self.classes = 'Fighter'
        self.ability = self.ability_name()
        self.level_cost = 9
        self.buy_price = 4  # 4-cost unit

    def ability_name(self):
        return "Blinding Slash"

    def ability_cast(self, targets):
        # Damage and conditional damage reduction
        if not targets:
            return f"{self.name}'s {self.ability} found no targets!"
        
        multiplier = 1.3 if self.level == 1 else 1.5 if self.level == 2 else 1.8
        damage = self.str * multiplier
        damage_reduction = 0.05 if self.level == 1 else 0.07 if self.level == 2 else 0.10
        
        # Deal damage to primary target
        actual_damage = targets[0].take_physical_damage(damage)
        
        # Apply damage reduction debuff if target is above 50% HP
        if targets[0].hp > (targets[0].max_hp * 0.5):
            # Store original str for reduction
            old_str = targets[0].str
            targets[0].str = int(targets[0].str * (1 - damage_reduction))
            str_reduction = old_str - targets[0].str
            return f"{self.name} uses {self.ability}, dealing {actual_damage:.0f} damage and reducing {targets[0].name}'s strength by {str_reduction}!"
        
        return f"{self.name} uses {self.ability}, dealing {actual_damage:.0f} damage to {targets[0].name}!"

    def level_up(self):
        print(f"{self.name} has leveled up!")
        self.level += 1
        self.level_cost = (self.level_cost * 2) + (self.level_cost / 2)
        # Stat Changes
        self.str += (50 * self.level)
        self.agi += (35 * self.level)
        self.max_hp += (600 * self.level)
        self.armor += (0.02 * self.level)
        self.magic_resist += (0.02 * self.level) 