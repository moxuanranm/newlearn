class Animal(object):
    pass

class Runnable(object):
    def run(self):
        print('Running')

class Flyable(object):
    def fly(self):
        print('Flying')

class Mammal(Animal):
    pass

class Bird(Animal):
    pass

class Dog(Mammal,Runnable):
    pass

class Rat(Mammal,Flyable):
    pass

class Parrot(Bird,Flyable):
    pass

class Ostrich(Bird,Runnable):
    pass

