import sys
import os

# Add the src directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from engine.game_engine import GameEngine
from engine.combat_system import CombatSystem
from player import Player
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
    """This function is no longer needed as combat end is handled in CombatSystem"""
    return not player1.board or not player2.board

def print_cast_summary(combat_log: str):
    """Print a summary of ability casts from the combat log"""
    print("\n=== Ability Cast Summary ===")
    
    # Parse combat log to count casts
    cast_counts = {}  # Format: {(unit_name, ability_name): cast_count}
    
    for line in combat_log.split('\n'):
        if "uses" in line:  # Our format is "Player's UnitName uses AbilityName"
            parts = line.split('uses')
            if len(parts) == 2:
                unit_info = parts[0].strip().split("'s ")  # Split "Player's UnitName"
                if len(unit_info) == 2:
                    player_name = unit_info[0]
                    unit_name = unit_info[1]
                    ability_name = parts[1].split('and')[0].strip()  # Get ability name before "and"
                    key = (unit_name, player_name, ability_name)
                    cast_counts[key] = cast_counts.get(key, 0) + 1
    
    # Sort by cast count (descending) and print
    sorted_casts = sorted(cast_counts.items(), key=lambda x: x[1], reverse=True)
    
    if not sorted_casts:
        print("No abilities were cast during combat")
    else:
        print(f"{'Unit':<15} {'Player':<15} {'Ability':<20} {'Casts':<5}")
        print("-" * 55)
        for (unit, player, ability), casts in sorted_casts:
            print(f"{unit:<15} {player:<15} {ability:<20} {casts:<5}")

def main():
    # Initialize game with just 2 players for 1v1 test
    game = GameEngine()
    
    # Clear any existing players and add just our test players
    game.players.clear()
    
    # Create player 1 with Craig
    player1 = Player(hero=None, ai=None)
    player1.gold = 10
    player1.add_hero(Craig("Craig Fighter"), to_bench=False)
    game.players.append(player1)
    
    # Create player 2 with Terran
    player2 = Player(hero=None, ai=None)
    player2.gold = 10
    player2.add_hero(Terran("Terran Warrior"), to_bench=False)
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
    
    # Process shop phase
    game.process_shop_phase()
    
    # Process combat phase
    game.process_combat_phase()
    
    # Process round end
    game.process_round_end()
    
    # Print final state
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