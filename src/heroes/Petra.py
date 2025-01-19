from heroes.hero import Hero

class Petra(Hero):
    origin = 'Earth'
    
    def __init__(self, name):
        super().__init__(name)
        self.name = 'Petra'
        # Stats - High str and agi for a fighter
        self.str = 65
        self.agi = 45
        self.max_hp = 850
        self.hp = self.max_hp
        self.armor = 0.30
        self.magic_resist = 0.25     
        # Mana
        self.mana = 0
        self.max_mana = 6
        self.starting_mana = 0
        # Core Stats
        self.origin = 'Earth'
        self.classes = 'Fighter'
        self.ability = self.ability_name()
        self.level_cost = 8
        self.buy_price = 3  # 3-cost powerful unit

    def ability_name(self):
        return "Earthen Flurry"

    def ability_cast(self, targets):
        # Two rapid strikes with armor gain
        if not targets:
            return f"{self.name}'s {self.ability} found no targets!"
        
        damage_per_hit = self.str * (0.8 if self.level == 1 else 0.9 if self.level == 2 else 1.0)
        armor_gain = 0.01 if self.level == 1 else 0.02 if self.level == 2 else 0.03
        
        total_damage = 0
        # Two hits on primary target
        for _ in range(2):
            actual_damage = targets[0].take_physical_damage(damage_per_hit)
            total_damage += actual_damage
        
        # Gain armor bonus
        old_armor = self.armor
        self.armor = min(0.80, self.armor + armor_gain)
        
        return f"{self.name} uses {self.ability}, dealing {total_damage:.0f} total damage and gaining {(self.armor - old_armor):.0%} armor!"

    def level_up(self):
        print(f"{self.name} has leveled up!")
        self.level += 1
        self.level_cost = (self.level_cost * 2) + (self.level_cost / 2)
        # Stat Changes - Strong scaling
        self.str += (55 * self.level)
        self.agi += (40 * self.level)
        self.max_hp += (700 * self.level)
        self.armor += (0.02 * self.level)
        self.magic_resist += (0.02 * self.level) 