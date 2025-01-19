from heroes.hero import Hero

class Zephon(Hero):
    origin = 'Wind'
    
    def __init__(self, name):
        super().__init__(name)
        self.name = 'Zephon'
        # Stats - Lower HP but high armor/resist as mentioned
        self.str = 25
        self.agi = 35  # Higher AGI for Wind unit
        self.max_hp = 450  # Lower HP as specified
        self.hp = self.max_hp
        self.armor = 0.40  # High armor
        self.magic_resist = 0.45  # Unusually high magic resist     
        # Mana
        self.mana = 0
        self.max_mana = 6
        self.starting_mana = 0
        # Core Stats
        self.origin = 'Wind'
        self.classes = 'Tank'
        self.ability = self.ability_name()
        self.level_cost = 6
        self.buy_price = 1  # 1-cost unit

    def ability_name(self):
        return "Cyclone Guard"

    def ability_cast(self):
        # Heals for 2% max hp and does 5% agi as wind damage to 3 random units
        heal_amount = self.max_hp * 0.02
        damage = self.agi * 0.05
        self.hp = min(self.max_hp, self.hp + heal_amount)
        return f"{self.name} uses {self.ability}, healing for {heal_amount:.0f} HP and dealing {damage:.0f} damage to 3 random units!"

    def level_up(self):
        print(f"{self.name} has leveled up!")
        self.level += 1
        self.level_cost = (self.level_cost * 2) + (self.level_cost / 2)
        # Stat Changes
        self.str += (20 * self.level)
        self.agi += (30 * self.level)
        self.max_hp += (400 * self.level)
        self.armor += (0.03 * self.level)
        self.magic_resist += (0.03 * self.level) 