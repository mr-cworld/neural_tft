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
        """Initialize a new game with a single player and Terran"""
        player = Player(None, None)  # AI parameter not used yet
        terran = Terran("Terran")
        player.add_hero(terran)
        self.players.append(player)
        self.combat_system = CombatSystem(self.players[0])
        
    def simulate_round(self):
        """Simulate a single round of combat"""
        player = self.players[0]
        
        # Run combat simulation
        combat_log = self.combat_system.simulate_combat()
        print(combat_log)
        
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