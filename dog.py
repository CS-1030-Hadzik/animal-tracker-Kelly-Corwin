# Dog doesn't know about the Animal, so you have to tell it what the PARENT CLASS is by importing it.
from animal import Animal

# Dog is a CHILD CLASS of Animal
class Dog(Animal):
    """
    Derived class representing a dog, which is a type of Animal.
    """
# The 'super()' function tells it to initialize from the PARENT. 
    def __init__(self, name, species, size):
        super().__init__(name, species)
        self.size = size

    def __str__(self):
        return super().__str__() + f"Size: {self.size}\n"

    def speak(self):
        print(f"{self.name} did a woofs!\n")

    # TODO: Override the __str__ method to include the breed.
    # Example output:
    # Kingdom: 'kingdom attribute', Name: 'name attribute', Species: 'species attribute', Breed: 'breed attribute'
    
    # TODO: Add a method for the dog to make a specific sound. 
    # Call the method `speak` and make it output a specific message like 
    # "The dog barks.