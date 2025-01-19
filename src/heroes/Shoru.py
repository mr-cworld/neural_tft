from heroes.hero import Hero

class Shoru(Hero):
    origin = 'Water'
    
    def __init__(self, name):
        super().__init__(name)
        self.name = 'Shoru'
        # Stats - High spell power mage
        self.str = 35
        self.agi = 40
        self.spell_power = 75
        self.max_hp = 600
        self.hp = self.max_hp
        self.armor = 0.20
        self.magic_resist = 0.25     
        # Mana
        self.mana = 0
        self.max_mana = 8
        self.starting_mana = 0
        # Core Stats
        self.origin = 'Water'
        self.classes = 'Mage'
        self.ability = self.ability_name()
        self.level_cost = 8
        self.buy_price = 3  # 3-cost unit

    def ability_name(self):
        return "Wave Surge"

    def ability_cast(self, targets):
        # Wave hitting multiple random enemies
        if not targets:
            return f"{self.name}'s {self.ability} found no targets!"
        
        import random
        
        # Scaling with level
        num_hits = 2 if self.level == 1 else 3 if self.level == 2 else 4
        damage_multi = 1.2 if self.level == 1 else 1.5 if self.level == 2 else 1.8
        base_damage = self.spell_power * damage_multi
        
        # Select random targets
        hits = min(len(targets), num_hits)
        random_targets = random.sample(targets, hits)
        total_damage = 0
        
        for target in random_targets:
            actual_damage = target.take_magic_damage(base_damage)
            total_damage += actual_damage
        
        return f"{self.name} uses {self.ability}, hitting {hits} random targets for {total_damage:.0f} total magic damage!"

    def level_up(self):
        print(f"{self.name} has leveled up!")
        self.level += 1
        self.level_cost = (self.level_cost * 2) + (self.level_cost / 2)
        # Stat Changes
        self.str += (30 * self.level)
        self.agi += (35 * self.level)
        self.spell_power += (65 * self.level)
        self.max_hp += (500 * self.level)
        self.armor += (0.02 * self.level)
        self.magic_resist += (0.02 * self.level) 