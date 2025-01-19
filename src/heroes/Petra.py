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

    def ability_cast(self):
        # Two rapid strikes, each dealing 120% str damage
        damage_per_hit = self.str * 1.2
        total_damage = damage_per_hit * 2
        # Gain armor bonus
        armor_gain = 0.01
        self.armor = min(0.80, self.armor + armor_gain)
        return f"{self.name} uses {self.ability}, striking twice for {total_damage} total damage and gaining {armor_gain:.0%} armor!"

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