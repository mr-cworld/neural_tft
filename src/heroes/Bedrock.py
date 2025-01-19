from heroes.hero import Hero

class Bedrock(Hero):
    origin = 'Earth'
    
    def __init__(self, name):
        super().__init__(name)
        self.name = 'Bedrock'
        # Stats - Balanced stats with high spell power
        self.str = 45
        self.agi = 35
        self.spell_power = 70
        self.max_hp = 900
        self.hp = self.max_hp
        self.armor = 0.35
        self.magic_resist = 0.35     
        # Mana
        self.mana = 0
        self.max_mana = 8
        self.starting_mana = 0
        # Core Stats
        self.origin = 'Earth'
        self.classes = 'Support'
        self.ability = self.ability_name()
        self.level_cost = 10
        self.buy_price = 5  # 5-cost legendary unit

    def ability_name(self):
        return "Geo-Fortify"

    def ability_cast(self):
        # Grants shield and stat boost
        shield = self.spell_power * 2
        stat_boost = 1 if self.level == 1 else 2 if self.level == 2 else 3
        return f"{self.name} uses {self.ability}, granting {shield} HP shield and {stat_boost} bonus to highest stat!"

    def level_up(self):
        print(f"{self.name} has leveled up!")
        self.level += 1
        self.level_cost = (self.level_cost * 2) + (self.level_cost / 2)
        # Stat Changes - Strong scaling for legendary unit
        self.str += (40 * self.level)
        self.agi += (30 * self.level)
        self.spell_power += (60 * self.level)
        self.max_hp += (800 * self.level)
        self.armor += (0.03 * self.level)
        self.magic_resist += (0.03 * self.level) 