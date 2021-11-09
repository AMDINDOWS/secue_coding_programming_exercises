import random

#player class

class Iron_Man (object):
    health = 99
    strength = 98
    defence = 97
    Time_travel = 96

class Captain_America (object):
    health = 89
    strength = 88
    defence = 87
    Time_travel = 86

class Thor (object):
    health = 95
    strength = 94
    defence = 93
    Time_travel = 92

#monster class

class Red_Skull (object):
    name = "Red_Skull"
    health = 20
    strength = 2
    defence = 2
    loot = random.randint(0,3)

class Loki (object):
    name = "Loki"
    health = 10
    strength = 1
    defence = 3
    loot = random.randint(0,3)

class Doctor_Doom (object):
    name = "Doctor_Doom"
    health = 30
    strength = 5
    defence = 1.5
    loot = random.randint(0,3)

class Thanos(object):
    name = "Thanos"
    health = 100
    strength = 10
    defence = 100
    loot = random.randint(0,3)


def gameOver(character, score):
    if character.health < 1:
        print("")
        print("SNAP")
        print("")
        print("Thanos snapped his fingers while using the Infinity Gauntlet")
        print("Thanos erased half of the population of the universe.....")
        print("")
        print("Whatever it takes...", score)
        exit()

def heroselect():
    print ("Select your hero!")
    selection = input("1. Iron_Man \n2. Captain_America \n3. Thor \n")
    if selection == "1":
        character = Iron_Man
        print ("You have selected the Iron_Man...These are their stats...")
        print ("Health - ", character.health)
        print ("Strength - ", character.strength)
        print ("Defence - ", character.defence)
        print ("Time_travel - ", character.Time_travel)
        return character

    elif selection == "2":
        character = Captain_America
        print ("You have selected the Captain_America...These are their stats...")
        print ("Health - ", character.health)
        print ("Strength - ", character.strength)
        print ("Defence - ", character.defence)
        print ("Time_travel - ", character.Time_travel)
        return character

    elif selection == "3":
        character = Thor
        print ("You have selected the Thor...These are their stats...")
        print ("Health - ", character.health)
        print ("Strength - ", character.strength)
        print ("Defence - ", character.defence)
        print ("Time_travel - ", character.Time_travel)
        return character

    else:
        print("Only press 1, 2 or 3")
        heroselect()

def enemyselect(Red_Skull,Loki,Doctor_Doom,Thanos):
    enemyList = [Red_Skull,Loki,Doctor_Doom,Thanos]
    chance = random.randint(0,3)
    enemy = enemyList[chance]
    return enemy

def loot():
    loot = ["The_Space_Stone(blue)", "The_Reality_Stone(red)", "The_Power_Stone(purple)" ,
              "The_Mind_Stone(yellow)","The_Time_Stone(green)","The_Soul_Stone(orange)"]
    lootChance = random.randint(0,5)
    lootDrop = loot[lootChance]
    return lootDrop

def lootEffect(lootDrop, character):
    if lootDrop == "The_Space_Stone(blue)" or "The_Mind_Stone(yellow)":
        character.health = character.health + 20
        print ("you took the The_Space_Stone(blue), increasing your health by 20!")
        print ("Your health is now", character.health)
        return character

    elif lootDrop == "The_Reality_Stone(red)" or "The_Time_Stone(green)":
        character.strength = character.strength + 2
        print ("you took your The_Reality_Stone(red) for the newer, much sharper one!")
        print ("Your strength has been increased by 2")
        print ("your new strength is now", character.strength)
        return character

    elif lootDrop == "The_Power_Stone(purple)" or "The_Soul_Stone(orange)":
        character.defence = character.defence + 2
        print ("you swap your The_Power_Stone(purple) for the newer, much stronger one!")
        print ("Your defence has been increased by 2")
        print ("your new strength is now", character.defence)
        return character
 
