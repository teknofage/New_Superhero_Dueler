# dog.py
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        print("dog initialized!")
        
    def bark(self):
        print("Woof!")
        
    def sits(self):
        print(f"{self.name} sits.")
        
    def rolls_over(self):
        print("{} rolls over.".format(self.name))
        
        

