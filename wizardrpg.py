# Main Menu
print("###############################")
print("#                             #")
print("#           WIZARD            #")
print("#            GAME             #")
print("#                             #")
print("###############################")
print("        Press 1 to Start       ")
start = int(input("> "))
# Character Creation / Back Story
if (start == 1):
    print("The people of your land believe the world was created by dragons")
    print("These dragons were created by the Gods of Creation.")
    print("You came from a small village, which dragon was worshipped in this village?")
    print("1 - Ardor, the Fire Dragon")
    print("2 - Gelus, the Ice Dragon")
    print("3 - Aecor, the Water Dragon")
    print("4 - Silva, the Plant Dragon")
    print("5 - Fulgur, the Thunder Dragon")
    print("6 - Petra, the Earth Dragon")
    dragon = int(input("> "))
    if dragon == 1:
        print("You studied pyromancy at the Royal Mage Tower Academy.")
        print("You now have the ability to command fire.")
    elif dragon == 2:
        print("You studied cryomancy at the Royal Mage Tower Academy.")
        print("You now have the ability to command ice.")
    elif dragon == 3:
        print("You studied hydromancy at the Royal Mage Tower Academy.")
        print("You now have the ability to command water.")
    elif dragon == 4:
        print("You lived among the druids and learned their arts.")
        print("You now have the ability to command plants.")
    elif dragon == 5:
        print("You studied electromancy at the Royal Mage Tower Academy.")
        print("You now have the ability to command electricity.")
    elif dragon == 6:
        print("You studied geomancy at the Royal Mage Tower Academy.")
        print("You now have the ability to command the ground itself.")
    else:
        print("That number is not associated with a dragon.")
print("After you completed your studies, you: ")
print("1 - Used magic to invent a communication network.")
print("2 - Locked yourself in a tower to study forbidden magic.")
print("3 - Joined a mercenary company and served as a guard for nobles and wizards.")
backstory = int(input("> "))
if backstory == 1:
    print("Traditional mages are purists and immediately shutdown your strange idea.")
    print("You now seek an audience with a powerful ruler to bring your ideas into being.")
    intel = 10
    mana = 6
    str = 4
    char = 4
elif backstory == 2:
    intel = 8
    mana = 8
    str = 4
    char = 4
    if dragon == 1:
        print("After years of study, you have become a necromancer.")
        print("You now command the undead and can summon burning ghouls.")
        print("You will be hunted as a rogue mage.")
    if dragon == 2:
        print("After years of study, you have become a necromancer.")
        print("You now command the undead and can summon ice men.")
        print("You will be hunted as a rogue mage.")
    if dragon == 3:
        print("After years of study, you have become a necromancer.")
        print("You now command the undead and can summon drowned zombies.")
        print("You will be hunted as a rogue mage.")
    if dragon == 4:
        print("After years of study, you have become a necromancer.")
        print("You now command the undead and can summon undead druids.")
        print("You will be hunted as a rogue mage.")
    if dragon == 5:
        print("After years of study, you have become a necromancer.")
        print("You now command the undead and can summon ghosts.")
        print("You will be hunted as a rogue mage.")
    if dragon == 6:
        print("After years of study, you have become a necromancer.")
        print("You now command the undead and can summon skeletal warriors.")
        print("You will be hunted as a rogue mage.")
elif backstory == 3:
    intel = 5
    mana = 5
    str = 6
    char = 8
    print("You made many friends and gained useful connections.")
    print("Your time as a mercenary soon came to an end.")
    print("Now you embark on a new adventure.")
else:
    print("That is not a valid number.")
print("You awake in the city of Kaen.")
print("You have the clothes on your back and a few coppers to your name.")
print("You need to find a source of money.")
choices1 = """You:
1 - Go to the tavern.
2 - Go to the market.
3 - Go to the dock.
"""
print(choices1)
choice1 = int(input("> "))
if choice1 == 1:
    print("You enter the busy tavern.")
    print("You see some shady individuals seated in a back corner.")
    print("You see some boisterous adventurers seated by the barkeep.")
    if backstory == 3:
        print("You see someone who must be a disguised noblewoman.")
tavernchoice = """You choose to:
1 - Approach the shady individuals
2 - Approach the adventurers"""
print(tavernchoice)
if backstory == 3:
    print("3 - Approach the disguised noblewoman")
approach = int(input("> "))
if approach == 1:
    print("You approach the shady individuals.")
    print("The hooded individuals look up from their card game.")
    print("\"Who are you?\"")
    print("A hooded man seated with his back to the wall asks you with an interrogating gaze.")
    name = input("Enter your name: ")
    print(f"Well, {name}, what do you want?")
    print("1 - You don't want anything")
    print("2 - You want to join his group")
    print("3 - You want to start a fight")
    shady = int(input("> "))
    if shady == 1:
        print("You leave them alone.")
    if shady == 2:
        print("You tell them your potential as a new recruit.")
        print("They need proof, you must pickpocket a certain noble to prove your skill.")
        print("They tell you a disguised noblewoman is in this tavern.")
        print("They came here to steal her necklace, they want you to do it for them.")
    if shady == 3:
        print("They rush to their feet and take out their knives.")
        print("There are three of them and there is little room to maneuver.")
elif approach == 2:
    print("You approach the adventurers.")
elif approach == 3:
    if backstory == 3:
        print("You approach the disguised noblewoman.")
    else:
        print("That is not a valid number.")
else:
    print("That is not a valid number.")


input("> ")
