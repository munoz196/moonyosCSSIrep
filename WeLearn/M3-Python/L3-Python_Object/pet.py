pet = {
"name":"Doggo",
"animal":"dog",
"species":"labrador",
"age":"5"
}

class Pet(object):
    def __init__(self, name, age, animal):
        self.name = name
        self.age = age
        self.animal = animal
        self.hungry = False
        self.mood= "happy"


    def eat(self):
        print("> %s is eating..." % self.name)
        if self.is_hungry:
            self.is_hungry = False
        else:
            print("> %s may have eaten too much." % self.name)
            self.mood = "lethargic "

my_pet= Pet("Fido", 3, "dog")

my_pet.is_hungry= True
print("is my pet hungry? %s"% my_pet.is_hungry)
my_pet.eat()
print("how about now? %s" % my_pet.is_hungry)
print ("My pet is feeling %s" % my_pet.mood)
