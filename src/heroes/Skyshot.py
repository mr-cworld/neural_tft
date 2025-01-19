from heroes.hero import Hero

class Skyshot(Hero):
    origin = 'Wind'
    
    def __init__(self, name):
        super().__init__(name)
        self.name = 'Skyshot'
        # Stats - Very high agi focus
        self.str = 30
        self.agi = 70
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
        self.classes = 'Ranger'
        self.ability = self.ability_name()
        self.level_cost = 8
        self.buy_price = 3  # 3-cost unit

    def ability_name(self):
        return "Feathered Volley"

    def ability_cast(self):
        # Multiple arrows with crit chance
        num_arrows = max(1, (self.agi // 69) + 1)
        base_damage = self.agi * 0.75
        crit_chance = 0.20 if self.level == 1 else 0.23 if self.level == 2 else 0.28
        crit_multi = 1.2 if self.level == 1 else 1.4 if self.level == 2 else 1.6
        return f"{self.name} uses {self.ability}, firing {num_arrows} arrows for {base_damage:.0f} damage each with {crit_chance:.0%} chance to deal {crit_multi}x damage!"

    def level_up(self):
        print(f"{self.name} has leveled up!")
        self.level += 1
        self.level_cost = (self.level_cost * 2) + (self.level_cost / 2)
        # Stat Changes - Heavy agi scaling
        self.str += (25 * self.level)
        self.agi += (60 * self.level)
        self.max_hp += (450 * self.level)
        self.armor += (0.02 * self.level)
        self.magic_resist += (0.02 * self.level) 