#this file will do a status check on the heroes a player has and update hero stats for the next fight accordingly

# this file is to hold what each origin does

#Origins List - water fire earth air light dark
from typing import Dict, List


class Origin:
    """Base class for all Origins and Classes"""
    def __init__(self, name: str, description: str, levels: Dict[int, str]):
        self.name = name
        self.description = description
        self.levels = levels  # Example: {2: "Bonus Effect", 4: "Stronger Effect"}

    def get_bonus(self, count: int):
        """Return the highest applicable bonus based on count of heroes with this trait."""
        active_levels = [lvl for lvl in sorted(self.levels.keys()) if count >= lvl]
        return self.levels[max(active_levels)] if active_levels else None

# Define Origins
ORIGINS = {
    "Water": Origin("Water", "Increase mana regen for all water units.", {2: "1", 4: "2", 6 : "3", 7: "4"}),
    "Earth": Origin("Earth", "Units gain armor and magic resist.", {3: 0.1, 5: 0.2, 7: 0.3}),
    "Fire": Origin("Fire", "Units deal more damage. +STR and SPELL Damage", {2:6, 4:18, 7: 30}),
    "Wind": Origin("Wind", "Units gain agi.", {1:2, 2:5, 3:11, 4:23, 5:47, 6:95, 7:191}),
    "Light": Origin("Light", "Magic Resist + STR", {2:15, 4:30}),
    "Dark": Origin("Dark", "Amor + Spell Dmg", {2:15, 4:30}),
}

# Define Classes
CLASSES = {
    "Fighter": Origin("Fighter", "Increase STR.", {2:10, 4:20}),
    "Tank": Origin("Tank", "Increase Health of All Units", {2:300, 4:500}),
    "Mage": Origin("Mage", "Increase Spell Power", {2: 10, 4: 20}),
    "Support": Origin("Support", "Increase Armor", {2:.025, 4: 0.052}),
    "Ranger": Origin("Ranger", "Increased AGI percent HP", {2:.1, 4: .25}),
    "Brusier": Origin("Brusier", "Increases STR by percent HP", {2:.1, 4: .25}),
}
