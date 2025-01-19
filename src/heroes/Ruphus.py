from heroes.hero import Hero

class Ruphus(Hero):
    origin = 'Wind'
    
    def __init__(self, name):
        super().__init__(name)
        self.name = 'Ruphus'
        # Stats - High agi for Wind fighter
        self.str = 40
        self.agi = 55
        self.max_hp = 600
        self.hp = self.max_hp
        self.armor = 0.25
        self.magic_resist = 0.25     
        # Mana
        self.mana = 0
        self.max_mana = 6
        self.starting_mana = 0
        # Core Stats
        self.origin = 'Wind'
        self.classes = 'Fighter'
        self.ability = self.ability_name()
        self.level_cost = 7
        self.buy_price = 2  # 2-cost unit

    def ability_name(self):
        return "Gust Slash"

    def ability_cast(self, targets):
        # Multiple strikes based on agi
        if not targets:
            return f"{self.name}'s {self.ability} found no targets!"
        
        # Number of strikes scales with level
        base_strikes = 2 if self.level == 1 else 3 if self.level == 2 else 4
        num_strikes = max(base_strikes, self.agi // 100)
        damage_per_strike = self.agi * (1.0 if self.level == 1 else 1.25 if self.level == 2 else 1.5)
        
        # Find second highest HP target
        sorted_targets = sorted(targets, key=lambda x: x.hp, reverse=True)
        target = sorted_targets[1] if len(sorted_targets) > 1 else sorted_targets[0]
        
        total_damage = 0
        for _ in range(num_strikes):
            actual_damage = target.take_physical_damage(damage_per_strike)
            total_damage += actual_damage
        
        return f"{self.name} uses {self.ability}, striking {target.name} {num_strikes} times for {total_damage:.0f} total damage!"

    def level_up(self):
        print(f"{self.name} has leveled up!")
        self.level += 1
        self.level_cost = (self.level_cost * 2) + (self.level_cost / 2)
        # Stat Changes
        self.str += (35 * self.level)
        self.agi += (45 * self.level)
        self.max_hp += (500 * self.level)
        self.armor += (0.02 * self.level)
        self.magic_resist += (0.02 * self.level) 