# A blueprint of what an OBJECT could be.
class Animal: 
    """
    Base class representing a generic animal.
    """
    # CLASS-level parameter/attribute/description
    kingdom = "Animalia" # Every animal, no matter what is in "Animalia"

    # OBJECT specific attributes - constructor initializer
    # The interpreter uses "self" to track the OBJECT we are creating. Name and species are temporary arguements. 
    def __init__(self, name, species): 
        self.name = name
        self.species = species
    # As soon as you leave the scope of this method, name and species no longer exist.

    # This is method, or something the animal CLASS can do.
    def speak(self): 
        print(f"{self.name} makes a noise.\n")

    # This is a majic method, and it changes/overrides how print(OBJECT) behaves.
    def __str__(self):
        return (f"Kingdom: {self.kingdom}\n"
               f"Name: {self.name}\n"
               f"Species: {self.species}\n")


