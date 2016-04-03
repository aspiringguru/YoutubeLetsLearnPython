#github.com/aspiringguru
#https://www.youtube.com/watch?v=TF_y8Gta0vY
from Base import BaseClass

class InClass(BaseClass):
    def __init__(self):
        super(InClass, self).__init__()
        self.x = 17

class InClass2(BaseClass):
    def __init__(self):
        super(InClass2, self).__init__()
    def printHam(self):
        print "Ham2"

class InClass3(InClass, InClass2):
    def __init__(self):
        super(InClass3, self).__init__()


a = BaseClass()
print a.x
b = InClass()
print b.x
c = InClass2()
c.printHam()
d = InClass3()
print d.x
d.printHam()
#
print BaseClass.__subclasses__()
#[<class '__main__.InClass'>, <class '__main__.InClass2'>]
print InClass.__subclasses__()
#[<class '__main__.InClass3'>]
print InClass2.__subclasses__()
#[<class '__main__.InClass3'>]
