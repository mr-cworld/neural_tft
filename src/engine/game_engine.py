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
        # Initialize player with None for both hero and AI
        player = Player(hero=None, ai=None)  # Explicitly pass required arguments
        self.players.append(player)
        self.combat_system = CombatSystem(player)
        return player
        
    def run_round(self):
        """Run a single round of combat"""
        print("\n=== Combat Phase ===")
        
        if len(self.players) > 1:
            # Run combat between players
            combat_result = self.combat_system.simulate_combat()  # Changed back to simulate_combat
            print(combat_result["log"])
            
            # Debug print
            print("\nPost-combat state:")
            for i, player in enumerate(self.players, 1):
                print(f"Player {i} board: {[h.name for h in player.board]}")
                print(f"Player {i} HP: {player.health}")
            
            # Determine winner/loser based on the combat result
            winner = self.players[0] if combat_result["winner"] == "player1" else self.players[1]
            loser = self.players[1] if combat_result["winner"] == "player1" else self.players[0]
            
            # Update win streaks and apply damage
            winner.win_round()
            loser.lose_round()
            
            # Apply damage to loser (scale with rounds)
            damage = 2 + self.round
            damage_result = loser.take_damage(damage)
            print(f"\nCombat Result: {winner.__class__.__name__} wins! {loser.__class__.__name__} {damage_result}")
        
        # Buy Phase
        print("\n=== Buy Phase ===")
        for player in self.players:
            player.get_xp()
            self.shop_engine.roll_shop(player.level)
        
        self.round += 1
    
    def get_game_state(self):
        """Return current game state in a formatted string"""
        output = []
        output.append(f"\n=== Round {self.round} ===")
        
        # Format player states side by side
        output.append("\nPlayer 1                                    Player 2")
        output.append("--------                                    --------")
        
        # Get both players' states
        p1 = self.players[0]
        p2 = self.players[1] if len(self.players) > 1 else None
        
        # Basic stats
        output.append(f"Gold: {p1.gold:<37} Gold: {p2.gold if p2 else 'N/A'}")
        output.append(f"Level: {p1.level:<36} Level: {p2.level if p2 else 'N/A'}")
        output.append(f"HP: {p1.health:<38} HP: {p2.health if p2 else 'N/A'}")
        
        # Board state
        output.append("\nBoard:                                     Board:")
        p1_board = [f"- {h.name}: HP={h.hp}/{h.max_hp}, Mana={h.mana}/{h.max_mana}" for h in p1.board]
        p2_board = [f"- {h.name}: HP={h.hp}/{h.max_hp}, Mana={h.mana}/{h.max_mana}" for h in p2.board] if p2 else []
        
        # Align board states
        max_board = max(len(p1_board), len(p2_board))
        for i in range(max_board):
            left = p1_board[i] if i < len(p1_board) else ""
            right = p2_board[i] if i < len(p2_board) else ""
            output.append(f"{left:<40} {right}")
            
        # Bench state
        output.append("\nBench:                                     Bench:")
        p1_bench = [f"- {h.name}: HP={h.hp}/{h.max_hp}, Mana={h.mana}/{h.max_mana}" for h in p1.bench]
        p2_bench = [f"- {h.name}: HP={h.hp}/{h.max_hp}, Mana={h.mana}/{h.max_mana}" for h in p2.bench] if p2 else []
        
        # Align bench states
        max_bench = max(len(p1_bench), len(p2_bench))
        for i in range(max_bench):
            left = p1_bench[i] if i < len(p1_bench) else ""
            right = p2_bench[i] if i < len(p2_bench) else ""
            output.append(f"{left:<40} {right}")
            
        return "\n".join(output)
    
    def add_player(self):
        """Add a second player to the game"""
        # Initialize second player with None for both hero and AI
        player = Player(hero=None, ai=None)  # Explicitly pass required arguments
        self.players.append(player)
        self.combat_system = CombatSystem(self.players[0], self.players[1])
        return player 