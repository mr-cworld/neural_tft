from heroes.hero import Hero

class Airstorm(Hero):
    origin = 'Wind'
    
    def __init__(self, name):
        super().__init__(name)
        self.name = 'Airstorm'
        # Stats - Balanced with good spell power
        self.str = 35
        self.agi = 45
        self.spell_power = 65
        self.max_hp = 600
        self.hp = self.max_hp
        self.armor = 0.25
        self.magic_resist = 0.25     
        # Mana
        self.mana = 0
        self.max_mana = 7
        self.starting_mana = 0
        # Core Stats
        self.origin = 'Wind'
        self.classes = 'Support'
        self.ability = self.ability_name()
        self.level_cost = 8
        self.buy_price = 3  # 3-cost unit

    def ability_name(self):
        return "Soothing Breeze"

    def ability_cast(self):
        # Healing with bonus AGI grant
        base_heal = self.spell_power * 1.2
        agi_bonus = 2 if self.level == 1 else 4 if self.level == 2 else 6
        low_hp_heal = self.spell_power * (1.5 if self.level == 1 else 1.75 if self.level == 2 else 2.0)
        return f"{self.name} uses {self.ability}, healing ally for {base_heal:.0f} (or {low_hp_heal:.0f} if below 50% HP) and granting {agi_bonus} AGI!"

    def level_up(self):
        print(f"{self.name} has leveled up!")
        self.level += 1
        self.level_cost = (self.level_cost * 2) + (self.level_cost / 2)
        # Stat Changes
        self.str += (30 * self.level)
        self.agi += (40 * self.level)
        self.spell_power += (55 * self.level)
        self.max_hp += (500 * self.level)
        self.armor += (0.02 * self.level)
        self.magic_resist += (0.02 * self.level) 