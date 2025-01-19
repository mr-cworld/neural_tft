from heroes.hero import Hero

class Craig(Hero):
    origin = 'Earth'
    
    def __init__(self, name):
        super().__init__(name)
        self.name = 'Craig'
        # Stats
        self.str = 45
        self.agi = 15
        self.max_hp = 600
        self.hp = self.max_hp
        self.armor = 0.30
        self.magic_resist = 0.30     
        # Mana
        self.mana = 3
        self.max_mana = 4
        self.starting_mana = 3
        # Core Stats
        self.origin = 'Earth'
        self.classes = 'Tank'
        self.ability = self.ability_name()
        self.level_cost = 6
        self.buy_price = 1

    def ability_name(self):
        return "Harden"

    def ability_cast(self, targets):
        # Healing based on missing HP
        if not targets:
            return f"{self.name}'s {self.ability} found no targets!"
        
        multiplier = 1.0 if self.level == 1 else 1.2 if self.level == 2 else 1.4
        base_heal = self.spell_power * multiplier
        
        # Find lowest HP ally
        target = min(targets, key=lambda x: x.hp/x.max_hp)
        missing_hp_percent = 1 - (target.hp / target.max_hp)
        heal_amount = base_heal * (1 + missing_hp_percent)  # Up to 2x healing on low HP targets
        
        old_hp = target.hp
        target.hp = min(target.max_hp, target.hp + heal_amount)
        actual_heal = target.hp - old_hp
        
        return f"{self.name} uses {self.ability}, healing {target.name} for {actual_heal:.0f} HP!"

    def level_up(self):
        print(f"{self.name} has leveled up!")
        # Level Up
        self.level += 1
        self.level_cost = (self.level_cost * 2) + (self.level_cost / 2)
        # Stat Changes
        self.str += (40 * self.level)
        self.agi += (15 * self.level)
        self.max_hp += (600 * self.level)
        self.armor += (0.01 * self.level)
        self.magic_resist += (0.03 * self.level)