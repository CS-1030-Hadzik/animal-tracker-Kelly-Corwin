class Animal:
    """
    Base class representing a generic animal.
    """
    # Class-level attribute - characteristic - description
    kingdom = "Animalia" # Every animal, no matter what is in "Animalia"
    def __init__(self, name, species): # The interpreter uses "self" to track the object we are creating. Name and species are arguements. 
        self.name = name
        self.species = species

    def speak(self): # This is something the animal class can DO.
        print(f"{self.name} makes a noise.")

    def __str__(self):
        return (f"Kingdom: {self.kingdom}\n"
               f"Name: {self.name}\n"
               f"Species: {self.species}")

    # TODO create a class-level attribute that is a list of all the Animal objects

    # TODO create the initializer for Animal with name and species as attributs

    # TODO: Add a method to make a generic sound 
    # Call the method `speak` and make it output a specific message like 
    # "The animal makes a noise.""

    # TODO __str__ method for string representation
    # Example output
    # Kingdom: 'kingdom attribute', Name: 'name attribute' Species: 'species attribute' 
