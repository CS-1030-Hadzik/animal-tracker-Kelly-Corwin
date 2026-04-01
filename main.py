# From the animal.py file import the Animal class.
from animal import Animal 
from dog import Dog
from frog import Frog

if __name__ == "__main__":

    # This is the OBJECT of the animal CLASS. AKA an Instanciation of the class. 
    animal = Animal("Animal Name", "Species")
    dog = Dog("Ginger", "Canine", "Medium")
    frog = Frog("Fred", "Amphibian", "Pond")
    
    print(frog)
    frog.speak()

    print(dog)
    dog.speak()

    dog.perform_trick("dance") # We call the dog object and the perform_trick method with the sit argument.
    dog.perform_trick("flip")
    print(dog.name)
    dog.new_age(-1)
    dog.new_age(12)
    
