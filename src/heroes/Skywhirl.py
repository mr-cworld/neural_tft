from heroes.hero import Hero

class Skywhirl(Hero):
    origin = 'Wind'
    
    def __init__(self, name):
        super().__init__(name)
        self.name = 'Skywhirl'
        # Stats - Balanced str/agi for bruiser
        self.str = 45
        self.agi = 45
        self.max_hp = 650
        self.hp = self.max_hp
        self.armor = 0.25
        self.magic_resist = 0.25     
        # Mana
        self.mana = 0
        self.max_mana = 7
        self.starting_mana = 0
        # Core Stats
        self.origin = 'Wind'
        self.classes = 'Bruiser'
        self.ability = self.ability_name()
        self.level_cost = 7
        self.buy_price = 2  # 2-cost unit

    def ability_name(self):
        return "Whirling Leap"

    def ability_cast(self):
        # Damage based on level multiplier
        multiplier = 2 if self.level == 1 else 3 if self.level == 2 else 4
        main_damage = (self.str + self.agi) * multiplier
        splash_damage = main_damage * 0.3
        return f"{self.name} uses {self.ability}, dealing {main_damage:.0f} damage to target and {splash_damage:.0f} to 2 adjacent units!"

    def level_up(self):
        print(f"{self.name} has leveled up!")
        self.level += 1
        self.level_cost = (self.level_cost * 2) + (self.level_cost / 2)
        # Stat Changes
        self.str += (40 * self.level)
        self.agi += (40 * self.level)
        self.max_hp += (550 * self.level)
        self.armor += (0.02 * self.level)
        self.magic_resist += (0.02 * self.level) 