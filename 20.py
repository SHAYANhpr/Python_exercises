class animal:
    zoo_name = "iran Zoo"  

    def __init__(self, name, species, age, sound):
        self.name = name
        self.species = species
        self.age = age
        self.sound = sound

    def make_sound(self):
        print(f"{self.name} mige: {self.sound}")

    def info(self):
        print(f"Name: {self.name}")
        print(f"Species: {self.species}")
        print(f"Age: {self.age}")
        print(f"Zoo: {animal.zoo_name}")

    def __str__(self):
        return f"{self.name} ({self.species}) - Age: {self.age}, Sound: {self.sound}"


class Bird(animal):
    def __init__(self, name, species, age, sound, wing_span):
        super().__init__(name, species, age, sound)
        self.wing_span = wing_span 

    def make_sound(self):
        print(f"{self.name} jir jir kardan: {self.sound}")

    def info(self):
        super().info()
        print(f"Wing Span: {self.wing_span} cm")


print("animal Example:")
shir = animal("shir", "gorbesan", 5, "woooooow")
print(shir)           
shir.make_sound()
shir.info()

print("\nBird Example:")
parrot = Bird("mina", "prande", 3, "oooooo", 20)
print(parrot)
parrot.make_sound()
parrot.info()

        