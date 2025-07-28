print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
path = input("There are two roads before you.\n    Do you go 'left' or 'right'?\n").lower()
if path == "left":
    action = input("You come across a river.\n    Do you try to 'swim' or 'wait'?\n").lower()
    if action == "wait":
        door = input("You spot a house. As you approach, you can make out three doors.\n"
                     "Do you enter the 'red', 'blue, or 'yellow' door?\n").lower()
        if door == "yellow":
            print("You find the treasure and teleported back home. You Win!")
        elif door == "red":
            print("You are teleported to your hometown and forget your adventures. Game Over.")
        elif door == "blue":
            print("You see a vast sea before you. With any luck, you may make it back home. Game Over.")
        else:
            print("The house dissipates. Game Over.")
    else:
        print("You are unable to swim in the strong current. Game Over.")
else:
    print("You get lost in a dense jungle. Game Over.")
