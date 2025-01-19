from heroes.hero import Hero

class Clayden(Hero):
    origin = 'Earth'
    
    def __init__(self, name):
        super().__init__(name)
        self.name = 'Clayden'
        # Stats - High spell power, low defensive stats
        self.str = 30
        self.agi = 30
        self.spell_power = 80
        self.max_hp = 600
        self.hp = self.max_hp
        self.armor = 0.20
        self.magic_resist = 0.20     
        # Mana
        self.mana = 0
        self.max_mana = 9
        self.starting_mana = 0
        # Core Stats
        self.origin = 'Earth'
        self.classes = 'Mage'
        self.ability = self.ability_name()
        self.level_cost = 9
        self.buy_price = 4  # 4-cost powerful unit

    def ability_name(self):
        return "Rockslide"

    def ability_cast(self):
        # High magic damage to 3 targets
        damage = self.spell_power * 2
        return f"{self.name} uses {self.ability}, dealing {damage} magic damage to 3 random targets!"

    def level_up(self):
        print(f"{self.name} has leveled up!")
        self.level += 1
        self.level_cost = (self.level_cost * 2) + (self.level_cost / 2)
        # Stat Changes - Focus on spell power scaling
        self.str += (20 * self.level)
        self.agi += (20 * self.level)
        self.spell_power += (70 * self.level)
        self.max_hp += (500 * self.level)
        self.armor += (0.01 * self.level)
        self.magic_resist += (0.01 * self.level) 