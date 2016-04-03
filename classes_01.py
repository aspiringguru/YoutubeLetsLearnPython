__author__ = 'MatthewWork'

#https://www.youtube.com/watch?v=pxbdnrjf-Uc
#Let's Learn Python #10 - Inheritance - OOP 1 of 3

class BaseClass(object):
    def printHam(self):
        print 'ham'

class InheritingClass (BaseClass):
    pass

x = InheritingClass()
x.printHam()




