from heroes.hero import Hero

class Brinesh(Hero):
    origin = 'Water'
    
    def __init__(self, name):
        super().__init__(name)
        self.name = 'Brinesh'
        # Stats - Tanky with good str
        self.str = 45
        self.agi = 30
        self.max_hp = 750
        self.hp = self.max_hp
        self.armor = 0.35
        self.magic_resist = 0.35     
        # Mana
        self.mana = 0
        self.max_mana = 6
        self.starting_mana = 0
        # Core Stats
        self.origin = 'Water'
        self.classes = 'Tank'
        self.ability = self.ability_name()
        self.level_cost = 6
        self.buy_price = 2  # 2-cost unit

    def ability_name(self):
        return "Tidal Ward"

    def ability_cast(self, targets):
        # Damage and team mana gain on being hit
        if not targets:
            return f"{self.name}'s {self.ability} found no targets!"
        
        damage = self.str * 1.2
        mana_gain = 1 if self.level == 1 else 2 if self.level == 2 else 3
        
        actual_damage = targets[0].take_magic_damage(damage)
        
        # Apply mana gain buff (will be checked when taking damage)
        self.mana_on_hit = mana_gain
        self.mana_on_hit_duration = 3
        
        return f"{self.name} uses {self.ability}, dealing {actual_damage:.0f} damage and granting allies +{mana_gain} mana when hit for 3s!"

    def level_up(self):
        print(f"{self.name} has leveled up!")
        self.level += 1
        self.level_cost = (self.level_cost * 2) + (self.level_cost / 2)
        # Stat Changes
        self.str += (40 * self.level)
        self.agi += (25 * self.level)
        self.max_hp += (650 * self.level)
        self.armor += (0.03 * self.level)
        self.magic_resist += (0.03 * self.level) 