def battlestate(score):
    enemy = enemyselect(Red_Skull,Loki,Doctor_Doom,Thanos)
    print(enemy.name, "has appeared!")
    print ("you have 3 options...")
    while enemy.health > 0 :
        choice = input("1. The_Infinity_Gauntlet\n2. Time_travel \n3. RUN! \n")

        if choice == "1":
            print ("You have SNAP your The_Infinity_Gauntlet, attacking the", enemy.name)
            hitchance = random.randint(0,10)
            if hitchance > 3:
                enemy.health = enemy.health - character.strength
                print ("You hit the enemy, their health is now....", enemy.health)

                if enemy.health > 1:
                    character.health = character.health - (enemy.strength / character.defence)
                    print ("The", enemy.name, "takes a swing, it hits you leaving", character.health)
                    gameOver(character, score)
                    

                else:
                    if enemy.name == "Red_Skull":
                        enemy.health = 20
                        score = score + 10
                        

                    elif enemy.name == "Loki":
                        enemy.health = 10
                        score = score + 5
                        

                    elif enemy.name == "Doctor_Doom":
                        enemy.health = 30
                        score = score + 15
                    
                    elif enemy.name == "Thanos":
                        enemy.health = 100
                        score = score + 100

                    print ("You have defeated the", enemy.name)
                    print ("looks like it dropped something!")
                    lootDrop = loot()
                    print ("you got a", lootDrop)
                    lootEffect(lootDrop, character)
                    return score
                    break
            else:
                print("Your The_Infinity_Gauntlet slips from your grasp, you fumble and miss!")
                print("The", enemy.name, "hits you for full damage")
                character.health = character.health - enemy.strength
                print("You now only have", character.health, "remaining")
                gameOver(character, score)


        elif choice == "2":
            print ("You have Time travelled, attacking the", enemy.name)
            hitchance = random.randint(0,10)
            if hitchance > 3:
                enemy.health = enemy.health - character.Time_travel
                print ("You hit the", enemy.name, "their health is now....", enemy.health)

                if enemy.health > 0:
                    character.health = character.health - (enemy.strength / character.defence)
                    print ("The", enemy.name, "takes a swing, it hits you leaving", character.health)
                    gameOver(character, score)

                else:
                    if enemy.name == "Red_Skull":
                        enemy.health = 20
                        score = score + 10
                        

                    elif enemy.name == "Loki":
                        enemy.health = 10
                        score = score + 5
                        

                    elif enemy.name == "Doctor_Doom":
                        enemy.health = 30
                        score = score + 15
                    
                    elif enemy.name == "Thanos":
                        enemy.health = 100
                        score = score + 100
                        

                    print ("You have defeated the", enemy.name)
                    print ("looks like it dropped something!")
                    lootDrop = loot()
                    print ("you got a", lootDrop)
                    lootEffect(lootDrop, character)
                    return score
                    break
            else:
                print("You slip when casting your spell, you fumble and miss!")
                print("The", enemy.name, "hits you for full damage")
                character.health = character.health - enemy.strength
                print("You now only have", character.health, "remaining")
                gameOver(character, score)


        elif choice == "3":
            print("you try to run....")
            runchance = random.randint(1,10)
            if runchance > 4:
                print ("you got away unscratched!")
                break
            else:
                print ("You try to run but slip and fall")
                print ("You try to defend but cannot, the enemy hits you for full damage...")
                character.health = character.health - enemy.strength
                print ("Your health is now", character.health)
                gameOver(character, score)

        else:
            print ("number not allowed, please only type 1, 2 or 3...")
       

def Thanosbattlestate(score):
    enemy = Thanos

score = 0
character = heroselect()
score = battlestate(score)
print(score)
score = battlestate(score)
print(score)
score = battlestate(score)
print (score)
score = battlestate(score)
print(score)
print("")
print("I AM IRONMAN")
print("")
print("SNAP!")
print("")
print("You have Saved The World")
print("I love you 3000...")
