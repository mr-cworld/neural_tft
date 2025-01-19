import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from engine.game_engine import GameEngine
from heroes.Terran import Terran
from heroes.Craig import Craig
from heroes.Rillan import Rillan
from heroes.Charion import Charion

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
    player1 = game.initialize_game()
    player2 = game.add_player()
    
    # Set initial state
    player1.gold = 10
    player2.gold = 10
    player1.health = 100
    player2.health = 100
    
    # Give each player a starting hero
    terran = Terran("Terran1")
    craig = Craig("Craig1")
    player1.add_hero(terran, to_bench=False)
    player2.add_hero(craig, to_bench=False)
    
    # Print initial state
    print(game.get_game_state())
    
    # Run game phases
    game.process_shop_phase()
    game.process_combat_phase()
    game.process_round_end()
    
    # Print final state
    print(game.get_game_state())

if __name__ == "__main__":
    main() 