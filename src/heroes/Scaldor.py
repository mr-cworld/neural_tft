from heroes.hero import Hero

class Scaldor(Hero):
    origin = 'Fire'
    
    def __init__(self, name):
        super().__init__(name)
        self.name = 'Scaldor'
        # Stats - Balanced tank with offensive capability
        self.str = 40
        self.agi = 25
        self.max_hp = 650
        self.hp = self.max_hp
        self.armor = 0.35
        self.magic_resist = 0.30     
        # Mana
        self.mana = 0
        self.max_mana = 7
        self.starting_mana = 0
        # Core Stats
        self.origin = 'Fire'
        self.classes = 'Tank'
        self.ability = self.ability_name()
        self.level_cost = 6
        self.buy_price = 2  # 2-cost unit

    def ability_name(self):
        return "Molten Guard"

    def ability_cast(self, targets):
        # Gains armor and reflects damage to attackers
        if not targets:
            return f"{self.name}'s {self.ability} found no targets!"
        
        # Armor gain scales with level
        armor_gain = 0.15 if self.level == 1 else 0.20 if self.level == 2 else 0.30
        old_armor = self.armor
        self.armor = min(0.80, self.armor + armor_gain)
        
        # Reflect damage to closest enemies
        reflect_damage = self.str * (0.3 if self.level == 1 else 0.5 if self.level == 2 else 0.7)
        hits = min(len(targets), 2)
        total_damage = 0
        
        for i in range(hits):
            actual_damage = targets[i].take_magic_damage(reflect_damage)
            total_damage += actual_damage
        
        return f"{self.name} uses {self.ability}, gaining {(self.armor - old_armor):.0%} Armor and reflecting {total_damage:.0f} heat damage to {hits} enemies!"

    def level_up(self):
        print(f"{self.name} has leveled up!")
        self.level += 1
        self.level_cost = (self.level_cost * 2) + (self.level_cost / 2)
        # Stat Changes
        self.str += (35 * self.level)
        self.agi += (20 * self.level)
        self.max_hp += (550 * self.level)
        self.armor += (0.03 * self.level)
        self.magic_resist += (0.02 * self.level) 