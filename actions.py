import random as r

moves = ["attack", "run", "use item"]

def enemyAttack(eHP):
    damage = r.randint(0, int(eHP/5))
    return damage 

def print_ascii_art(fn):
    f = open(fn, 'r')
    print( ''.join([line for line in f]))

def useItem(bag, player):
    if len(bag) == 0:
        print("You have no items. :(")
    else:
        item = input(f"Pick an item {bag} ").lower().strip()
        print(f"You used {item}")
        if item == "apple":
            player.heal(5)
            print("You have healed for 5 hp!")
        bag.remove(item)

def encounter(eHP, coinValue, player, bag):
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
            useItem(bag, player)
        hInput = ""
        print(f"The enemy has {eHP} hp.")

        enemyDamage = enemyAttack(eHP)
        player.takeDamage(enemyDamage)
        print(f"The enemy has done {enemyDamage} damage")

        heroHP = player.getHP()
        print(f"You have {heroHP} hp")
    if eHP == 0:
        print(f"Congrats! You have defeated the enemy!")
        print(f"You have earned {coinValue} coins")
        player.earnCoin(coinValue)
    if heroHP == 0:
        print(f"Oh no! You've lost the battle.")