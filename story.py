import random as r
import time
from hero import  Hero
from actions import *

availableClasses = ["strategic", "courageous", "sneaky"] # known as a list or an array
bag = []
spells = 3
sneakAttacks = 3

def intro(player: Hero):
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
        spells = 5
    elif player.getchClass() == "courageous":
        player.setDamage(5)
        player.setSneakAttacks(2)
        print("You have a bonus to damage, but have less sneak attacks")
        sneakAttacks = 2
    else:
        player.setSneakAttacks(5)
        player.setSpellSlots(2)
        print("You have bonus to sneak attacks, but have less spell slots")
        spells = 2
        sneakAttacks = 5
    

    time.sleep(3)

    print("Welcome to the land of Aezwolth! Our adventure starts off at your home village.")
    time.sleep(3)
    print("Your mother has requested your help with dinner. You are tasked to find a rabbit for her to cook.")

    time.sleep(4)

# Starter Quest: chase rabbits
def starterquest(player: Hero):
    enemyHP = 4
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
            useItem(bag, player)
        heroInput = ""
        print(f"The enemy has {enemyHP} hp.")

    print("After defeating the rabbit, you find a rusty sword in the forest")
    time.sleep(1)

    player.setSpellSlots(spells)
    player.setSneakAttacks(sneakAttacks)
    print("Congrats! Enemy defeated. You have received a rusty blade (plus one to damage), 5 apples, a stick (to yeet at enemy)")
    player.setBoost(1)
    bag.append("stick")
    for x in range(5):
        bag.append("apple")
    print(bag)
    player.attackTypes[0] = "rusty blade"

# Once complete, your village is attacked by monsters
def firstMonster(player: Hero):
    print("You return to your house to find your house in ruins!")
    print("A goblin caught you from the behind by suprise!")

    time.sleep(3)

    print_ascii_art("goblin.txt")
    print(f"You have encountered a goblin! They have 20 hp. What do you want to do?")
    encounter(20, 15, player, bag)

    time.sleep(1)
    print("The rest of goblins have left already, thankfully.")
    time.sleep(1)
    print("You decide to get revenge on the goblins and get ready.")
    time.sleep(1)
    print(f"{player.getName()}, it sounds like a good idea to head for a village.")
    time.sleep(1)
    print("After a day of walking, you find a small village.")
    time.sleep(1)
    print("You decide to enter.") 
    time.sleep(1)
    print("You find that villagers from your town made it to here.")
    time.sleep(1)
    print("You ask about your parents.")
    time.sleep(1)
    print("You're told no one has seen them since the attack...")
    time.sleep(3)
    print("Your best friend Tamone steps up and says he'll help you by supplying gear.")
    time.sleep(2)
    print("Store unlocked! Tamone's Armory.")
    time.sleep(1)
    print("Tamone gives you two options for free.")
    heroInput = input("Copper Sword or Wooden Shield? ").lower().strip()
    if heroInput == "copper sword":
        player.setBoost(2)
        print("You now have a boost of 2!")
    if heroInput == "wooden shield":
        player.setHP(30)
        print("Your hp is now 30!")

#Nolan add the storyline here
def secondQuest(player: Hero):
    print("Nolan add content here")