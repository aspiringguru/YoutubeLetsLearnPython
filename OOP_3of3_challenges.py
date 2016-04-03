#github.com/aspiringguru
#https://www.youtube.com/watch?v=rOaRMW8jYOo
from abc import ABCMeta, abstractmethod
#https://docs.python.org/2/library/abc.html
#abc = abstract base classes.
class Human(object):
    __metaclass__ = ABCMeta
    @abstractmethod
    def run(self):
        print "running"
class Robot(object):
    __metaclass__ = ABCMeta
    @abstractmethod
    def vacuum(self):
        print "vacuuming"
class Cyborg(Human, Robot):
    def __init__(self):
        super(Cyborg, self).__init__()
    def run(self):
        print "running blah"
    def vacuum(self):
        print "vacuuming blagh"
test1 = Cyborg()
test1.run()
test1.vacuum()







