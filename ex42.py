## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    def speak(self):
		print "something"

## Dog is-a Aninmal
class Dog(Animal):

    def __init__(self, name):
        ## dog has-a name
        self.name = name
		
	def speak(self):
		print "Woof!"

## Cat is-a Animal
class Cat(Animal):

    def __init__(self, name):
        ## Cat has-a name
        self.name = name

	def speak(self):
		print "Meow..."
		
## Person is-a object
class Person(object):

    def __init__(self, name):
        ## Person has-a name
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None
		
	def speak(self):
		print "To be or not to be?"

## Employee is-a person
class Employee(Person):

    def __init__(self, name, salary):
        ## ?? hmm what is this strange magic?
        super(Employee, self).__init__(name)
        ## Employee has-a salary
        self.salary = salary
	
	def speak(self):
		print "How may I help you?"

## Fish is-a object
class Fish(object):
    pass

## Salmon is-a Fish
class Salmon(Fish):
    pass

## Halibut is-a Fish
class Halibut(Fish):
    pass


## rover is-a Dog
rover = Dog("Rover")

## Satan is-a Cat that has-a name "Satan"
satan = Cat("Satan")

## mary is-a Person that has-a name "Mary"
mary = Person("Mary")

## mary has-a pet satan
mary.pet = satan

## frank  is-a Employee that has-a name "Frank" and salary 120000
frank = Employee("Frank", 120000)

## frank has-a pet rover
frank.pet = rover

## flipper is-a Fish
flipper = Fish()

## crouse is-a Salmon
crouse = Salmon()

## harry is-a Halibut
harry = Halibut()

rover.speak()
satan.speak()
#frank.speak()
#frank.pet.speak()