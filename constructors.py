from abc import ABC, abstractmethod

class animal(ABC):

    def __init__(self,name,species):
        self.name = name
        self.species= species

    
    @abstractmethod
    def speak(self):
        print("Animal speaks")


class dog(animal):

    def __init__(self, name, breed):
        super().__init__(name, "dog")
        self.breed = breed


    def get_details(self):
        print(f"{self.name} is a {self.species} belongs to {self.breed}")

    
    def speak(self):
        print("dog barks")


x = dog("Max","German Separd")

x.get_details()