class Dog:
    species = "Canis Familiaris"

    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    def bark(self):
        return f"{self.name} says Woof!"

    def zoomie(self):
        return f"{self.name} runs like crazy!"

    def dog_math(self, num1, num2):
        answer = num1 + num2
        return f"{num1} + {num2} = snack time for {self.name}, and {answer} for hoomans."


# Create instances of the Dog class
dog1 = Dog("Mozzy", 4, "Multipoo")
dog2 = Dog("Ralph", 8, "Golden Retriever")

print(dog1.name)
print(dog1.breed)
print(dog2.name)
print(dog2.bark())
print(dog1.dog_math(3, 12))