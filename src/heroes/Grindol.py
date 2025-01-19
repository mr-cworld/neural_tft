from heroes.hero import Hero

class Grindol(Hero):
    origin = 'Earth'
    
    def __init__(self, name):
        super().__init__(name)
        self.name = 'Grindol'
        # Stats - High agi, moderate str
        self.str = 35
        self.agi = 60
        self.max_hp = 550
        self.hp = self.max_hp
        self.armor = 0.20
        self.magic_resist = 0.20     
        # Mana
        self.mana = 0
        self.max_mana = 7
        self.starting_mana = 0
        # Core Stats
        self.origin = 'Earth'
        self.classes = 'Ranger'
        self.ability = self.ability_name()
        self.level_cost = 6
        self.buy_price = 2  # 2-cost unit

    def ability_name(self):
        return "Crystalline Arrow"

    def ability_cast(self):
        # Damage based on both str and agi
        damage = (1.2 * self.str) + (1.5 * self.agi)
        return f"{self.name} uses {self.ability}, firing an arrow that deals {damage} physical damage and ricochets!"

    def level_up(self):
        print(f"{self.name} has leveled up!")
        self.level += 1
        self.level_cost = (self.level_cost * 2) + (self.level_cost / 2)
        # Stat Changes
        self.str += (25 * self.level)
        self.agi += (50 * self.level)
        self.max_hp += (450 * self.level)
        self.armor += (0.02 * self.level)
        self.magic_resist += (0.02 * self.level) 