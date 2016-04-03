#github.com/aspiringguru
#https://www.youtube.com/watch?v=rOaRMW8jYOo
from abc import ABCMeta, abstractmethod
#https://docs.python.org/2/library/abc.html
#abc = abstract base classes.

class Enemy(object):
    __metaclass__ = ABCMeta
    @abstractmethod
    def attackPlayer(self, player):
        pass

class EnvironmentAsset(object):
    __metaclass__ = ABCMeta
    @abstractmethod
    def __init__(self):
        self.mobile = False


class Trap(Enemy, EnvironmentAsset):
    def __init__(self):
        super(Trap, self).__init__()
    def attackPlayer(self, player):
        return player.health -10

class Player(object):
    def __init__(self):
        self.health = 5


x = Trap()
print x
p = Player()
print p.health
print x.attackPlayer(p)

