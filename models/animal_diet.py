class AnimalDiet:
    def __init__(self, type, calories):
        self.type = type
        self.calories = calories
        
    def setType(self, type):
        self.type = type

    def setCalories(self, calories):
        self.calories = calories

    def getType(self):
        return self.type

    def getCalories(self):
        return self.calories        