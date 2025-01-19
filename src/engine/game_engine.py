from typing import List
from player import Player
from heroes.Terran import Terran
from engine.combat_system import CombatSystem

class GameEngine:
    def __init__(self):
        self.round = 1
        self.players: List[Player] = []
        self.combat_system = None
    
    def initialize_game(self):
        """Initialize a new game with a single player"""
        player = Player(None, None)  
        self.players.append(player)
        self.combat_system = CombatSystem(self.players[0])
        return player  
    
    def simulate_round(self):
        """Simulate a complete game round (combat + buy phase)"""
        player = self.players[0]
        
        # Combat Phase - Full combat until one side is defeated
        combat_log = self.combat_system.simulate_combat()
        
        # Buy Phase
        print("\n=== Buy Phase ===")
        player.get_xp()
        player.round_end_gold()
        self.round += 1
        
        return combat_log
    
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
    
    def add_player(self):
        """Add a second board to the game (Computer Opponent)"""
        player = Player(None, None)
        self.players.append(player)
        self.combat_system = CombatSystem(self.players[0], self.players[1])  # Update combat system with both players
        return player 