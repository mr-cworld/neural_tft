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
        
    def process_combat_phase(self):
        """Process the combat phase and apply results"""
        print("\n=== Combat Phase ===")
        combat_result = self.combat_system.simulate_combat()
        print(combat_result["log"])
        
        # Process round end - handle win/lose first
        print("\n=== Round End ===")
        if combat_result["winner"] == "player1":
            self.players[0].win_round()
            self.players[1].lose_round()
        else:
            self.players[1].win_round()
            self.players[0].lose_round()
        
        return combat_result

    def process_round_end(self):
        """Process end of round updates for all players"""
        for player in self.players:
            player.get_xp()
            player.round_end_gold()
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

    def process_shop_phase(self):
        """Process the shopping phase for all players"""
        print("\n=== Buy Phase ===")
        for i, player in enumerate(self.players, 1):
            print(f"\nPlayer {i}'s turn:")
            shop_slots = self.shop_engine.roll_shop(player.level)
            self._simulate_buy_phase(player, shop_slots)
    
    def _simulate_buy_phase(self, player, shop_slots):
        """Simulate buying decisions for a player"""
        for i, slot in enumerate(shop_slots):
            if (not slot.purchased and 
                player.gold >= slot.cost and 
                (len(player.board) + len(player.bench) < player.level + 5)):
                
                hero_type = self.shop_engine.purchase_hero(i)
                if hero_type:
                    hero = hero_type(f"{hero_type.__name__}_{i}")
                    player.add_hero(hero, to_bench=(len(player.board) >= player.level))
                    player.gold -= slot.cost
                    print(f"Purchased {hero.name} for {slot.cost} gold") 