__author__ = 'MatthewWork'


class Character (object):
    def __init__(self, name):
        self.health = 100
        self.name = name
    def printName(self):
        #print "method Character.printName called"
        print self.name
        #print "method Character.printName end"
        #return ""

#class NPC inherits from Character   (non playable character)
class Npc (Character):
    def __init__(self, name):
        super(Npc, self).__init__(name)
#class Friendly inherets from NPC inherits from Character
class Friendly (Npc):
    def __init__(self, name):
        super(Friendly, self).__init__(name)

#class Enemy inherets from NPC inherits from Character
class Enemy(Npc):
    def __init__(self, name):
        super(Enemy, self).__init__(name)
        self.attackDamage = 5 #_ONLY_ Enemy objects have this attribute


#class PC inherits from Character    (playable character)
class Pc (Character):
    def __init__(self, name):
        super(Pc, self).__init__(name)
        self.Weapon = Weapon("Knife")
#class Archer inherets from Pc inherits from Character
class Archer (Pc):
    def __init__(self, name):
        super(Archer, self).__init__(name)
#class Archer inherets from Pc inherits from Character
class Butcher(Pc):
    def __init__(self, name):
        super(Butcher, self).__init__(name)
#class GreenLantern inherets from Pc inherits from Character
class GreenLantern(Pc):
    def __init__(self, name):
        super(GreenLantern, self).__init__(name)

#class Blacksmith inherits from Character
class Blacksmith (Character):
    def __init__(self, name, forgeName):
        super(Blacksmith, self).__init__(name)
        self.forge = Forge(forgeName)

class Forge:
    def __init__(self, forgeName):
        self.name = forgeName
        #print "Forge class initiated with forgeName=", forgeName

class Weapon:
    def __init__(self, weaponName):
        self.name = weaponName



bs = Blacksmith("Bob", "Ricks")
print "bs.health=", bs.health
#print "bs.printName()="
bs.printName()
#print "bs.forge.name=", \
print bs.forge.name
print ""
gl = GreenLantern("Something Green")
gl.printName()
print gl.health
print gl.Weapon.name
print ""
gl = Butcher("Brian Meat Supplies")
gl.printName()
print gl.health
print gl.Weapon.name
print ""
gl = Archer("Andrew w bow")
gl.printName()
print gl.health
print gl.Weapon.name
print ""
gl = Friendly("buddy1")
gl.printName()
print gl.health
#print gl.Weapon.name #NB: since Friendly does not have a Weapon attribute, calling blah.Weapon.name will be error.



