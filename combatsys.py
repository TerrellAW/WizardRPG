<<<<<<< HEAD
'''
A combat system inspired by classic rpg games.
It will have characters with health and attacks with AP (attack points).
The player will have five uses of a move that blocks damage.
One use of a healing move that heals some health and restores AP.
Ten to twenty uses of an attack move.
The enemy NPC will have one attack (blood magic).
'''
# Class for player and enemy NPC
class Character:
    def __init__(self, name, health):
        self.name = name
        self.health = health

# Class for attacks/abilities
class Attack:
    def __init__(self, name, damage, ap, target):
        self.name = name
        self.damage = damage
        self.ap = ap
        self.target = target

# Character Objects
player = Character('Player', 25)
npc = Character('NPC', 40)

# Attacks and Abilities
fireball = Attack('Fire Ball', 5, 15, 'NPC')
barrier = Attack('Barrier', 0, 5, 'Player')
heal = Attack('Heal', -5, 1, 'Player')
=======
'''
A combat system inspired by classic rpg games.
It will have characters with health and attacks with AP (attack points).
The player will have five uses of a move that blocks damage.
One use of a healing move that heals some health and restores AP.
Ten to twenty uses of an attack move.
The enemy NPC will have one attack (blood magic).
'''
# Class for player and enemy NPC
class Character:
    def __init__(self, name, health):
        self.name = name
        self.health = health

# Class for attacks/abilities
class Attack:
    def __init__(self, name, damage, ap, target):
        self.name = name
        self.damage = damage
        self.ap = ap
        self.target = target

# Character Objects
player = Character('Player', 25)
npc = Character('NPC', 40)

# Attacks and Abilities
fireball = Attack('Fire Ball', 5, 15, 'NPC')
barrier = Attack('Barrier', 0, 5, 'Player')
heal = Attack('Heal', -5, 1, 'Player')
>>>>>>> b724a4a11440ae05ef1e2416307cad626194888b
blood_blade = Attack('Blood Blade', 6, 40, 'Player')