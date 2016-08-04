## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

## ??
class Dog(Animal):

    def __init__(self, name):
        ## ??
        self.name = name
        self.sound = "woof"

## ??
class Cat(Animal):

    def __init__(self, name):
        ## ??
        self.name = name
        self.sound = "meow"

## ??
class Person(object):

    def __init__(self, name):
        ## ??
        self.name = name

        ## ??
        self.pet = None

## Employee is-a subclass of Person (inherits)
class Employee(Person):

        def __init__(self, name, salary):
            ## ?? hm what is this strange magic?
            super(Employee, self).__init__(name)
            ## ??
            self.salary = salary

## Fish is-a object
class Fish(object):
    pass

## Salmon is-a subclass of Fish
class Salmon(Fish):
    pass

## Halibut is-a subclass of Fish
class Halibut(Fish):
    pass


## rover is-a Dog
rover = Dog("Rover")

## satan is-a Cat
satan = Cat("Satan")

## mary is-a Person
mary = Person("Mary")

## mary has-a pet names satan
mary.pet = satan

## frank is-a Employee
frank = Employee("Frank", 120000)

## frank has a pet named rover
frank.pet = rover

## flipper is-a Fish
flipper = Fish()

## crouse is-a Salmon
crouse = Salmon()

## harry is-a Halibut
harry = Halibut()

print "I wonder if %s makes a sound." % rover.name
print "Let's see if he makes a sound: %s" % rover.sound

    def do_something_new():
        print "blah"
        blah_dict = {
                "1": "Do it"
                "2": "Don't Do it"
                "3": "I hate you"
                }

