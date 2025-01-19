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

    def ability_cast(self):
        # Deals physical damage based on str + 0.5 * agi and reduces armor
        damage = self.str + (0.5 * self.agi)
        armor_reduction = 0.02 if self.level == 1 else 0.05 if self.level == 2 else 0.08
        return f"{self.name} uses {self.ability}, dealing {damage} physical damage and reducing armor by {armor_reduction:.0%}!"

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