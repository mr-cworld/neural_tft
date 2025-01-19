from heroes.hero import Hero

class Blaze(Hero):
    origin = 'Fire'
    
    def __init__(self, name):
        super().__init__(name)
        self.name = 'Blaze'
        # Stats - Strong fighter with DOT focus
        self.str = 55
        self.agi = 50
        self.spell_power = 40
        self.max_hp = 700
        self.hp = self.max_hp
        self.armor = 0.25
        self.magic_resist = 0.25     
        # Mana
        self.mana = 0
        self.max_mana = 7
        self.starting_mana = 0
        # Core Stats
        self.origin = 'Fire'
        self.classes = 'Fighter'
        self.ability = self.ability_name()
        self.level_cost = 9
        self.buy_price = 3  # 3-cost unit

    def ability_name(self):
        return "Burning Flurry"

    def ability_cast(self, targets):
        # Double strike with burn effect
        if not targets:
            return f"{self.name}'s {self.ability} found no targets!"
        
        hit_damage = self.str * (0.8 if self.level == 1 else 0.9 if self.level == 2 else 1.0)
        burn_damage = (self.str + self.spell_power) * (0.2 if self.level == 1 else 0.4 if self.level == 2 else 0.6)
        
        # Two hits on primary target
        total_damage = 0
        for _ in range(2):
            actual_damage = targets[0].take_magic_damage(hit_damage)
            total_damage += actual_damage
        
        # Apply burn
        actual_burn = targets[0].take_magic_damage(burn_damage)
        total_damage += actual_burn
        
        return f"{self.name} uses {self.ability}, dealing {total_damage:.0f} total damage to {targets[0].name}!"

    def level_up(self):
        print(f"{self.name} has leveled up!")
        self.level += 1
        self.level_cost = (self.level_cost * 2) + (self.level_cost / 2)
        # Stat Changes
        self.str += (45 * self.level)
        self.agi += (40 * self.level)
        self.spell_power += (35 * self.level)
        self.max_hp += (600 * self.level)
        self.armor += (0.02 * self.level)
        self.magic_resist += (0.02 * self.level) 