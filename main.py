import random as r
import time
from hero import  Hero

availableClasses = ["strategic", "courageous", "sneaky"] # known as a list or an array
moves = ["attack", "run", "use item"]
enemyHP = 4
bag = []

player = Hero("Gen", "Player", 3, 3, 3, 5, 6, 0)

def print_ascii_art(fn):
    f = open(fn, 'r')
    print( ''.join([line for line in f]))

def useItem():
    if len(bag) == 0:
        print("You have no items. :(")
    else:
        item = input(f"Pick an item {bag} ").lower().strip()
        print(f"You used {item}")
        bag.remove(item)

def encounter(eHP):
    hInput = ''
    heroHP = player.getHP()
    while eHP > 0 and heroHP > 0:
        while (hInput in moves) == False:
            hInput = input(f"Choose an action: {moves} ")
        print(f"You have chosen to {hInput}")
        if hInput == "attack":
            enemyDamaged = player.attack()
            eHP = eHP - enemyDamaged
        if hInput  == "run":
            if player.run():
                print("Successfully ran away!")
                break
            else:
                print("Running has failed!")
        if hInput  == "use item":
            useItem()
        hInput = ""
        print(f"The enemy has {eHP} hp.")

player.setName(input("Hello adventurer! What is your name? ").strip())
print(f"Hello {player.getName()}!")
time.sleep(3)

while (player.getchClass() in availableClasses) == False:
    characterClass = input("What kind of hero are you? [Strategic, Courageous, Sneaky] ").lower().strip()
    player.setchClass(characterClass)

print(f"You are a {player.getchClass()} hero! That means you have the following attributes:")
if player.getchClass() == "strategic":
    player.setSpellSlots(5)
    player.setDamage(2)
    print("You have bonus to spells, but do less physical damage")
elif player.getchClass() == "courageous":
    player.setDamage(5)
    player.setSneakAttacks(2)
    print("You have a bonus to damage, but have less sneak attacks")
else:
    player.setSneakAttacks(5)
    player.setSpellSlots(2)
    print("You have bonus to sneak attacks, but have less spell slots")

time.sleep(3)

print("Welcome to the land of Aezwolth! Our adventure starts off at your home village.")
time.sleep(3)
print("Your mother has requested your help with dinner. You are tasked to find a rabbit for her to cook.")

time.sleep(4)

# Starter Quest: chase rabbits
print_ascii_art('rabbit.txt')
print(f"You have encountered a rabbit! They have {enemyHP} hp. What do you want to do?")
heroInput = ""
while enemyHP > 0:
    while (heroInput in moves) == False:
        heroInput = input(f"Choose an action: {moves} ")
    print(f"You have chosen to {heroInput}")
    if heroInput == "attack":
        enemyDamaged = player.attack()
        enemyHP = enemyHP - enemyDamaged
    if heroInput  == "run":
        print("No running for tutorial quest")
    if heroInput  == "use item":
        useItem()
    heroInput = ""
    print(f"The enemy has {enemyHP} hp.")

print("Congrats! Enemy defeated. You have received a rusty blade (plus one to damage), 5 apples, a stick (to yeet at enemy)")
player.setBoost(1)
bag.append("stick")
for x in range(5):
    bag.append("apple")
print(bag)
player.attackTypes[0] = "rusty blade"

# Once complete, your village is attacked by monsters

print("You return to your house to find your house in ruins and blood soaking out from under the door.")
print("A goblin cuaght you from the behind by suprise!")

print(f"You have encountered a goblin! They have 20 hp. What do you want to do?")
encounter(20)

print("Congrats! Enemy defeated.")