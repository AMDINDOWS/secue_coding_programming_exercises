# Build a CLI RPG game following the instructions from the course.
# Ask the player for their name.
# Display a message that greets them and introduces them to the game world.
# Present them with a choice between two doors.
# If they choose the left door, they'll see an empty room.
# If they choose the right door, then they encounter a dragon.
# In both cases, they have the option to return to the previous room or interact further.
# When in the seemingly empty room, they can choose to look around. If they do so, they will find a sword. They can choose to take it or leave it.
# When encountering the dragon, they have the choice to fight it.
# If they have the sword from the other room, then they will be able to defeat it and win the game.
# If they don't have the sword, then they will be eaten by the dragon and lose the game.
import random
class Item:
    def __init__(self, door_choice, intr_choice):
        self.door_choice = door_choice
        self.inventory = {"has_sword" : False, "health_potion" : 0, "mana_potion" : 0}
        #self.flag = 0
    def interact(self, door_choice, intr_choice):
        flag  = 0
        out_str = ''
        if intr_choice == 'look' and door_choice == 'ld':
            out_str = "There is a sword in the room"
            z = print(out_str)
            return z
        elif intr_choice == 'pickup' and door_choice == 'ld':
            a = self.inventory.update({'has_sword' : True})
            flag = 1
            out_str = "You have the sword"
            z = print(out_str)
            return a
        elif intr_choice == 'attack' and door_choice == 'rd':
            if flag == 1:
                out_str = "You can defeat the Dragon"
                z = print(out_str)
                return z
            else:
                out_str =  "You cannot defeat the Dragon since you donot have the sword"
                z = print(out_str)
                return z
        elif intr_choice == 'run' and door_choice == 'rd':
            out_str = "You chose to run"
            print(out_str)
            return out_str
        else:
            print("invalid choice")
            return 0
class Player:
        def __init__(self, name):
            self.name = name
            #self.flag = ''
            #self.inventory = {"has_sword" : False, "health_potion" : 0, "mana_potion" : 0}
            self.player_stats = {
                "num_lives" : 3,
                "strength" : 5,
                "vitality" : 5,
                "dexeterity" : 5,
                "intelligence" : 5,
            }
            self.movement_actions = {
                "left",
                "right",
                "forward",
                "backward"
            }
            self.interact_actions = {
                "look",
                "pickup",
                "attack",
                "run"
            }
            self.eating_actions = {"eat", "drink"}
            def validate():
                choice = input("Enter your choice : ")
                return choice
            print("Welcome to 'Hunt for Mighty Dragon'!")
            print("There are 2 rooms - Left (ld) and Right (rd)")
            print("In the Left room, you can look for the sword")
            print("In the right room, you can attack the dragon or run away")
            while True:
                print("Which room do you want to enter ? Type rd or ld")
                door_choice = validate()
                if door_choice not in ["ld", "rd"]:
                    print("typr rd or ld")
                    door_choice = validate()
                if door_choice == 'ld':
                    print(f"Enter your action from the list {self.interact_actions}")
                    intr_choice = validate()
                    intr_out = Item.interact(self,door_choice,intr_choice)
                    #print(intr_out)
                    if intr_out:
                        print("You can now go to the right room if you want")
                        continue
                    else:
                        print("You can go to any room")
                        continue
                elif door_choice == 'rd':
                    monster = Monster()
                    print(f"You have encountered the Monster {monster}")
                    print(f"Enter your action from the list {self.interact_actions}")
                    intr_choice = validate()
                    intr_out = Item.interact(self,door_choice,intr_choice)
                    print(intr_out)
                    if intr_out:
                        print("You can now go to the left room if you want")
                        continue
                    else:
                        print("You can go to any room")
                        continue
class Monster:
    def __init__(self):
        self.monster = ["Pikachhu", "Dracula", "Godzilla"]
    def mon_cho(self):
        self.monster_choice = random.choice(self.monster)
        return self.monster_choice
name = input("What is your name? : ")
player = Player(name)