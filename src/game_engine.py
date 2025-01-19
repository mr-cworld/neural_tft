from typing import List
from player import Player
from heroes.Terran import Terran

class GameEngine:
    def __init__(self):
        self.round = 1
        self.players: List[Player] = []
    
    def initialize_game(self):
        """Initialize a new game with a single player and Terran"""
        player = Player(None, None)  # AI parameter not used yet
        terran = Terran("Terran")
        player.add_hero(terran)
        self.players.append(player)
        
    def simulate_round(self):
        """Simulate a single round of combat"""
        player = self.players[0]
        
        # Reset all heroes for the round
        for hero in player.board:
            hero.reset_hero()
            
        # Sort heroes by agility (highest to lowest)
        active_heroes = sorted(player.board, key=lambda x: x.agi, reverse=True)
        
        # Apply origin and class bonuses
        origins, classes = player.check_heroes()
        
        # Simple combat simulation (will expand later)
        for hero in active_heroes:
            # For now, just have the hero attack once
            damage = hero.attack()
            print(f"{hero.name} attacks for {damage} damage!")
            
            # Check if hero can cast ability
            if hero.mana >= hero.max_mana:
                print(hero.ability_cast())
        
        # End round processing
        player.get_xp()
        player.round_end_gold()
        self.round += 1
        
        return f"Round {self.round} completed"
    
    def get_game_state(self):
        """Return current game state"""
        player = self.players[0]
        return {
            "round": self.round,
            "player_gold": player.gold,
            "player_level": player.level,
            "player_health": player.health,
            "heroes": [(hero.name, hero.hp, hero.mana) for hero in player.board]
        } 