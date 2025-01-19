from heroes.hero import Hero

class Halo(Hero):
    origin = 'Light'
    
    def __init__(self, name):
        super().__init__(name)
        self.name = 'Halo'
        # Stats - High spell power mage
        self.str = 35
        self.agi = 35
        self.spell_power = 80
        self.max_hp = 650
        self.hp = self.max_hp
        self.armor = 0.20
        self.magic_resist = 0.20     
        # Mana
        self.mana = 0
        self.max_mana = 8
        self.starting_mana = 0
        # Core Stats
        self.origin = 'Light'
        self.classes = 'Mage'
        self.ability = self.ability_name()
        self.level_cost = 8
        self.buy_price = 3  # 3-cost unit

    def ability_name(self):
        return "Illumine"

    def ability_cast(self, targets):
        # Magic damage and conditional team heal
        if not targets:
            return f"{self.name}'s {self.ability} found no targets!"
        
        multiplier = 1.5 if self.level == 1 else 1.8 if self.level == 2 else 2.2
        damage = self.spell_power * multiplier
        heal_percent = 0.01 if self.level == 1 else 0.02 if self.level == 2 else 0.03
        
        hits = min(len(targets), 2)
        total_damage = 0
        
        for i in range(hits):
            actual_damage = targets[i].take_magic_damage(damage)
            total_damage += actual_damage
            
            # Heal self if target is below 50% HP
            if targets[i].hp < (targets[i].max_hp * 0.5):
                heal_amount = self.max_hp * heal_percent
                self.hp = min(self.max_hp, self.hp + heal_amount)
                return f"{self.name} uses {self.ability}, dealing {total_damage:.0f} damage and healing for {heal_amount:.0f}!"
            
        return f"{self.name} uses {self.ability}, dealing {total_damage:.0f} damage to {hits} targets!"

    def level_up(self):
        print(f"{self.name} has leveled up!")
        self.level += 1
        self.level_cost = (self.level_cost * 2) + (self.level_cost / 2)
        # Stat Changes
        self.str += (30 * self.level)
        self.agi += (30 * self.level)
        self.spell_power += (70 * self.level)
        self.max_hp += (550 * self.level)
        self.armor += (0.02 * self.level)
        self.magic_resist += (0.02 * self.level) 