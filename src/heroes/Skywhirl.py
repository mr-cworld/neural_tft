from heroes.hero import Hero

class Skywhirl(Hero):
    origin = 'Wind'
    
    def __init__(self, name):
        super().__init__(name)
        self.name = 'Skywhirl'
        # Stats - Balanced str/agi for bruiser
        self.str = 45
        self.agi = 45
        self.max_hp = 650
        self.hp = self.max_hp
        self.armor = 0.25
        self.magic_resist = 0.25     
        # Mana
        self.mana = 0
        self.max_mana = 7
        self.starting_mana = 0
        # Core Stats
        self.origin = 'Wind'
        self.classes = 'Bruiser'
        self.ability = self.ability_name()
        self.level_cost = 7
        self.buy_price = 2  # 2-cost unit

    def ability_name(self):
        return "Whirling Leap"

    def ability_cast(self, targets):
        # Leap damage based on str + agi with AOE splash
        if not targets:
            return f"{self.name}'s {self.ability} found no targets!"
            
        # Main target damage
        multiplier = 2.0 if self.level == 1 else 2.5 if self.level == 2 else 3.0
        main_damage = (self.str + self.agi) * multiplier
        splash_damage = main_damage * 0.3
        
        # Deal main damage to primary target
        actual_damage = targets[0].take_physical_damage(main_damage)
        total_damage = actual_damage
        
        # Deal splash to up to 2 additional targets
        splash_hits = min(len(targets[1:]), 2)
        for i in range(splash_hits):
            splash_actual = targets[i+1].take_physical_damage(splash_damage)
            total_damage += splash_actual
            
        return f"{self.name} uses {self.ability}, dealing {actual_damage:.0f} damage to {targets[0].name} and {splash_damage:.0f} splash to {splash_hits} nearby enemies!"

    def level_up(self):
        print(f"{self.name} has leveled up!")
        self.level += 1
        self.level_cost = (self.level_cost * 2) + (self.level_cost / 2)
        # Stat Changes
        self.str += (40 * self.level)
        self.agi += (40 * self.level)
        self.max_hp += (550 * self.level)
        self.armor += (0.02 * self.level)
        self.magic_resist += (0.02 * self.level) 