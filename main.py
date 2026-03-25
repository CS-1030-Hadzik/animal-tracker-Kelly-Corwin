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

    # TODO: Create an instance of the Animal class
    # TODO: Print the Animal instance
    # TODO: Call the method to make a generic animal sound

    # TODO: Create an instance of the Dog class
    # TODO: Print the Dog instance
    # TODO: Call the method to make the dog-specific sound

    # TODO print out all the animals
