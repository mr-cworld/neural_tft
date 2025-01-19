from heroes.hero import Hero

class Aurion(Hero):
    origin = 'Light'
    
    def __init__(self, name):
        super().__init__(name)
        self.name = 'Aurion'
        # Stats - Balanced tank with healing
        self.str = 45
        self.agi = 30
        self.max_hp = 750
        self.hp = self.max_hp
        self.armor = 0.35
        self.magic_resist = 0.35     
        # Mana
        self.mana = 0
        self.max_mana = 6
        self.starting_mana = 0
        # Core Stats
        self.origin = 'Light'
        self.classes = 'Tank'
        self.ability = self.ability_name()
        self.level_cost = 6
        self.buy_price = 2  # 2-cost unit

    def ability_name(self):
        return "Beacon of Valor"

    def ability_cast(self, targets):
        # Damage and conditional self-heal
        if not targets:
            return f"{self.name}'s {self.ability} found no targets!"
        
        damage = self.str * 1.2
        heal_percent = 0.02 if self.level == 1 else 0.03 if self.level == 2 else 0.04
        heal_amount = self.max_hp * heal_percent
        
        actual_damage = targets[0].take_magic_damage(damage)
        
        # Heal if below 50% HP
        if self.hp < (self.max_hp * 0.5):
            self.hp = min(self.max_hp, self.hp + heal_amount)
            return f"{self.name} uses {self.ability}, dealing {actual_damage:.0f} damage and healing for {heal_amount:.0f} HP!"
        
        return f"{self.name} uses {self.ability}, dealing {actual_damage:.0f} damage!"

    def level_up(self):
        print(f"{self.name} has leveled up!")
        self.level += 1
        self.level_cost = (self.level_cost * 2) + (self.level_cost / 2)
        # Stat Changes
        self.str += (40 * self.level)
        self.agi += (25 * self.level)
        self.max_hp += (650 * self.level)
        self.armor += (0.03 * self.level)
        self.magic_resist += (0.03 * self.level) 