import random as r

class Hero:

    def __init__(self, name: str, chClass: str, spellSlots: int,  sneakAttacks: int, damage: int, spellDamage: int, sneakDamage: int, boost: int):
        self.name = name
        self.chClass = chClass
        self.hp = 25
        self.spellSlots = spellSlots
        self.sneakAttacks = sneakAttacks
        self.damage  = damage
        self.spellDamage = spellDamage
        self.sneakDamage = sneakDamage
        self.boost = boost
        self.attackTypes = ["stick", "spell", "sneak"]
        self.coin = 100

    #getters for each field
    def getName(self):
        return self.name

    def getchClass(self):
        return self.chClass

    def getHP(self):
        return self.hp

    def getSpellSlots(self):
        return self.spellSlots

    def getSneakAttacks(self):
        return self.sneakAttacks
    
    def getDamage(self):
        return self.damage

    def getSpellDamage(self):
        return self.spellDamage
    
    def getSneakDamage(self):
        return self.sneakDamage

    def getBoost(self):
        return self.boost
    
    def getAttackTypes(self):
        return self.attackTypes

    #setters for method
    def setName(self, n):
        self.name = n

    def setchClass(self, c):
        self.chClass = c

    def setSpellSlots(self, s):
        self.spellSlots = s

    def setSneakAttacks(self, s):
        self.sneakAttacks
    
    def setDamage(self, s):
        self.damage = s

    def setSpellDamage(self, s):
        self.spellDamage = s
    
    def setSneakDamage(self, s):
        self.sneakDamage = s

    def setBoost(self, s):
        self.boost = s

    def setHP(self, s):
        self.hp = s

    def takeDamage(self, damage):
        self.hp = self.hp - damage

    def heal(self, heal):
        self.hp = self.hp + heal

    def attack(self):
        attackInput = input(f"Choose type of attack: {self.attackTypes} ")
        enemyDamaged = 0
        if attackInput == self.attackTypes[0]:
            enemyDamaged = r.randint(1, self.damage) + self.boost
            print(f"You used {self.attackTypes[0]}. It does {enemyDamaged} damage.")
        elif attackInput == self.attackTypes[1] and self.spellSlots > 0:
            enemyDamaged = r.randint(0, self.spellDamage)
            print(f"You used {self.attackTypes[1]}. It does {enemyDamaged} damage.")
            self.spellSlots = self.spellSlots - 1
            print(f"You have {self.spellSlots} spells left")
        elif attackInput == self.attackTypes[2] and self.sneakAttacks > 0:
            enemyDamaged = r.randint(0, self.sneakDamage)
            print(f"You used {self.attackTypes[2]}. It does {enemyDamaged} damage.")
            self.sneakAttacks = self.sneakAttacks - 1
            print(f"You have {self.sneakAttacks} sneak attacks left")
        return enemyDamaged

    def run(self):
        return r.randint(1,3) == 3

    def getCoin(self):
        return self.coin

    def earnCoin(self, x: int):
        self.coin + x

    def buyItem(self, price: int, item: str):
        self.bag.add(item)
        self.coin - price
    
    def buyEquipment(self, price: int):
        self.coin - price
