from animal import Animal

class Frog(Animal):

    def __init__(self, name, species, type):
        super().__init__(name, species)
        self.type = type
    
    def __str__(self):
        return super().__str__() + f"Type: {self.type}\n"
    
    def speak(self):
        print(f"{self.name} did a ribbits!\n")