from typing import List, Dict
from dataclasses import dataclass
import random

@dataclass
class ShopSlot:
  hero_type: type
  cost: int
  purchased: bool = False

class ShopEngine:
  def __init__(self):
     # Pool of available champions per cost tier
        self.champion_pool: Dict[int, List[type]] = {
            1: [],  # 8 copies of each
            2: [],  # 8 copies of each
            3: [],  # 8 copies of each
            4: [],  # 7 copies of each
            5: []   # 5 copies of each
        }
        
        self.tier_odds: Dict[int, Dict[int, float]] = {
            # level: {cost: probability}
            1: {1: 1.0, 2: 0.0, 3: 0.0, 4: 0.0, 5: 0.0},
            2: {1: 0.8, 2: 0.2, 3: 0.0, 4: 0.0, 5: 0.0},
            3: {1: 0.75, 2: 0.25, 3: 0.0, 4: 0.0, 5: 0.0},
            4: {1: 0.55, 2: 0.30, 3: 0.15, 4: 0.0, 5: 0.0},
            5: {1: 0.45, 2: 0.33, 3: 0.20, 4: 0.02, 5: 0.0},
            6: {1: 0.25, 2: 0.40, 3: 0.30, 4: 0.05, 5: 0.0},
            7: {1: 0.19, 2: 0.30, 3: 0.35, 4: 0.15, 5: 0.01},
            8: {1: 0.15, 2: 0.25, 3: 0.35, 4: 0.20, 5: 0.05},
            9: {1: 0.10, 2: 0.15, 3: 0.35, 4: 0.30, 5: 0.10},
            10: {1: 0.05, 2: 0.08, 3: 0.24, 4: 0.35, 5: 0.28}
        }
        
        self.shop_slots: List[ShopSlot] = []
        self.SHOP_SIZE = 5

  def register_hero(self, hero_class: type, cost:int):
     """Register a hero type to the pool"""
     copies = 5 if cost == 5 else(7 if cost == 4 else 8)
     self.champion_pool[cost].extend([hero_class]*copies)

  def roll_shop (self, player_level:int) -> List[ShopSlot]:
     """Generate a new shop based on player level"""
     self.shop_slots.clear()
     for _ in range(self.SHOP_SIZE):
        # Determine cost tier based on level probabilities
        cost = random.choices(
            list(self.tier_odds[player_level].keys()),
            list(self.tier_odds[player_level].values())
        )[0]
        
        # Select random hero from that cost pool if available
        if self.champion_pool[cost]:
            hero_type = random.choice(self.champion_pool[cost])
            self.shop_slots.append(ShopSlot(hero_type=hero_type, cost=cost))
        else:
            # If pool is empty, try to find next available cost tier
            for alt_cost in range(cost, 0, -1):
                if self.champion_pool[alt_cost]:
                    hero_type = random.choice(self.champion_pool[alt_cost])
                    self.shop_slots.append(ShopSlot(hero_type=hero_type, cost=alt_cost))
                    break
     return self.shop_slots

  def purchase_hero(self, slot_index: int) -> type:
     """Purchase a hero from the shop"""
     if 0 <= slot_index < len(self.shop_slots):
        slot = self.shop_slots[slot_index]
        if not slot.purchased:
            # Remove one copy from the pool
            self.champion_pool[slot.cost].remove(slot.hero_type)
            slot.purchased = True
            return slot.hero_type
     return None

  def return_hero_to_pool(self, hero_type: type, cost: int):
     """Return a hero to the pool (when selling)"""
     self.champion_pool[cost].append(hero_type)
