import random

def userInf():
    input("What is your name: ")
    age  = int(input("What is your age : "))
    return age

def ageRestrict(age) -> str:
    if int(age) >= 18:
        input("Press ENTER to start the game")
    elif int(age) <= 12:
        print("Oh no you don't!")
        exit()
    elif int(age) <= 17:
        print("You're just a bit too young.")
        exit()

def userInf():
    name = input("What is your name: ")
    age  = int(input("What is your age : "))
    return age

def ageRestrict(age:int) -> str:
    if age >= 18:
        input("Press ENTER to start the game")
    elif age <= 12:
        print("Oh no you don't!")
        exit()
    elif age <= 17:
        print("You're just a bit too young.")
        exit()

def attackDRGN(attackdrgn):
    #attack with the dragonslayersword
    if attackdrgn == 'dragonslayersword':
        print("You swing your sword at the dragon dealing a heavy blow to it. The dragon shoots fire at you but you use your sword to block it. you sprint toward the dragon and deal the final blow killing it")
        print("Having beaten the dragon you go look through the treasure grabbing the most important stuff. You return home and become really rich and very powerful.")
        exit()
    #hug the dragon
    elif attackdrgn == "hug":
        print("You go and hug the dragon. The dragon and you become good friends and togheter you begin taking over the world. After a month you have taken over the whole world.") 
        print("Now that you and the dragon are rulers of the world you can live comfortably and take it easy for the rest of your life.")
        exit()
    else:
        pass

def snaek(sneak):
    #stealing treasure
    if sneak == "steal":
        print("While you put some of the treasure in your bag the dragon wakes up and burns you to a crisp.")
        exit()
    #sneak attack the dragon
    elif sneak == "attack":
        print("You stab the dragon in it's weakspot but your sword breaks. The dragon wakes up and eats you whole.")
        exit()
    else:
        pass

def dragonRoom(dragon):
    #escaping from the dragon    
    if dragon == "escape":
        print("While trying to escape you get lost and die of dehydration.")
        exit()
    #sneaking behind the dragon
    elif dragon == "sneak":
        print("You've successfully sneak behind the dragon. Do you sneak 'attack' the dragon or 'steal' some treasure?")
        sneak = input("{").lower()  
        return sneak          
    #attack the dragon
    elif dragon == "attack":
        print("You think of a way to attack the dragon. will you use your 'dragonslayersword' or 'hug' the dragon?")
        attackdrgn = input("{").lower()
        return attackdrgn
    else:
        pass

def crossroad2(cross):
    #going left at second crossroad
    if cross == "left":
        print("You walk for 5 hours till you stop at a door. You open the door and get pushed through by some invisible force. by looking at our surroundings you know your outside and the door has dissapeared.")
        print("When you go back to the entrance of the dungeon you can't find it anywhere it looks like it's dissapeared.")
        exit()
    #going right at second crossroad
    elif cross == "right":
        print("You walk through the right hall when you suddenly hear a click. You look down and you see the floor dissapearing. While you are falling you see something shiny at the bodem of the pit. It turns out that they were spikes.")
        exit()
    #going straight at second crossroad
    elif cross == "straight":
        print("Walking through the middle hall you hear a deep rumble but you think nothing of it. You stop at a giant door. Behind the door is the dungeon boss.")
        print("You enter the room and see a gaint black dragon gaurding a huge pile of treasure. Even though it is sleeping you know it's really powerfull.")
        print("There are three options you can think of: 'attack', 'sneak' behind it and 'escape'.")
        dragon = input("{").lower()
        return dragon
    else:
        pass

def randomChance():
    number = random.randint(0, 100)	#to make a change to have two diffrent endings that are chosen at random
    if number < 76:
        print("You walk to the goblin unarmed with your arms open. The golbin spots you and bashes your head in with it's club.")
        print("GAME OVER")
        exit()
    elif number > 75:
        print("Just before you hug the goblin you wake up. It turs out it was all a dream.")
        exit()

def fGoblin(goblin):
    #hugging the goblin
    if goblin == "hug":
        randomChance()
    #attacking the goblin
    elif goblin == "attack":
        print("You draw your sword and approach the goblin. The goblin swings his club you dodge it and swing your sword at it. The attack was a critical hit and killed the goblin instantly.")
        print("You loot the goblin and venture deeper into the dungeon. After taking a quick nap you stop at another crossroad. Do you go 'left', 'right' or 'straight'?")
        cross = input("{").lower()
        return cross
    else:
        pass

def legndSword(key):
    #keep going with the legendary sword
    if key == "keep going":
        print("You keep going deeper into the dungeon. After a little while you get the feeling that you're surrounded. You get attacked from all sides by goblins and die.")
        exit()
    #return home with legendary sword
    elif key == "return":
        print("You return home. You sell the legendary sword and live the life of luxury. at the age of 69 you drown under a pile of money you tried to swim in.")
        exit()
    else:
        pass

def chestMimmic(chest):
    #mimic attaks
    if chest == "lockpick":
        print("While trying to lockpick the chest you get attacked. turns out the chest was a mimic. It bites you to death")
        exit()
    #opening the chest with the key
    elif chest == "key":
        print("You open the chest with your key. In the chest you find a legendary sword. Will you 'keep going' deeper into the dungeon or will you 'return' home.")
        key = input("{").lower()
        return key
    else:
        pass

def hallway1(hallway):
    #left hallway
    if hallway != "right":
        print("You enter the left hallway. In the distance you see a goblin. There are two things you can think of doing: giving it a 'hug' or 'attack' it with your sword.")
        goblin = input("{").lower()
        return goblin
    #right hallway
    elif hallway == "right":
        print("You walk into a room with a chest right at the center. Do you open it with your 'key'or do you try with 'lockpick'?")
        chest = input("{").lower()
        return chest
    else:
        pass

def Enter(enter):
    #entering the dungeon
    if enter == "enter":
        print("You enter the dungeon and walk trhough a long hallway. After some time you stop at a crossroad. There are two paths do you want to go 'left' or 'right'?")
        hallway = input("{").lower()
        return hallway
    #don't enter the dungeon
    else:
        print("You return home to your boring uneventful life. Before passing on to the afterlife you say to your self that the only thing you regret is not going in to that dungeon.")
        exit()

def start():
    #player chooses if he wants to enter dungeon
    print("You stand before the entrance of a dungeon do you 'enter' or will you 'leave'?")
    enter = input("{").lower()
    return enter

age = userInf()
ageRestrict(age)
var1 = start()
var2 = Enter(var1)
var3 = hallway1(var2)
var4 = chestMimmic(var3)
legndSword(var4)
var5 = fGoblin(var3)
var6 = crossroad2(var5)
var7 = dragonRoom(var6)
snaek(var7)
attackDRGN(var7)