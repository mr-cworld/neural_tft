from heroes.hero import Hero

class Aqua(Hero):
    origin = 'Water'
    
    def __init__(self, name):
        super().__init__(name)
        self.name = 'Aqua'
        # Stats - High spell power mage
        self.str = 35
        self.agi = 35
        self.spell_power = 75
        self.max_hp = 600
        self.hp = self.max_hp
        self.armor = 0.20
        self.magic_resist = 0.20     
        # Mana
        self.mana = 0
        self.max_mana = 7
        self.starting_mana = 0
        # Core Stats
        self.origin = 'Water'
        self.classes = 'Mage'
        self.ability = self.ability_name()
        self.level_cost = 8
        self.buy_price = 3  # 3-cost unit

    def ability_name(self):
        return "Aqua Surge"

    def ability_cast(self, targets):
        # Magic damage and team mana gain
        if not targets:
            return f"{self.name}'s {self.ability} found no targets!"
        
        multiplier = 1.2 if self.level == 1 else 1.5 if self.level == 2 else 1.8
        damage = self.spell_power * multiplier
        mana_gain = 1 if self.level == 1 else 2 if self.level == 2 else 3
        
        # Hit up to 2 random targets
        hits = min(len(targets), 2)
        total_damage = 0
        for i in range(hits):
            actual_damage = targets[i].take_magic_damage(damage)
            total_damage += actual_damage
        
        return f"{self.name} uses {self.ability}, dealing {total_damage:.0f} magic damage to {hits} enemies and granting allies +{mana_gain} mana!"

    def level_up(self):
        print(f"{self.name} has leveled up!")
        self.level += 1
        self.level_cost = (self.level_cost * 2) + (self.level_cost / 2)
        # Stat Changes
        self.str += (30 * self.level)
        self.agi += (30 * self.level)
        self.spell_power += (65 * self.level)
        self.max_hp += (500 * self.level)
        self.armor += (0.02 * self.level)
        self.magic_resist += (0.02 * self.level) 