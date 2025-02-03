from typing import List, Optional
from player import Player
from heroes.Terran import Terran
from heroes.Craig import Craig
from engine.combat_system import CombatSystem
from engine.shop_engine import ShopEngine
import random

class GameEngine:
    def __init__(self):
        self.round = 1
        self.players: List[Player] = []
        self.main_player: Optional[Player] = None  # Track main player separately
        self.combat_system = None
        self.shop_engine = ShopEngine()
        
        # Register all hero types with the shop
        self._register_heroes()
    
    def _register_heroes(self):
        """Register all available heroes with the shop engine"""
        # You'll need to import all hero classes and register them here
        self.shop_engine.register_hero(Terran, 1)
        self.shop_engine.register_hero(Craig, 1)
        # ... register other heroes ...
    
    def initialize_game(self):
        """Initialize a new game with main player and 7 AI opponents"""
        # Clear any existing players first
        self.players.clear()
        
        # Create main player (player1)
        self.main_player = Player(hero=None, ai=None)
        self.main_player.gold = 10
        self.main_player.is_main_player = True  # Add flag to identify main player
        self.players.append(self.main_player)
        
        # Create 7 AI opponents
        for i in range(7):
            ai_player = Player(hero=None, ai=f"ai_version_{i}")  # You can customize AI versions
            ai_player.gold = 10
            ai_player.is_main_player = False
            self.players.append(ai_player)
        
        # Initialize combat system with first two players for initial setup
        if len(self.players) >= 2:
            self.combat_system = CombatSystem(self.players[0], self.players[1])
        return self.main_player

    def process_combat_phase(self):
        """Process the combat phase and apply results"""
        print("\n=== Combat Phase ===")
        
        # For 1v1 test, just use the first two players
        if len(self.players) >= 2:
            player1, player2 = self.players[0], self.players[1]
            
            # Create combat system for these two players
            combat_system = CombatSystem(player1, player2)
            result = combat_system.simulate_combat()
            
            # Apply combat results
            if result["winner"] == "player1":
                player1.win_round()
                player2.lose_round()
            else:
                player2.win_round()
                player1.lose_round()
                
            print(result["log"])
            return result
        return None

    def process_round_end(self):
        """Process end of round updates"""
        # Give base gold to all players
        for player in self.players:
            player.gold += 5  # Base gold per round
            
            # Interest gold (every 10 gold = +1)
            interest = min(player.gold // 10, 5)
            player.gold += interest
            
            # Win/loss streak gold would be handled here
            
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
        """Add a player to the game (up to 8 players), this method is for manual testing, the game adds 8 when initialized. never use both"""
        # Clear existing players if any
        self.players.clear()
        self.main_player = None
        
        # Add the new player
        player = Player(hero=None, ai=None)
        player.gold = 10  # Starting gold
        self.players.append(player)
        
        # Update combat system with single player for now
        self.combat_system = CombatSystem(player, None)  # Initialize with one player
        return player

    def process_shop_phase(self):
        """Process the shop phase for all players"""
        print("\n=== Buy Phase ===")
        
        for i, player in enumerate(self.players):
            print(f"\nPlayer {i + 1}'s turn:")
            shop_slots = self.shop_engine.roll_shop(player.level)
            
            # Print shop state for debugging
            print("\nShop offers:")
            for j, slot in enumerate(shop_slots):
                if not slot.purchased:
                    print(f"Slot {j}: {slot.hero_type.__name__} (Cost: {slot.cost})")
            
            # Simulate buying decisions
            for slot_index, slot in enumerate(shop_slots):
                if (not slot.purchased and 
                    player.gold >= slot.cost and 
                    (len(player.board) + len(player.bench) < player.level + 5)):
                    
                    hero_type = self.shop_engine.purchase_hero(slot_index)
                    if hero_type:
                        # Create hero with unique name for this player
                        hero = hero_type(f"P{i+1}_{hero_type.__name__}_{slot_index}")
                        # Add hero to the correct player's board/bench
                        should_bench = len(player.board) >= player.level
                        player.add_hero(hero, to_bench=should_bench)
                        player.gold -= slot.cost
                        print(f"Player {i+1} purchased {hero_type.__name__} for {slot.cost} gold {'(to bench)' if should_bench else ''}")

    def get_detailed_state(self) -> str:
        """Get detailed game state including all players"""
        output = []
        output.append(f"\n=== Round {self.round} State ===")
        
        for i, player in enumerate(self.players, 1):
            output.append(f"\nPlayer {i}:")
            output.append(player.get_state_string())
            
        return "\n".join(output)
        
    def simulate_combat_with_summary(self) -> dict:
        """Run combat and return both results and ability summary"""
        combat_result = self.combat_system.simulate_combat()
        ability_summary = self.combat_system.get_ability_cast_summary()
        
        return {
            "combat_log": combat_result["log"],
            "winner": combat_result["winner"],
            "ability_summary": ability_summary,
            "damage_dealt": combat_result.get("damage_dealt", 0)
        } 

    def process_round(self):
        """Process a complete round"""
        # Shop phase
        self.process_shop_phase()
        
        # Combat phase
        combat_results = self.process_combat_phase()
        
        # Round end updates
        self.process_round_end()
        
        return combat_results 

    def get_main_player_state(self):
        """Get detailed state for the main player"""
        if not self.main_player:
            return "No main player found"
            
        output = []
        output.append(f"\n=== Main Player Status (Round {self.round}) ===")
        output.append(f"Gold: {self.main_player.gold}")
        output.append(f"Level: {self.main_player.level}")
        output.append(f"HP: {self.main_player.health}")
        output.append("\nBoard:")
        for hero in self.main_player.board:
            output.append(f"- {hero.name}: HP={hero.hp}/{hero.max_hp}, Mana={hero.mana}/{h.max_mana}")
        output.append("\nBench:")
        for hero in self.main_player.bench:
            output.append(f"- {hero.name}: HP={hero.hp}/{hero.max_hp}, Mana={hero.mana}/{h.max_mana}")
        
        return "\n".join(output) 