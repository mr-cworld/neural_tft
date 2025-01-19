from heroes.hero import Hero

class Pyrrhus(Hero):
    origin = 'Fire'
    
    def __init__(self, name):
        super().__init__(name)
        self.name = 'Pyrrhus'
        # Stats - High agi ranger with DOT focus
        self.str = 35
        self.agi = 65
        self.max_hp = 550
        self.hp = self.max_hp
        self.armor = 0.20
        self.magic_resist = 0.20     
        # Mana
        self.mana = 0
        self.max_mana = 8
        self.starting_mana = 0
        # Core Stats
        self.origin = 'Fire'
        self.classes = 'Ranger'
        self.ability = self.ability_name()
        self.level_cost = 7
        self.buy_price = 2  # 2-cost unit

    def ability_name(self):
        return "Rain of Embers"

    def ability_cast(self, targets):
        # Arrow damage plus % max HP burn
        if not targets:
            return f"{self.name}'s {self.ability} found no targets!"
        
        arrow_damage = self.agi * 0.9
        burn_percent = 0.02 if self.level == 1 else 0.03 if self.level == 2 else 0.04
        
        # Hit up to 3 targets with arrows and burn
        hits = min(len(targets), 3)
        total_damage = 0
        
        for i in range(hits):
            # Initial arrow damage
            actual_damage = targets[i].take_physical_damage(arrow_damage)
            # Burn damage based on target's max HP
            burn_damage = targets[i].max_hp * burn_percent
            actual_burn = targets[i].take_magic_damage(burn_damage)
            total_damage += (actual_damage + actual_burn)
        
        return f"{self.name} uses {self.ability}, dealing {total_damage:.0f} total damage to {hits} targets with {burn_percent:.0%} max HP burn!"

    def level_up(self):
        print(f"{self.name} has leveled up!")
        self.level += 1
        self.level_cost = (self.level_cost * 2) + (self.level_cost / 2)
        # Stat Changes
        self.str += (30 * self.level)
        self.agi += (55 * self.level)
        self.max_hp += (450 * self.level)
        self.armor += (0.02 * self.level)
        self.magic_resist += (0.02 * self.level) 