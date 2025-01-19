from heroes.hero import Hero

class Craig(Hero):
    origin = 'Earth'
    
    def __init__(self, name):
        super().__init__(name)
        self.name = 'Craig'
        # Stats
        self.str = 40
        self.agi = 15
        self.max_hp = 600
        self.hp = self.max_hp
        self.armor = 0.30
        self.magic_resist = 0.30     
        # Mana
        self.mana = 3
        self.max_mana = 4
        self.starting_mana = 3
        # Core Stats
        self.origin = 'Earth'
        self.classes = 'Tank'
        self.ability = self.ability_name()
        self.level_cost = 6
        self.buy_price = 1

    def ability_name(self):
        return "Quaking Shield"

    def ability_cast(self):
        # Craig's ability is to convert 5% of str into bonus Armor. Max of 80% bonus Armor
        bonus_armor = self.str * 0.05
        bonus_armor_percent = bonus_armor / 100
        self.armor += bonus_armor
        if self.armor >= 0.80:
            self.armor = 0.80
        return f"{self.name} uses {self.ability} and gains {bonus_armor} bonus Armor! Armor now at {self.armor}!"

    def level_up(self):
        print(f"{self.name} has leveled up!")
        # Level Up
        self.level += 1
        self.level_cost = (self.level_cost * 2) + (self.level_cost / 2)
        # Stat Changes
        self.str += (40 * self.level)
        self.agi += (15 * self.level)
        self.max_hp += (600 * self.level)
        self.armor += (0.01 * self.level)
        self.magic_resist += (0.03 * self.level)