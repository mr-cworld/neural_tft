This is a github repo to learn the gymnasium (formerly OpenAIGym) to create an autobattler, TFT-like game where agents make decisions and learn via Reinforcment Learning (RL)

Basic Rules:
Hero will be given gold / team slots as the game progresses

Origin List = ['Water', 'Fire','Air','Earth','Light','Dark']
Class List = ['Fighter','Tank', 'Mage', 'Support', 'Ranger', 'Brusier']



Game Structure:
The player can play up to the number of units active = to their level
The player has a bench of up to 5 other heroes to swap between
The player can always sell a hero back for 80% value

Based on the heros on the board (heroes=[]) the user calculates the Origins for both origin and classes, going through the list and then seeing the highest level the player is eligible for each origin trait, and then returing that value to a dictionary, then applying the benefit the appropriate units one buff at a time (first additive, then mulitplicative)

Each round works like This:
  Heros are sorted into attack order from highest agility to lowest
  Heroes attack one at a time
  If they die, they are removed from list
  Heroes always Target in order ['Tank','Bruiser','Fighter','Support','Mage']]
  If any units hit's max mana, they cast instantly
  The battle continues until someone wins
  The loser takes hp damage, the winner gains 1 gold immediately, and then see the list below for what to do
  At the end of the round see list below for what happens


Round Ends:
Player Gains 2 exp (player.get_xp())
Player gets Gold (player.round_end_gold())
The Player's Shop rerolls

Each Player has a shop of 5 available champions:
 List of Champion Cost = [1,2,3,4,5]
 *When the game is started a shop is created, which is in the following logic
List of Number of Each Champion [1:8, 2:8, 3:8, 4:7, 5:5], so 8 1 costs, 8 2 costs, etc
the player can buy any number of champions, or upgrade the champion based on their upgrade price if they have the gold


