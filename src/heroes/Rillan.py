from heroes.hero import Hero

class Rillan(Hero):
    origin = 'Water'
    
    def __init__(self, name):
        super().__init__(name)
        self.name = 'Rillan'
        # Stats - Support with high spell power
        self.str = 30
        self.agi = 35
        self.spell_power = 75
        self.max_hp = 600
        self.hp = self.max_hp
        self.armor = 0.25
        self.magic_resist = 0.25     
        # Mana
        self.mana = 0
        self.max_mana = 8
        self.starting_mana = 0
        # Core Stats
        self.origin = 'Water'
        self.classes = 'Support'
        self.ability = self.ability_name()
        self.level_cost = 9
        self.buy_price = 4  # 4-cost unit

    def ability_name(self):
        return "Mana Cascade"

    def ability_cast(self, targets):
        # Healing or mana grant based on target HP
        if not targets:
            return f"{self.name}'s {self.ability} found no targets!"
        
        # Scale healing and mana with level
        multiplier = 1.0 if self.level == 1 else 1.2 if self.level == 2 else 1.4
        heal_amount = self.spell_power * multiplier
        mana_bonus = 2 if self.level == 1 else 4 if self.level == 2 else 6
        
        # Sort targets by lowest HP percentage
        sorted_targets = sorted(targets, key=lambda x: x.hp/x.max_hp)
        hits = min(len(sorted_targets), 2)  # Heal 2 allies
        total_healing = 0
        mana_grants = 0
        
        for i in range(hits):
            target = sorted_targets[i]
            if target.hp < (target.max_hp * 0.5):  # Below 50% HP
                old_hp = target.hp
                target.hp = min(target.max_hp, target.hp + heal_amount)
                actual_heal = target.hp - old_hp
                total_healing += actual_heal
            else:  # Above 50% HP
                target.mana = min(target.max_mana, target.mana + mana_bonus)
                mana_grants += 1
            
        if mana_grants > 0:
            return f"{self.name} uses {self.ability}, healing for {total_healing:.0f} and granting {mana_bonus} mana to {mana_grants} high-HP allies!"
        else:
            return f"{self.name} uses {self.ability}, healing allies for {total_healing:.0f} total HP!"

    def level_up(self):
        print(f"{self.name} has leveled up!")
        self.level += 1
        self.level_cost = (self.level_cost * 2) + (self.level_cost / 2)
        # Stat Changes
        self.str += (25 * self.level)
        self.agi += (30 * self.level)
        self.spell_power += (65 * self.level)
        self.max_hp += (500 * self.level)
        self.armor += (0.02 * self.level)
        self.magic_resist += (0.02 * self.level) 