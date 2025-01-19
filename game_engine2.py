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
        
