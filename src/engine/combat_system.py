from typing import List, Tuple
from player import Player
from engine.combat_logger import CombatLogger
from copy import deepcopy
import math
from heroes.hero import Hero


class CombatSystem:
    def __init__(self, player1: Player, player2: Player = None):
        self.player1 = player1
        self.player2 = player2 #Computer Opponent
        self.combat_started = False
        self.combat_logger = CombatLogger()  # Add combat logger
        # Add state preservation
        self.preserved_p1_board = []
        self.preserved_p2_board = []
        self.ability_casts = {}  # Format: {(unit_name, player_name, ability_name): count}
        
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
        
    def _preserve_board_states(self) -> None:
        """Save the current board states before combat"""
        # Store references to original heroes
        self.preserved_p1_board = self.player1.board.copy()
        if self.player2:
            self.preserved_p2_board = self.player2.board.copy()
            
    def _restore_board_states(self) -> None:
        """Restore the preserved board states after combat"""
        # Restore original heroes with their pre-combat stats
        self.player1.board = self.preserved_p1_board
        if self.player2:
            self.player2.board = self.preserved_p2_board
        
        # Reset all heroes to full health/mana
        for hero in self.preserved_p1_board:
            hero.reset_hero()
        for hero in self.preserved_p2_board:
            hero.reset_hero()

    def _calculate_damage(self, winner_board: List, round_num: int) -> int:
        """Calculate damage based on surviving units and round number
        Damage = (2 × Number of surviving units) + max(1, round/3)
        """
        surviving_units = len(winner_board)
        round_damage = max(1, math.floor(round_num / 3))
        total_damage = (2 * surviving_units) + round_damage
        return total_damage

    def simulate_combat(self) -> dict:
        """Simulate a complete combat (multiple rounds until one side dies)"""
        # Save board states before combat
        self._preserve_board_states()
        self._reset_heroes()
        self._apply_bonuses()
        
        # Set teams for heroes
        for hero in self.player1.board:
            hero.team = 1
        for hero in self.player2.board:
            hero.team = 2
        
        combat_log = []
        round_number = 1
        
        print("Initial state:")
        print(f"Player 1 board: {[h.name for h in self.player1.board]}")
        print(f"Player 2 board: {[h.name for h in self.player2.board]}")
        
        # Continue combat until one side is defeated
        while self.player1.has_living_heroes() and self.player2.has_living_heroes():
            combat_log.append(f"\n=== Combat Round {round_number} ===")
            round_log = self._process_round()
            combat_log.extend(round_log)
            
            # Debug prints
            print(f"\nAfter round {round_number}:")
            print(f"Player 1 heroes: {[(h.name, h.hp) for h in self.player1.board]}")
            print(f"Player 2 heroes: {[(h.name, h.hp) for h in self.player2.board]}")
            
            round_number += 1
        
        # Determine winner and calculate damage
        if self.player1.has_living_heroes():
            winner = "player1"
            winner_board = self.player1.board
            loser = self.player2
            combat_log.append("\nPlayer 1 is victorious!")
        else:
            winner = "player2"
            winner_board = self.player2.board
            loser = self.player1
            combat_log.append("\nPlayer 2 is victorious!")
            
        # Calculate and apply damage
        damage = self._calculate_damage(winner_board, round_number)
        damage_result = loser.take_damage(damage)
        combat_log.append(f"\nDamage dealt: {damage} ({len(winner_board)} surviving units × 2 + {max(1, math.floor(round_number/3))} round damage)")
        combat_log.append(damage_result)
        
        # Restore board states after combat
        self._restore_board_states()
        
        return {
            "log": "\n".join(combat_log),
            "winner": winner,
            "damage_dealt": damage
        }
    
    def _process_round(self) -> List[str]:
        round_log = []
        active_heroes = self._get_sorted_heroes()
        
        for hero, owner in active_heroes:
            if not hero.is_alive():
                continue
                
            opponent = self.player2 if owner == self.player1 else self.player1
            if not opponent.has_living_heroes():  # Changed from board check to living heroes check
                break
                
            # Attack phase
            damage = hero.attack()
            target = opponent.get_first_living_hero()  # Get first living hero instead of board[0]
            if target:  # Only attack if there's a valid target
                actual_damage = target.take_phys_damage(damage)
                round_log.append(f"{owner.__class__.__name__}'s {hero.name} attacks {opponent.__class__.__name__}'s {target.name} for {actual_damage:.0f} damage!")
                round_log.append(f"Target HP: {target.hp}/{target.max_hp}")
                
                # Clean up any dead units after attack
                opponent.remove_dead_heroes()
            
            # Mana and ability check
            if hero.mana >= hero.max_mana:
                # Pass available targets to ability_cast
                ability_result = hero.ability_cast(opponent.board)
                round_log.append(f"{owner.__class__.__name__}'s {ability_result}")
                # Record the ability cast
                self._record_ability_cast(hero, owner, hero.ability)
                hero.mana = 0
                round_log.append(f"{hero.name} mana reset to 0")
                
                # Clean up any dead units after ability
                opponent.remove_dead_heroes()
            else:
                hero.mana += 1
                round_log.append(f"{hero.name} gains 1 mana ({hero.mana}/{hero.max_mana})")
                
        return round_log 

    def _record_ability_cast(self, hero: Hero, player: Player, ability_name: str):
        """Record an ability cast for summary"""
        key = (hero.name, player.__class__.__name__, ability_name)
        self.ability_casts[key] = self.ability_casts.get(key, 0) + 1
        
    def get_ability_cast_summary(self) -> str:
        """Return formatted summary of ability casts"""
        if not self.ability_casts:
            return "No abilities were cast during combat"
            
        output = ["\n=== Ability Cast Summary ==="]
        output.append(f"{'Unit':<15} {'Player':<15} {'Ability':<20} {'Casts':<5}")
        output.append("-" * 55)
        
        # Sort by cast count (descending)
        sorted_casts = sorted(self.ability_casts.items(), key=lambda x: x[1], reverse=True)
        for (unit, player, ability), casts in sorted_casts:
            output.append(f"{unit:<15} {player:<15} {ability:<20} {casts:<5}")
            
        return "\n".join(output) 