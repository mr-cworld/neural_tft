from heroes.hero import Hero

class Flint(Hero):
    origin = 'Earth'
    
    def __init__(self, name):
        super().__init__(name)
        self.name = 'Flint'
        # Stats - Strong str/hp for bruiser, moderate agi
        self.str = 55
        self.agi = 25
        self.max_hp = 750
        self.hp = self.max_hp
        self.armor = 0.25
        self.magic_resist = 0.25     
        # Mana
        self.mana = 0
        self.max_mana = 8
        self.starting_mana = 0
        # Core Stats
        self.origin = 'Earth'
        self.classes = 'Bruiser'
        self.ability = self.ability_name()
        self.level_cost = 6
        self.buy_price = 2  # 2-cost unit

    def ability_name(self):
        return "Shatterstrike"

    def ability_cast(self, targets):
        # Physical damage and armor reduction
        if not targets:
            return f"{self.name}'s {self.ability} found no targets!"
        
        damage = self.str + (0.5 * self.agi)
        armor_reduction = 0.02 if self.level == 1 else 0.05 if self.level == 2 else 0.08
        
        actual_damage = targets[0].take_physical_damage(damage)
        
        # Apply armor reduction
        old_armor = targets[0].armor
        targets[0].armor = max(0, targets[0].armor - armor_reduction)
        
        return f"{self.name} uses {self.ability}, dealing {actual_damage:.0f} damage and reducing {targets[0].name}'s armor by {(old_armor - targets[0].armor):.0%}!"

    def level_up(self):
        print(f"{self.name} has leveled up!")
        self.level += 1
        self.level_cost = (self.level_cost * 2) + (self.level_cost / 2)
        # Stat Changes
        self.str += (45 * self.level)
        self.agi += (20 * self.level)
        self.max_hp += (650 * self.level)
        self.armor += (0.02 * self.level)
        self.magic_resist += (0.02 * self.level) 