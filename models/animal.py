class Animal:

    def __init__(self, name, age ):
        self.name = name
        self.age = age

    def printAnimal(self):
        print(self.name)
        print(self.age)

    def makeNoise(self):
        print("Animal making noise")

    def getAge (self):
        return self.age
    
    def setAnimalAge(self, age):
        self.age = age

    def setAnimalDiet(self, animal_diet):
        self.animal_diet = animal_diet

    def printAnimalDiet(self):
        print(self.animal_diet.getType())
        print(self.animal_diet.getCalories())
