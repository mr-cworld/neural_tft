from heroes.hero import Hero

class Seafin(Hero):
    origin = 'Water'
    
    def __init__(self, name):
        super().__init__(name)
        self.name = 'Seafin'
        # Stats - High spell power chain mage
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
        self.origin = 'Water'
        self.classes = 'Mage'
        self.ability = self.ability_name()
        self.level_cost = 9
        self.buy_price = 4  # 4-cost unit

    def ability_name(self):
        return "Wave Resonance"

    def ability_cast(self, targets):
        # Chain heal with mana generation
        if not targets:
            return f"{self.name}'s {self.ability} found no targets!"
        
        # Base heal amount scales with spell power
        heal_multiplier = 1.2 if self.level == 1 else 1.5 if self.level == 2 else 1.8
        base_heal = self.spell_power * heal_multiplier
        chain_heal = base_heal * 0.7  # 70% effectiveness on chain targets
        mana_gain = 1 if self.level == 1 else 2 if self.level == 2 else 3
        
        # Find lowest HP targets to heal
        sorted_targets = sorted(targets, key=lambda x: x.hp/x.max_hp)
        hits = min(len(sorted_targets), 3)
        total_healing = 0
        
        # Primary heal on lowest HP target
        primary_target = sorted_targets[0]
        primary_target.hp = min(primary_target.max_hp, primary_target.hp + base_heal)
        total_healing += base_heal
        primary_target.mana = min(primary_target.max_mana, primary_target.mana + mana_gain)
        
        # Chain heal to other low HP targets
        for i in range(1, hits):
            target = sorted_targets[i]
            target.hp = min(target.max_hp, target.hp + chain_heal)
            total_healing += chain_heal
            target.mana = min(target.max_mana, target.mana + mana_gain)
        
        return f"{self.name} uses {self.ability}, healing for {total_healing:.0f} total HP and granting {mana_gain} mana to {hits} allies!"

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