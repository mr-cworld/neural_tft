from heroes.hero import Hero

class Ondine(Hero):
    origin = 'Water'
    
    def __init__(self, name):
        super().__init__(name)
        self.name = 'Ondine'
        # Stats - Strong bruiser with spell scaling
        self.str = 55
        self.agi = 40
        self.spell_power = 45
        self.max_hp = 750
        self.hp = self.max_hp
        self.armor = 0.30
        self.magic_resist = 0.30     
        # Mana
        self.mana = 0
        self.max_mana = 8
        self.starting_mana = 0
        # Core Stats
        self.origin = 'Water'
        self.classes = 'Bruiser'
        self.ability = self.ability_name()
        self.level_cost = 8
        self.buy_price = 3  # 3-cost unit

    def ability_name(self):
        return "Undertow Smash"

    def ability_cast(self, targets):
        # Damage and conditional team mana grant
        if not targets:
            return f"{self.name}'s {self.ability} found no targets!"
        
        damage = self.str + (0.5 * self.spell_power)
        mana_grant = 1 if self.level == 1 else 2 if self.level == 2 else 3
        
        actual_damage = targets[0].take_physical_damage(damage)
        
        # Grant mana to allies above 50% mana
        mana_granted = 0
        for ally in targets[1:]:  # Skip first target (enemy)
            if ally.mana >= (ally.max_mana * 0.5):
                ally.mana = min(ally.max_mana, ally.mana + mana_grant)
                mana_granted += 1
            
        return f"{self.name} uses {self.ability}, dealing {actual_damage:.0f} damage and granting {mana_grant} mana to {mana_granted} allies!"

    def level_up(self):
        print(f"{self.name} has leveled up!")
        self.level += 1
        self.level_cost = (self.level_cost * 2) + (self.level_cost / 2)
        # Stat Changes
        self.str += (45 * self.level)
        self.agi += (35 * self.level)
        self.spell_power += (40 * self.level)
        self.max_hp += (650 * self.level)
        self.armor += (0.02 * self.level)
        self.magic_resist += (0.02 * self.level) 