from typing import List
from player import Player
from engine.combat_logger import CombatLogger

class CombatSystem:
    def __init__(self, player1: Player, player2: Player = None):
        self.player1 = player1
        self.player2 = player2 #Computer Opponent
        self.combat_started = False
        self.combat_logger = CombatLogger()  # Add combat logger
        
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
        """Simulate a complete combat (multiple rounds until one side dies)"""
        self._reset_heroes()
        self._apply_bonuses()
        
        combat_log = []
        round_number = 1
        
        # Continue combat until one side is defeated
        while self.player1.board and self.player2.board:
            combat_log.append(f"\n=== Round {round_number} ===")
            round_log = self._process_round()
            combat_log.extend(round_log)
            round_number += 1
            
        # Determine winner
        winner = self.player1 if self.player1.board else self.player2
        combat_log.append(f"\nCombat ended! {winner.__class__.__name__} is victorious!")
        
        return "\n".join(combat_log)
    
    def _process_round(self) -> List[str]:
        round_log = []
        active_heroes = self._get_sorted_heroes()
        
        for hero, owner in active_heroes:
            if not hero.is_alive():
                continue
                
            opponent = self.player2 if owner == self.player1 else self.player1
            if not opponent.board:  # Check if opponent has any units left
                break
                
            # Attack phase
            damage = hero.attack()
            target = opponent.board[0]  # Simple targeting for now
            actual_damage = target.take_phys_damage(damage)
            round_log.append(f"{owner.__class__.__name__}'s {hero.name} attacks {opponent.__class__.__name__}'s {target.name} for {actual_damage:.0f} damage!")
            round_log.append(f"Target HP: {target.hp}/{target.max_hp}")
            
            # Remove dead units
            if not target.is_alive():
                round_log.append(f"{target.name} has been defeated!")
                opponent.board.remove(target)
            
            # Mana and ability check
            if hero.mana >= hero.max_mana:
                # Pass available targets to ability_cast
                ability_result = hero.ability_cast(opponent.board)
                round_log.append(f"{owner.__class__.__name__}'s {ability_result}")
                hero.mana = 0
                round_log.append(f"{hero.name} mana reset to 0")
                
                # Clean up any dead units after ability
                opponent.remove_dead_heroes()
            else:
                hero.mana += 1
                round_log.append(f"{hero.name} gains 1 mana ({hero.mana}/{hero.max_mana})")
                
        return round_log 