from heroes.hero import Hero

class Marina(Hero):
    origin = 'Water'
    
    def __init__(self, name):
        super().__init__(name)
        self.name = 'Marina'
        # Stats - Support with good spell power
        self.str = 30
        self.agi = 35
        self.spell_power = 70
        self.max_hp = 600
        self.hp = self.max_hp
        self.armor = 0.25
        self.magic_resist = 0.25     
        # Mana
        self.mana = 0
        self.max_mana = 7
        self.starting_mana = 0
        # Core Stats
        self.origin = 'Water'
        self.classes = 'Support'
        self.ability = self.ability_name()
        self.level_cost = 7
        self.buy_price = 2  # 2-cost unit

    def ability_name(self):
        return "Mana Tide"

    def ability_cast(self, targets):
        # Healing and mana grant
        if not targets:
            return f"{self.name}'s {self.ability} found no targets!"
        
        multiplier = 1.0 if self.level == 1 else 1.3 if self.level == 2 else 1.6
        heal_amount = self.spell_power * multiplier
        mana_gain = 2 if self.level == 1 else 4 if self.level == 2 else 6
        
        # Heal lowest HP target
        target = min(targets, key=lambda x: x.hp/x.max_hp)
        target.hp = min(target.max_hp, target.hp + heal_amount)
        
        # Grant mana to target and half to another random ally if available
        target.mana = min(target.max_mana, target.mana + mana_gain)
        
        if len(targets) > 1:
            secondary_target = targets[1]  # Get second target if available
            secondary_target.mana = min(secondary_target.max_mana, 
                                      secondary_target.mana + (mana_gain // 2))
            return f"{self.name} uses {self.ability}, healing {target.name} for {heal_amount:.0f} and granting {mana_gain} mana (and {mana_gain//2} to {secondary_target.name})!"
        
        return f"{self.name} uses {self.ability}, healing {target.name} for {heal_amount:.0f} and granting {mana_gain} mana!"

    def level_up(self):
        print(f"{self.name} has leveled up!")
        self.level += 1
        self.level_cost = (self.level_cost * 2) + (self.level_cost / 2)
        # Stat Changes
        self.str += (25 * self.level)
        self.agi += (30 * self.level)
        self.spell_power += (60 * self.level)
        self.max_hp += (500 * self.level)
        self.armor += (0.02 * self.level)
        self.magic_resist += (0.02 * self.level) 