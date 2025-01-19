from heroes.hero import Hero

class Ruphus(Hero):
    origin = 'Wind'
    
    def __init__(self, name):
        super().__init__(name)
        self.name = 'Ruphus'
        # Stats - High agi for Wind fighter
        self.str = 40
        self.agi = 55
        self.max_hp = 600
        self.hp = self.max_hp
        self.armor = 0.25
        self.magic_resist = 0.25     
        # Mana
        self.mana = 0
        self.max_mana = 6
        self.starting_mana = 0
        # Core Stats
        self.origin = 'Wind'
        self.classes = 'Fighter'
        self.ability = self.ability_name()
        self.level_cost = 7
        self.buy_price = 2  # 2-cost unit

    def ability_name(self):
        return "Gust Slash"

    def ability_cast(self):
        # Multiple strikes based on agi
        num_strikes = max(2, self.agi // 100)
        damage_per_strike = self.agi * 1.25
        total_damage = damage_per_strike * num_strikes
        return f"{self.name} uses {self.ability}, striking {num_strikes} times for {total_damage:.0f} total damage to second highest HP target!"

    def level_up(self):
        print(f"{self.name} has leveled up!")
        self.level += 1
        self.level_cost = (self.level_cost * 2) + (self.level_cost / 2)
        # Stat Changes
        self.str += (35 * self.level)
        self.agi += (45 * self.level)
        self.max_hp += (500 * self.level)
        self.armor += (0.02 * self.level)
        self.magic_resist += (0.02 * self.level) 