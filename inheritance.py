class animal():     #---------> parent class

    def sound(self):
        return "Animal sound"
    

class dog(animal):  #----------->child class
    def sound(self):
        return "Dog Barks"
    

class cat(animal):
    def sound(self):
        return "Cat Meows"
    

class human(animal):
    pass


dog_instance = dog()
print(dog_instance.sound())

human_instance = human()
print(human_instance.sound())