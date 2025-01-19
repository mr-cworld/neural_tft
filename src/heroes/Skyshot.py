from heroes.hero import Hero

class Skyshot(Hero):
    origin = 'Wind'
    
    def __init__(self, name):
        super().__init__(name)
        self.name = 'Skyshot'
        # Stats - Very high agi focus
        self.str = 30
        self.agi = 70
        self.max_hp = 550
        self.hp = self.max_hp
        self.armor = 0.20
        self.magic_resist = 0.20     
        # Mana
        self.mana = 0
        self.max_mana = 8
        self.starting_mana = 0
        # Core Stats
        self.origin = 'Wind'
        self.classes = 'Ranger'
        self.ability = self.ability_name()
        self.level_cost = 8
        self.buy_price = 3  # 3-cost unit

    def ability_name(self):
        return "Feathered Volley"

    def ability_cast(self, targets):
        # Multiple arrows with crit chance
        if not targets:
            return f"{self.name}'s {self.ability} found no targets!"
        
        import random
        
        # Scaling with level
        num_arrows = max(3, (self.agi // 69) + self.level)
        base_damage = self.agi * (0.75 if self.level == 1 else 0.9 if self.level == 2 else 1.05)
        crit_chance = 0.20 if self.level == 1 else 0.23 if self.level == 2 else 0.28
        crit_multi = 1.2 if self.level == 1 else 1.4 if self.level == 2 else 1.6
        
        total_damage = 0
        crits = 0
        hits = min(len(targets), num_arrows)
        
        for i in range(hits):
            damage = base_damage
            if random.random() < crit_chance:
                damage *= crit_multi
                crits += 1
            
            actual_damage = targets[i].take_physical_damage(damage)
            total_damage += actual_damage
        
        return f"{self.name} uses {self.ability}, firing {hits} arrows for {total_damage:.0f} total damage with {crits} critical hits!"

    def level_up(self):
        print(f"{self.name} has leveled up!")
        self.level += 1
        self.level_cost = (self.level_cost * 2) + (self.level_cost / 2)
        # Stat Changes - Heavy agi scaling
        self.str += (25 * self.level)
        self.agi += (60 * self.level)
        self.max_hp += (450 * self.level)
        self.armor += (0.02 * self.level)
        self.magic_resist += (0.02 * self.level) 