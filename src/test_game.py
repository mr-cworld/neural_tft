from game_engine import GameEngine

def main():
    # Initialize game
    game = GameEngine()
    game.initialize_game()
    
    # Run for 3 rounds as a test
    for _ in range(3):
        print("\n=== Round Start ===")
        print(game.simulate_round())
        state = game.get_game_state()
        print("\nGame State:")
        print(f"Round: {state['round']}")
        print(f"Player Gold: {state['player_gold']}")
        print(f"Player Level: {state['player_level']}")
        print(f"Player Health: {state['player_health']}")
        print("\nHeroes:")
        for hero_name, hp, mana in state['heroes']:
            print(f"{hero_name}: HP={hp}, Mana={mana}")
        print("=== Round End ===\n")

if __name__ == "__main__":
    main() 