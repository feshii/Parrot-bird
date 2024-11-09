class parrot:
    species = "bird"
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Species:", self.species)
t1 = parrot("Blu", 10)
t1.display()
t2 = parrot("Snowball", 2)
t2.display()
