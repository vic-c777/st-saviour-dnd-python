import random
from draw import draw_d20, draw_d4

class Player:
   def __init__(self, name: str, role: str, strength: int):
      self.name = name
      self.role = role 
      self.strength = strength
      self.hp = 100
  
   def roll_d20(self) -> int: 
       roll = random.randint(1, 20)
       draw_d20(roll)
