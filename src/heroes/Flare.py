from heroes.hero import Hero

class Flare(Hero):
    origin = 'Fire'
    
    def __init__(self, name):
        super().__init__(name)
        self.name = 'Flare'
        # Stats - High str, moderate agi for early fighter
        self.str = 45
        self.agi = 35
        self.max_hp = 550
        self.hp = self.max_hp
        self.armor = 0.25
        self.magic_resist = 0.20     
        # Mana
        self.mana = 0
        self.max_mana = 6
        self.starting_mana = 0
        # Core Stats
        self.origin = 'Fire'
        self.classes = 'Fighter'
        self.ability = self.ability_name()
        self.level_cost = 6
        self.buy_price = 1  # 1-cost unit

    def ability_name(self):
        return "Blazing Strike"

    def ability_cast(self, targets):
        # Deals bonus damage to low HP targets
        if not targets:
            return f"{self.name}'s {self.ability} found no targets!"
        
        base_damage = self.str * 1.5
        bonus_multiplier = 1.5 if self.level == 1 else 1.6 if self.level == 2 else 1.75
        
        target = targets[0]  # Get first target
        damage = base_damage
        if target.hp < (target.max_hp * 0.5):  # Below 50% HP
            damage *= bonus_multiplier
        
        actual_damage = target.take_magic_damage(damage)
        return f"{self.name} uses {self.ability}, dealing {actual_damage:.0f} damage to {target.name}!"

    def level_up(self):
        print(f"{self.name} has leveled up!")
        self.level += 1
        self.level_cost = (self.level_cost * 2) + (self.level_cost / 2)
        # Stat Changes
        self.str += (40 * self.level)
        self.agi += (30 * self.level)
        self.max_hp += (450 * self.level)
        self.armor += (0.02 * self.level)
        self.magic_resist += (0.02 * self.level) 