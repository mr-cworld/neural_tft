import sys
import os

# Add the src directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from engine.game_engine import GameEngine
from heroes.Terran import Terran
from heroes.Craig import Craig

def print_player_state(player1, player2, round_num=None):
    """Helper function to print both players' states"""
    prefix = f"\n=== Players State{f' After Round {round_num}' if round_num else ''} ==="
    print(prefix)
    
    # Player 1 - Terran Player
    print(f"\nPlayer 1 (Terran Player):")
    print(f"Gold: {player1.gold}")
    print(f"Level: {player1.level}")
    print(f"XP: {player1.experience}/{player1.level_up_table[player1.level]}")
    print("\nBoard Heroes:")
    if player1.board:
        for hero in player1.board:
            print(f"- {hero.name}: HP={hero.hp}/{hero.max_hp}, Mana={hero.mana}/{hero.max_mana}")
    else:
        print("- Empty")
    
    print("\nBench Heroes:")
    if player1.bench:
        for hero in player1.bench:
            print(f"- {hero.name}: HP={hero.hp}/{hero.max_hp}, Mana={hero.mana}/{hero.max_mana}")
    else:
        print("- Empty")
        
    # Player 2 - Craig Player
    print(f"\nPlayer 2 (Craig Player):")
    print(f"Gold: {player2.gold}")
    print(f"Level: {player2.level}")
    print(f"XP: {player2.experience}/{player2.level_up_table[player2.level]}")
    print("\nBoard Heroes:")
    if player2.board:
        for hero in player2.board:
            print(f"- {hero.name}: HP={hero.hp}/{hero.max_hp}, Mana={hero.mana}/{hero.max_mana}")
    else:
        print("- Empty")
    
    print("\nBench Heroes:")
    if player2.bench:
        for hero in player2.bench:
            print(f"- {hero.name}: HP={hero.hp}/{hero.max_hp}, Mana={hero.mana}/{hero.max_mana}")
    else:
        print("- Empty")

def check_combat_end(player1, player2):
    """Check if combat should end"""
    if not player1.board or not player2.board:
        return True
    for hero in player1.board + player2.board:
        if hero.hp <= 0:
            return True
    return False

def main():
    # Initialize game
    game = GameEngine()
    terran_player = game.initialize_game()
    craig_player = game.add_player()
    
    # Create heroes for 1v1
    terran = Terran("Terran Warrior")
    craig = Craig("Craig Fighter")
    
    # Add heroes to players' boards (no bench this time)
    terran_player.add_hero(terran, to_bench=False)
    craig_player.add_hero(craig, to_bench=False)
    
    # Print initial state
    print("\n=== Combat Start ===")
    print_player_state(terran_player, craig_player)
    
    # Run combat simulation until one hero dies
    round_num = 1
    while True:
        print(f"\n=== Round {round_num} ===")
        combat_log = game.simulate_round()
        print("\nCombat Log:")
        print(combat_log)
        
        # Print state after round
        print_player_state(terran_player, craig_player, round_num)
        
        # Check if combat should end
        if check_combat_end(terran_player, craig_player):
            print("\n=== Combat End ===")
            # Determine winner
            if not craig_player.board or (craig_player.board and craig_player.board[0].hp <= 0):
                print("Terran Player Wins!")
            elif not terran_player.board or (terran_player.board and terran_player.board[0].hp <= 0):
                print("Craig Player Wins!")
            break
            
        round_num += 1

if __name__ == "__main__":
    main() 