# Dog doesn't know about the Animal, so you have to tell it what the PARENT CLASS is by importing it.
from animal import Animal

# Inheritance allows us to define a class that inherits all the methods/properties/parameters from another class.

# Dog is a CHILD CLASS of Animal
class Dog(Animal):
    """
    Derived class representing a dog, which is a type of Animal.
    """
    # kingdom
    # name
    # species
    # speak()
    # __str__
    # all of the above are inherited from the parent, Animal, class

# The 'super()' function tells it to initialize from the parent. 
    def __init__(self, name, species, size):
        super().__init__(name, species)
        self.size = size
        self.__age = 0 # Encapsulation __ = Private 

    # Public method to get the dog's age.
    # "Getter"
    def get_age(self): # Public
        return self.__age
    # "Setter"
    def new_age(self, new_age): # Public
        if new_age < 0:
            return print("The age you entered is not valid.")
        self.__age = new_age
        self.print_dog_age()
        
    def print_dog_age(self): # Private
        print(f"{self.name}'s age is {self.__age}.")

    def __str__(self):
        return super().__str__() + f"Size: {self.size}\n" # This calls the parent's __str__ function

    def speak(self): # Example of polymorphism. Has the same name as another method, but does something different. 
        print(f"{self.name} did a woofs!\n") # We don't call the parent here because we are overriding the speak method with something new

    # Dog preforms a trick (sit, lay down, stay, fetch, shake, etc)
    # Create a method that allows us to have the Dog object do a trick

    def perform_trick(self, trick):
        self.trick = trick
        # The Match statement is used to perform different actions using the same arguement
        print(f"{self.name}", end=" ")
        match trick:
            case "sit":
                print("sits down.")
            case "lay down":
                print("lays down.")
            case "fetch":
                print("fetches a ball.")
            case "stay":
                print("stays in place.")
            case "shake":
                print("shakes your hand.")
            case "dance":
                print("dances around the room.")
            case _: # default case that prints if the user inputs anything you haven't mapped out
                print("looks at you, confused.")

   