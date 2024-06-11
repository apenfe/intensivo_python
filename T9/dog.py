class Dog:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        print(f"{self.name} is rolling over.")

my_dog = Dog("Zaira",8)
my_other_dog = Dog("Laika",3)

print(f"El nombre de mi perro es {my_dog.name}")
print(f"Y tiene {my_dog.age} años")

my_dog.sit()
my_dog.roll_over()

my_other_dog.sit()
my_other_dog.roll_over()