import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from engine.game_engine import GameEngine
from heroes.Terran import Terran
from heroes.Craig import Craig
from heroes.Rillan import Rillan
from heroes.Charion import Charion
from engine.combat_system import CombatSystem
from player import Player

def print_shop_state(shop_slots):
    """Helper to print current shop state"""
    print("\n=== Shop State ===")
    for i, slot in enumerate(shop_slots):
        if not slot.purchased:
            print(f"Slot {i}: {slot.hero_type.__name__} (Cost: {slot.cost})")
        else:
            print(f"Slot {i}: [Purchased]")

def print_player_state(player, player_num):
    """Helper to print player state"""
    print(f"\n=== Player {player_num} State ===")
    print(f"Gold: {player.gold}")
    print(f"Level: {player.level}")
    print(f"HP: {player.health}")
    print(f"XP: {player.experience}/{player.level_up_table[player.level]}")
    
    print("\nBoard:")
    for hero in player.board:
        print(f"- {hero.name}: HP={hero.hp}/{hero.max_hp}, Mana={hero.mana}/{hero.max_mana}")
    
    print("\nBench:")
    for hero in player.bench:
        print(f"- {hero.name}: HP={hero.hp}/{hero.max_hp}, Mana={hero.mana}/{hero.max_mana}")

def simulate_buy_phase(player, shop_engine):
    """Simulate player buying decisions"""
    shop_slots = shop_engine.roll_shop(player.level)
    print_shop_state(shop_slots)
    
    for i, slot in enumerate(shop_slots):
        if (not slot.purchased and 
            player.gold >= slot.cost and 
            (len(player.board) + len(player.bench) < player.level + 5)):
            
            hero_type = shop_engine.purchase_hero(i)
            if hero_type:
                hero = hero_type(f"{hero_type.__name__}_{i}")
                player.add_hero(hero, to_bench=(len(player.board) >= player.level))
                player.gold -= slot.cost
                print(f"Purchased {hero.name} for {slot.cost} gold")

def main():
    # Initialize game
    game = GameEngine()
    game.players.clear()  # Clear any existing players
    
    # Create player 1
    player1 = Player(hero=None, ai=None)
    player1.gold = 10
    player1.add_hero(Craig("P1_Craig1"), to_bench=False)
    game.players.append(player1)
    
    # Create player 2
    player2 = Player(hero=None, ai=None)
    player2.gold = 10
    player2.add_hero(Terran("P2_Terran1"), to_bench=False)
    game.players.append(player2)
    
    # Initialize combat system
    game.combat_system = CombatSystem(player1, player2)
    
    # Print initial state
    print(f"\n=== Round {game.round} ===")
    print("\nPlayer 1                                    Player 2")
    print("--------                                    --------")
    print(f"Gold: {player1.gold:<39} Gold: {player2.gold}")
    print(f"Level: {player1.level:<38} Level: {player2.level}")
    print(f"HP: {player1.health:<40} HP: {player2.health}")
    
    print("\nBoard:                                     Board:")
    for i in range(max(len(player1.board), len(player2.board))):
        p1_hero = f"- {player1.board[i].get_status_string()}" if i < len(player1.board) else ""
        p2_hero = f"- {player2.board[i].get_status_string()}" if i < len(player2.board) else ""
        print(f"{p1_hero:<40} {p2_hero}")
    
    print("\nBench:                                     Bench:")
    for i in range(max(len(player1.bench), len(player2.bench))):
        p1_hero = f"- {player1.bench[i].get_status_string()}" if i < len(player1.bench) else ""
        p2_hero = f"- {player2.bench[i].get_status_string()}" if i < len(player2.bench) else ""
        print(f"{p1_hero:<40} {p2_hero}")
    
    # Run game phases
    print("\n=== Buy Phase ===")
    print("\nPlayer 1's turn:")
    game.process_shop_phase()
    
    # Process combat phase
    print("\n=== Combat Phase ===")
    result = game.combat_system.simulate_combat()
    print(result["log"])
    
    # Process round end and print final state
    game.process_round_end()
    print(f"\n=== Round {game.round} ===")
    
    print("\nPlayer 1                                    Player 2")
    print("--------                                    --------")
    print(f"Gold: {player1.gold:<39} Gold: {player2.gold}")
    print(f"Level: {player1.level:<38} Level: {player2.level}")
    print(f"HP: {player1.health:<40} HP: {player2.health}")
    
    print("\nBoard:                                     Board:")
    for i in range(max(len(player1.board), len(player2.board))):
        p1_hero = f"- {player1.board[i].get_status_string()}" if i < len(player1.board) else ""
        p2_hero = f"- {player2.board[i].get_status_string()}" if i < len(player2.board) else ""
        print(f"{p1_hero:<40} {p2_hero}")
    
    print("\nBench:                                     Bench:")
    for i in range(max(len(player1.bench), len(player2.bench))):
        p1_hero = f"- {player1.bench[i].get_status_string()}" if i < len(player1.bench) else ""
        p2_hero = f"- {player2.bench[i].get_status_string()}" if i < len(player2.bench) else ""
        print(f"{p1_hero:<40} {p2_hero}")

if __name__ == "__main__":
    main() 