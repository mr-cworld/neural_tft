from heroes.hero import Hero

class Ignira(Hero):
    origin = 'Fire'
    
    def __init__(self, name):
        super().__init__(name)
        self.name = 'Ignira'
        # Stats - Support with good spell power
        self.str = 30
        self.agi = 35
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
        self.origin = 'Fire'
        self.classes = 'Support'
        self.ability = self.ability_name()
        self.level_cost = 8
        self.buy_price = 3  # 3-cost unit

    def ability_name(self):
        return "Cinder Ward"

    def ability_cast(self, targets):
        # Shield ally and burn enemies
        if not targets:
            return f"{self.name}'s {self.ability} found no targets!"
        
        shield_amount = self.spell_power
        burn_percent = 0.01 if self.level == 1 else 0.03 if self.level == 2 else 0.06
        
        # Apply shield to self
        self.hp = min(self.max_hp, self.hp + shield_amount)
        
        # Apply burn damage to up to 2 targets
        hits = min(len(targets), 2)
        total_damage = 0
        
        for i in range(hits):
            burn_damage = targets[i].max_hp * burn_percent
            actual_damage = targets[i].take_magic_damage(burn_damage)
            total_damage += actual_damage
        
        return f"{self.name} uses {self.ability}, gaining {shield_amount:.0f} shield and dealing {total_damage:.0f} burn damage to {hits} enemies!"

    def level_up(self):
        print(f"{self.name} has leveled up!")
        self.level += 1
        self.level_cost = (self.level_cost * 2) + (self.level_cost / 2)
        # Stat Changes
        self.str += (25 * self.level)
        self.agi += (30 * self.level)
        self.spell_power += (55 * self.level)
        self.max_hp += (500 * self.level)
        self.armor += (0.02 * self.level)
        self.magic_resist += (0.02 * self.level) 