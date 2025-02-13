from abc import ABC,abstractmethod

class animal(ABC):
    
    @abstractmethod
    def speak(self):
        pass

# x = animal() ---> cannot instantiate abstract class animal
# x.speak

class dog(animal):

    def speak(self):
        print("Dog barks")

    
    def sound(self):
        print("Woff Woof")


x = dog()
x.speak()
x.sound()