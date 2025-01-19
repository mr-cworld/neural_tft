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
    print("\n=== Game Start ===")
    print_player_state(terran_player, craig_player)
    
    # Run a single complete combat (which includes multiple rounds of attacks)
    print("\n=== Combat Phase ===")
    combat_log = game.simulate_round()
    print("\nCombat Log:")
    print(combat_log)
    
    # Print cast summary
    print_cast_summary(combat_log)
    
    # Print final state
    print_player_state(terran_player, craig_player, "Combat End")
    
    # Determine winner
    if not craig_player.board:
        print("\nTerran Player Wins!")
    elif not terran_player.board:
        print("\nCraig Player Wins!")

if __name__ == "__main__":
    main() 