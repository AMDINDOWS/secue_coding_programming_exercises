import random

class Item:
    def __init__(self):
        self.intr_choice = ''
    def interact(self, intr_choice):
        self.intr_choice = intr_choice
        if self.intr_choice == 'look':
            print("There is a sword. Try to pick it up it")
        else:
            print("You chose to run!")

class Monster:
    def __init__(self):
        #self.monster = ["Pikachhu", "Dracula", "Godzilla"]
        self.monster_choice = ''
    def __str__(self):
        monster = ["Pikachhu", "Dracula", "Godzilla"]
        monster_choice = random.choice(monster)
        return monster_choice
        #print(f"You have encountered the Monster {monster_choice}")

class Player:
        def __init__(self, name):
            self.name = name
            #self.monster = ''
            self.inventory = {"has_sword" : False, "health_potion" : 5, }
            self.player_stats = {
                "num_lives" : 5,
                "strength" : 0,
                "intelligence" : 0,
            }
            self.movement_actions = {
                "left",
                "right",
                "forward",
                "backward"
            }
            self.interact_actions_ld = {
                "look",
                "pickup", }
            self.interact_actions_rd = {
                "attack",
                "run"
            }
            self.eating_actions = {"eat", "drink"}

            
            print(f"Hello {self.name} Welcome to 'Hunt for Mighty Dragon'!")
            print("There are 2 rooms - Left (ld) and Right (rd)")
            print("In the Left room, you can look for the sword")
            print("In the right room, you can attack the dragon or run away")

            def validate():
                choice = input("Enter your choice : ")
                return choice

            def pickup():
                print("You have the sword now!")

            def attack():
                #Monster()
                monster = Monster.__str__(self)
                print(f"You have encountered the Monster {monster}")
                print("Do you want to move in any order? Type yes or no")
                movechoice = validate()
                if movechoice == 'yes':
                    print(f"You can choose from {self.movement_actions}")
                    movement_choice = validate()
                    print(f"You have chose to move {movement_choice}")
                else:
                    print("Guess you are comfortable in your current position")
                print("You have defeated the Monster Dragon")

            no_of_lives = self.player_stats.get('num_lives')
            while no_of_lives > 0 and no_of_lives <=5:

                hp = self.inventory.get('health_potion')
                intel = self.player_stats.get('intelligence')
                intel = 0
                strong = self.player_stats.get('strength')
                strong = 0
                
                print("Do you want to play? Type yes or no")
                play_choice = validate()
                if play_choice not in ['yes', 'no']:
                    print("Type yes or no")
                    play_choice = validate()
                if play_choice == 'no':
                    break
                
                while play_choice == 'yes':
                    print("Which room do you want to enter?\n Type 'ld' for left door or 'rd' for right door")
                    door_choice = validate()
                
                    if door_choice not in ["ld", "rd"]:
                        print("typr rd or ld")
                        door_choice = validate()

                    if door_choice == 'ld':
                        print(f"Enter your action from the list {self.interact_actions_ld}")
                        intr_choice = validate() 
                        if intr_choice not in ["look", "pickup"]:
                            print("type look or pickup")
                            intr_choice = validate()     
                        if intr_choice == 'look':
                            eat_choice = input("While looking around, do you want to eat or drink anything? Type yes or no: ")
                            if eat_choice == 'yes':
                                print(f"Choose from {self.eating_actions}")
                                ec = validate()
                                if ec == 'eat':
                                    print("You have an apple! Enjoy.")
                                else:
                                    print("You have a milkshake! Enjoy")
                                strong += 1
                                print(f"Your strength level increased to {strong}")
                            else:
                                print(f"Your strength level is {strong}")
                                print("Go ahead and look")
                            Item.interact(self,intr_choice)
                        else:
                            pickup() 
                            self.inventory.update({'has_sword' : True})
                        continue        
                    else:
                        print(f"Enter your action from the list {self.interact_actions_rd}")
                        intr_choice = validate() 
                        if intr_choice not in ["attack", "run"]:
                            print("typr attack or run")
                            intr_choice = validate()
                        if intr_choice == 'attack':
                            if self.inventory.get('has_sword') == True:
                                print("Do you want to have health potion? Type yes or no :")
                                health_potion = validate()
                                if health_potion not in ['yes', 'no']:
                                    print("type yes or no")
                                    health_potion = validate()
                                if health_potion == 'yes':
                                    if hp > 0 and hp <= 5:
                                        hp -= 1
                                        print(f"No of health potions left is {hp}")
                                    else:
                                        print("You donot have suffient health potion")
                                attack()
                                intel += 1
                                print(f"Your intelligence level is {intel}")
                                break
                            else:
                                print("You donot have the sword! Do you want to attack still or run away")
                                print("Type fight or run")
                                no_sword = validate()
                                if no_sword == 'fight':
                                    print("Dragon ate you!")
                                    no_of_lives -= 1
                                    print(f"No of lives remaining : {no_of_lives}")
                                    break
                                else:
                                    Item.interact(self,no_sword)
                                    continue
                        else:
                            Item.interact(self,intr_choice)
                            continue
                

name = input("What is your name? : ")
player = Player(name)



