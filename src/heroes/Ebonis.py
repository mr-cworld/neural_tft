from heroes.hero import Hero

class Ebonis(Hero):
    origin = 'Dark'
    
    def __init__(self, name):
        super().__init__(name)
        self.name = 'Ebonis'
        # Stats - High spell power mage
        self.str = 35
        self.agi = 35
        self.spell_power = 80
        self.max_hp = 600
        self.hp = self.max_hp
        self.armor = 0.20
        self.magic_resist = 0.20     
        # Mana
        self.mana = 0
        self.max_mana = 8
        self.starting_mana = 0
        # Core Stats
        self.origin = 'Dark'
        self.classes = 'Mage'
        self.ability = self.ability_name()
        self.level_cost = 8
        self.buy_price = 3  # 3-cost unit

    def ability_name(self):
        return "Eclipse Bolt"

    def ability_cast(self, targets):
        # Magic damage based on spell power and target's armor
        if not targets:
            return f"{self.name}'s {self.ability} found no targets!"
        
        multiplier = 1.6 if self.level == 1 else 1.9 if self.level == 2 else 2.2
        base_damage = self.spell_power * multiplier
        armor_bonus = targets[0].armor * 0.5  # 50% of target's armor as bonus damage
        
        damage = base_damage + (base_damage * armor_bonus)
        if targets[0].hp < (targets[0].max_hp * 0.5):  # Below 50% HP
            damage *= 1.25  # 25% bonus damage
        
        actual_damage = targets[0].take_magic_damage(damage)
        return f"{self.name} uses {self.ability}, dealing {actual_damage:.0f} magic damage to {targets[0].name}!"

    def level_up(self):
        print(f"{self.name} has leveled up!")
        self.level += 1
        self.level_cost = (self.level_cost * 2) + (self.level_cost / 2)
        # Stat Changes
        self.str += (30 * self.level)
        self.agi += (30 * self.level)
        self.spell_power += (70 * self.level)
        self.max_hp += (500 * self.level)
        self.armor += (0.02 * self.level)
        self.magic_resist += (0.02 * self.level) 