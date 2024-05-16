#Treasure Island Game
#find the treasure
print('''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/
*******************************************************************************
''')
print('Welcome to Preshy\'s Treasure Island\nYour mission is to find the treasure.\nGood Luck!')
road = input('Your\'re at a cross road. where do you want to go? Type "left" or "right"\n').lower()
if road == 'left':
    lake = input('You came to a lake. There is an island in the middle of the lake.\nType "wait" to wait for a boat. Type "swim" to swim across.\n').lower()
    if lake == 'wait':
        doors = input('You arrive at the island unharmed. There is a house with 3 doors.\nOne red, one yellow and one blue. which color do you choose?\n').lower()
        if doors == 'red':
            print('It\'s a room full of fire. GAME OVER!')
        elif doors == 'blue':
            print('Yikes! A bomb...Tick tock...BOOM!!. GAME OVER!!')
        else:
            print('Hurray you found the treasure!. You Won!')
    else:
        print('Oh no the are big sharks in the sea. Game Over!')
else:
    print('opps You just entered a big hole. GAME OVER!')