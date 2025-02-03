from typing import Dict, List
from dataclasses import dataclass, field
import json
from datetime import datetime

@dataclass
class HeroCombatStats:
  name: str
  damage_delt: List[int] = field(default_factory=list)
  damage_taken: List[int] = field(default_factory=list)
  health_done: List[int] = field(default_factory=list)
  abilities_cast: List[float] = field(default_factory=list)
  attacks_done: List[float] = field(default_factory=list)

  def to_dict(self):
    return {
      "name": self.name,
      "damage_delt": self.damage_delt,
      "damage_taken": self.damage_taken,
      "health_done": self.health_done,
      "abilities_cast": self.abilities_cast,
      "attacks_done": self.attacks_done,
      "totals": {
        "damage_delt": sum(self.damage_delt),
        "damage_taken": sum(self.damage_taken),
        "health_done": sum(self.health_done),
        "abilities_cast": sum(self.abilities_cast),
        "attacks_done": sum(self.attacks_done)
      }
    }

@dataclass
class CombatRound:
  round_number: int
  actions: List[dict] = field(default_factory=list)
  hero_states: Dict[str, dict] = field(default_factory=dict)


class CombatLogger:
  def __init__(self):
    self.match_data = {
      "combats": [],  # List of complete combats
      "current_combat": {
        "rounds": [],  # List of rounds in current combat
        "winner": None
      }
    }
    self.hero_stats: Dict[str, HeroCombatStats] = {}

  def start_combat(self, player1, player2):
    """Start a new combat and snapshot initial state"""
    self.match_data["current_combat"] = {
      "rounds": [],
      "initial_state": {
        "player1": self._snapshot_player(player1),
        "player2": self._snapshot_player(player2)
      },
      "winner": None
    }

  def _snapshot_player(self, player):
    return {
      "name": player.__class__.__name__,
      "board": [(hero.name, hero.hp, hero.max_hp, hero.mana) for hero in player.board]
    }

  def record_ability_cast(self, hero_name: str, ability_name: str):
    """Record an ability cast for a hero"""
    if hero_name not in self.hero_stats:
        self.hero_stats[hero_name] = HeroCombatStats(hero_name)
    self.hero_stats[hero_name].abilities_cast.append(ability_name)

  def record_attack(self, hero_name: str, damage: float):
    """Record an attack for a hero"""
    if hero_name not in self.hero_stats:
        self.hero_stats[hero_name] = HeroCombatStats(hero_name)
    self.hero_stats[hero_name].attacks_done.append(damage)

