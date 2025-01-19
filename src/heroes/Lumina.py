from heroes.hero import Hero

class Lumina(Hero):
    origin = 'Light'
    
    def __init__(self, name):
        super().__init__(name)
        self.name = 'Lumina'
        # Stats - Support focused on healing
        self.str = 30
        self.agi = 35
        self.spell_power = 70
        self.max_hp = 600
        self.hp = self.max_hp
        self.armor = 0.25
        self.magic_resist = 0.25     
        # Mana
        self.mana = 0
        self.max_mana = 7
        self.starting_mana = 0
        # Core Stats
        self.origin = 'Light'
        self.classes = 'Support'
        self.ability = self.ability_name()
        self.level_cost = 8
        self.buy_price = 3  # 3-cost unit

    def ability_name(self):
        return "Radiant Blessing"

    def ability_cast(self, targets):
        # Healing and conditional str buff
        if not targets:
            return f"{self.name}'s {self.ability} found no targets!"
        
        heal_multiplier = 1.3 if self.level == 1 else 1.6 if self.level == 2 else 2.0
        heal_amount = self.spell_power * heal_multiplier
        str_bonus = 2 if self.level == 1 else 4 if self.level == 2 else 6
        
        # Find lowest HP target
        target = min(targets, key=lambda x: x.hp/x.max_hp)
        target.hp = min(target.max_hp, target.hp + heal_amount)
        
        # Grant STR if target was below 50% HP
        if target.hp < (target.max_hp * 0.5):
            target.str += str_bonus
            return f"{self.name} uses {self.ability}, healing {target.name} for {heal_amount:.0f} and granting {str_bonus} STR!"
        
        return f"{self.name} uses {self.ability}, healing {target.name} for {heal_amount:.0f}!"

    def level_up(self):
        print(f"{self.name} has leveled up!")
        self.level += 1
        self.level_cost = (self.level_cost * 2) + (self.level_cost / 2)
        # Stat Changes
        self.str += (25 * self.level)
        self.agi += (30 * self.level)
        self.spell_power += (60 * self.level)
        self.max_hp += (500 * self.level)
        self.armor += (0.02 * self.level)
        self.magic_resist += (0.02 * self.level) 