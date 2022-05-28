import random as r
import time

characterName = "Gen"
characterClass = "Player"
availableClasses = ["strategic", "courageous", "sneaky"] # known as a list or an array
spellSlot = 3
sneakAttacks = 3
damage = 3
spellDamage = 5
sneakDamage = 6
moves = ["attack", "run", "use item"]
attackTypes = ["stick", "spell", "sneak"]
enemyHP = 4
boost =  0
bag = []

def print_ascii_art(fn):
    f = open(fn, 'r')
    print( ''.join([line for line in f]))

def attack():
    attackInput = input(f"Choose type of attack: {attackTypes} ")
    enemyDamaged = 0
    if attackInput == attackTypes[0]:
        enemyDamaged = r.randint(0, damage) + boost
        print(f"You used {attackTypes[0]}. It does {enemyDamaged} damage.")
    elif attackInput == attackTypes[1]:
        enemyDamaged = r.randint(0, spellDamage)
        print(f"You used {attackTypes[1]}. It does {enemyDamaged} damage.")
    elif attackInput == attackTypes[2]:
        enemyDamaged = r.randint(0, sneakDamage)
        print(f"You used {attackTypes[2]}. It does {enemyDamaged} damage.")
    return enemyDamaged

def run():
    return r.randint(1,3) == 3

def useItem():
    if len(bag) == 0:
        print("You have no items. :(")
    else:
        item = input(f"Pick an item {bag} ").lower().strip()
        print(f"You used {item}")
        bag.remove(item)

def encounter(eHP):
    hInput = ''
    while eHP > 0:
        while (hInput in moves) == False:
            hInput = input(f"Choose an action: {moves} ")
        print(f"You have chosen to {heroInput}")
        if hInput == "attack":
            enemyDamaged = attack()
            eHP = eHP - enemyDamaged
        if hInput  == "run":
            if run():
                print("Successfully ran away!")
                break
            else:
                print("Running has failed!")
        if hInput  == "use item":
            useItem()
        hInput = ""
        print(f"The enemy has {eHP} hp.")

characterName = input("Hello adventurer! What is your name? ").strip()
print(f"Hello {characterName}!")
time.sleep(3)

while (characterClass in availableClasses) == False:
    characterClass = input("What kind of hero are you? [Strategic, Courageous, Sneaky] ").lower().strip()

print(f"You are a {characterClass} hero! That means you have the following attributes:")
if characterClass == "strategic":
    spellSlot = 5
    damage = 2
    print("You have bonus to spells, but do less physical damage")
elif characterClass == "courageous":
    damage = 5
    sneakAttacks = 2
    print("You have a bonus to damage, but have less sneak attacks")
else:
    sneakAttacks = 5
    spellSlots = 2
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
        enemyDamaged = attack()
        enemyHP = enemyHP - enemyDamaged
    if heroInput  == "run":
        print("No running for tutorial quest")
    if heroInput  == "use item":
        useItem()
    heroInput = ""
    print(f"The enemy has {enemyHP} hp.")

print("Congrats! Enemy defeated. You have received a rusty blade (plus one to damage), 5 apples, a stick (to yeet at enemy)")
boost = 1
bag.append("stick")
for x in range(5):
    bag.append("apple")
print(bag)
attackTypes[0] = "rusty blade"

print(f"You have encountered a rabbit! They have 20 hp. What do you want to do?")
encounter(20)

# Once complete, your village is attacked by monsters
