from typing import List
from player import Player
from heroes.Terran import Terran
from heroes.Craig import Craig
from engine.combat_system import CombatSystem
from engine.shop_engine import ShopEngine

class GameEngine:
    def __init__(self):
        self.round = 1
        self.players: List[Player] = []
        self.combat_system = None
        self.shop_engine = ShopEngine()  # Add shop engine
        
        # Register all hero types with the shop
        self._register_heroes()
    
    def _register_heroes(self):
        """Register all available heroes with the shop engine"""
        # You'll need to import all hero classes and register them here
        self.shop_engine.register_hero(Terran, 1)
        self.shop_engine.register_hero(Craig, 1)
        # ... register other heroes ...
    
    def initialize_game(self):
        """Initialize a new game with a single player"""
        player = Player(None, None)  
        self.players.append(player)
        self.combat_system = CombatSystem(self.players[0])
        
        # Initial shop roll
        self.shop_engine.roll_shop(player.level)
        return player  
    
    def simulate_round(self):
        """Simulate a complete game round (combat + buy phase)"""
        player = self.players[0]
        
        # Combat Phase
        combat_log = self.combat_system.simulate_combat()
        
        # Buy Phase
        print("\n=== Buy Phase ===")
        player.get_xp()
        player.round_end_gold()
        
        # Roll new shop
        self.shop_engine.roll_shop(player.level)
        
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