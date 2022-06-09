import random as r
import time
from hero import  Hero
from story import starterquest, intro, firstMonster

player = Hero("Gen", "Player", 3, 3, 3, 5, 6, 0)

if __name__ == "__main__":
    intro(player)
    starterquest(player)
    firstMonster(player)
