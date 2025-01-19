from typing import List
from player import Player

class CombatSystem:
    def __init__(self, player1: Player, player2: Player = None):
        self.player1 = player1
        self.player2 = player2 #Computer Opponent
        self.combat_started = False
        
    def _reset_heroes(self) -> None:
        """Reset heroes only at the start of combat"""
        if not self.combat_started:
            for hero in self.player1.board + (self.player2.board if self.player2 else []):
                hero.reset_hero()
            self.combat_started = True
            
    def _apply_bonuses(self) -> None:
        """Apply origin and class bonuses for both players"""
        self.player1.check_heroes()
        if self.player2:
            self.player2.check_heroes()
        
    def _get_sorted_heroes(self) -> List:
        """Get all heroes sorted by agility"""
        all_heroes = []
        all_heroes.extend((hero, self.player1) for hero in self.player1.board)
        if self.player2:
            all_heroes.extend((hero, self.player2) for hero in self.player2.board)
        # Sort by agility and return hero objects
        return sorted(all_heroes, key=lambda x: x[0].agi, reverse=True)
        
    def simulate_combat(self) -> str:
        """Simulate a complete combat round"""
        self._reset_heroes()
        self._apply_bonuses()
        active_heroes = self._get_sorted_heroes()
        
        combat_log = []
        for hero, owner in active_heroes:
            # Get opponent's board for targeting
            opponent = self.player2 if owner == self.player1 else self.player1
            if not opponent.board:  # Skip if no targets
                continue
                
            # Attack phase
            damage = hero.attack()
            target = opponent.board[0]  # Simple targeting for now
            actual_damage = target.take_phys_damage(damage)
            combat_log.append(f"{owner.__class__.__name__}'s {hero.name} attacks {opponent.__class__.__name__}'s {target.name} for {actual_damage:.0f} damage!")
            combat_log.append(f"Target HP: {target.hp}/{target.max_hp}")
            
            # Mana and ability check
            if hero.mana >= hero.max_mana:
                ability_result = hero.ability_cast()
                combat_log.append(ability_result)
                hero.mana = 0
                combat_log.append(f"{hero.name} mana reset to 0")
            else:
                combat_log.append(f"{hero.name} gains 1 mana ({hero.mana}/{hero.max_mana})")
                
        return "\n".join(combat_log) 