from heroes.hero import Hero

class Noctis(Hero):
    origin = 'Dark'
    
    def __init__(self, name):
        super().__init__(name)
        self.name = 'Noctis'
        # Stats - High damage fighter
        self.str = 60
        self.agi = 45
        self.max_hp = 650
        self.hp = self.max_hp
        self.armor = 0.25
        self.magic_resist = 0.25     
        # Mana
        self.mana = 0
        self.max_mana = 6
        self.starting_mana = 0
        # Core Stats
        self.origin = 'Dark'
        self.classes = 'Fighter'
        self.ability = self.ability_name()
        self.level_cost = 9
        self.buy_price = 4  # 4-cost unit

    def ability_name(self):
        return "Shadow Lunge"

    def ability_cast(self, targets):
        # Damage based on str and target's magic resist with lifesteal
        if not targets:
            return f"{self.name}'s {self.ability} found no targets!"
        
        base_damage = self.str * 1.5
        mr_bonus = targets[0].magic_resist * 0.1  # 10% of target's MR as bonus damage
        lifesteal_percent = 0.02 if self.level == 1 else 0.04 if self.level == 2 else 0.06
        
        total_damage = base_damage + (base_damage * mr_bonus)
        actual_damage = targets[0].take_physical_damage(total_damage)
        
        # Apply lifesteal
        heal_amount = actual_damage * lifesteal_percent
        self.hp = min(self.max_hp, self.hp + heal_amount)
        
        return f"{self.name} uses {self.ability}, dealing {actual_damage:.0f} damage and healing for {heal_amount:.0f}!"

    def level_up(self):
        print(f"{self.name} has leveled up!")
        self.level += 1
        self.level_cost = (self.level_cost * 2) + (self.level_cost / 2)
        # Stat Changes
        self.str += (50 * self.level)
        self.agi += (35 * self.level)
        self.max_hp += (550 * self.level)
        self.armor += (0.02 * self.level)
        self.magic_resist += (0.02 * self.level) 