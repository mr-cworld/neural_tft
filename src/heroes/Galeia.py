from heroes.hero import Hero

class Galeia(Hero):
    origin = 'Wind'
    
    def __init__(self, name):
        super().__init__(name)
        self.name = 'Galeia'
        # Stats - High spell power focus
        self.str = 30
        self.agi = 40
        self.spell_power = 75
        self.max_hp = 550
        self.hp = self.max_hp
        self.armor = 0.20
        self.magic_resist = 0.20     
        # Mana
        self.mana = 0
        self.max_mana = 8
        self.starting_mana = 0
        # Core Stats
        self.origin = 'Wind'
        self.classes = 'Mage'
        self.ability = self.ability_name()
        self.level_cost = 8
        self.buy_price = 3  # 3-cost unit

    def ability_name(self):
        return "Wind Shear"

    def ability_cast(self):
        # Magic damage to top 2 HP targets
        multiplier = 1.3 if self.level == 1 else 1.5 if self.level == 2 else 1.8
        damage = self.spell_power * multiplier
        return f"{self.name} uses {self.ability}, dealing {damage:.0f} magic damage to the 2 highest HP enemies!"

    def level_up(self):
        print(f"{self.name} has leveled up!")
        self.level += 1
        self.level_cost = (self.level_cost * 2) + (self.level_cost / 2)
        # Stat Changes
        self.str += (25 * self.level)
        self.agi += (35 * self.level)
        self.spell_power += (65 * self.level)
        self.max_hp += (450 * self.level)
        self.armor += (0.02 * self.level)
        self.magic_resist += (0.02 * self.level) 