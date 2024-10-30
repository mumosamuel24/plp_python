class Person:
    def __init__(self, name, age, gender, traits):
        self.name = name
        self.age = age
        self.gender = gender
        self.traits = traits  # New attribute for traits

    def introduce(self):
        traits_description = ', '.join(self.traits)  # Joining traits into a string
        print(f"Hello, my name is {self.name}. I am {self.age} years old, I identify as {self.gender}, and I have the following traits: {traits_description}.")

# Creating an instance of the Person class with additional traits
person1 = Person("Sam", 23, "Male", ["muscular"])
# Calling the introduce method to display the person's information
person1.introduce()
