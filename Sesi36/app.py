# raka = ["Raka Ardhi", 28, "CurDev", 2265]
# spock = ["Spock", 35, "Science Officer", 2254]
# mccoy = ["Leonard McCoy", "Chief Medical Officer", 2266]

# print("Daftar nama: ", raka[0], spock[0], mccoy[0])
# print("Daftar umur: ", raka[1], spock[1], mccoy[1])
# print("Daftar jabatan: ", raka[2], spock[2], mccoy[2])
# print("Daftar tahun mulai: ", raka[3], spock[3], mccoy[3])

# class Dog:   
#     # Class attribute
#     species = "Canis familiaris"
#     def __init__(self, input_name, input_age):        
#         self.name = input_name      
#         self.age = input_age
   
#     def __init__(self, info_name, info_age):        
#         self.name = info_name      
#         self.age = info_age





# dog_3 = Dog()
# dog_3.name = 'Scooby'
# dog_3.age = 1
# print("Species")
# print(dog_1.species)
# print(dog_2.species)
# print(dog_3.species)
# print(buddy.species)

# dog_1 = Dog('Miley', 9)        
# dog_2 = Dog('Hike', 2)         
# dog_3 = Dog('Scooby', 1)
# buddy = Dog('Buddy', 9)
# print("Dog 1 ::", dog_1.name, dog_1.age)
# print("Dog 2 ::", dog_2.name, dog_2.age)
# print("Dog 3 ::", dog_3.name, dog_3.age)
# print("Buddy ::", buddy.name, buddy.age)

# class Dog:
#     species = "Canis familiaris"

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         # self.breed = breed

#     # Instance method
#     def description(self):
#         return f"{self.name} is {self.age} years old"

#     # Another instance method
#     def speak(self, sound):
#         return f"{self.name} says {sound}"


# dog_1 = Dog('Miley', 9)
# buddy = Dog("Buddy", 9)

# print(buddy.description())
# print(dog_1.description())

# print(dog_1.speak("Woof Woof"))
# print(dog_1.speak("Bow Wow"))

# parent class
# class Dog:
#     species = "Canis familiaris"

#     def __init__(self, name, age, breed):
#         self.name = name
#         self.age = age
#         self.breed = breed

#     # Instance method
#     def description(self):
#         return f"{self.name} is {self.age} years old"

#     # Another instance method
#     def speak(self, sound):
#         return f"{self.name} says {sound}"

# miles = Dog("Miles", 4, "Jack Russell Terrier")
# buddy = Dog("Buddy", 9, "Dachshund")
# jack = Dog("Jack", 3, "Bulldog")
# jim = Dog("Jim", 5, "Bulldog")

# # define that Bulldogs is a subclass of Dog class
# class Bulldogs (Dog):
#     # Another instance method
#     def speak(self):
#         return f"{self.name} says Woof Woof"

# # define that Dachshund is a subclass of Dog class
# class Dachshund (Dog):
#     # Another instance method
#     def speak(self):
#         return f"{self.name} says yap yap"
# class JackRussellTerrier(Dog):
#     # pass
#     def speak(self, sound):
#         return f"{self.name} says {sound}"

# hike = Bulldogs('Hike', 9, 'Bulldogs')
# miles = JackRussellTerrier('Miles', 4, 'Jack Russel Terrier ')
# dachs = Dachshund('Dachs', 9, 'Dachshund')

# print(hike.speak())
# print(miles.speak("arf"))
# print(dachs.speak())

# print(hike)
# print(miles)
# print(dachs)

# print(1 + 1)        #2, int + int,   __add__()  __add__(int, int)
# print('1' + '1')    #11, str + str,  __add__() __add__(str, str)
# print(hike + miles) #???             __add__() __add__(obj/instance, obj/instance)

# __repr__() --> provide unambiguous tentang suatu object --> ditujukan baca
# oleh developer:; debugging, logging, etc etc --> "Dog(self, name, age, bread)"
# __str__() --> provide informasi yang lebih readab1 --> tujuannya untuk
# disaksikan/ditujukan kepada end user --> "Miley is 4years old"

# print(hike)
#     cuma ada 1 __str__() --> __str__()
#     cuma ada 1 __repr__() --> __repr__()
#     kalau 22nya ada: priorias 1 __str__()

#parent class
class Dog:
    species = "Canis familiaris"
 
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed
 
    # Instance method
    def description(self):
        return f"{self.name} is {self.age} years old"
 
    # Another instance method
    def speak(self, sound):
        return f"{self.name} says {sound}"
 
    def __repr__(self):
        return f"to create instance :: Dog( name={self.name}, age={self.age}, breed={self.breed} ) #REPR"
 
    def __str__(self):
        return f"clean info :: {self.name} is {self.age} years old {self.breed}  #STR"
    
miles = Dog("Miles", 4, "Jack Russell Terrier")
# buddy = Dog("Buddy", 9, "Dachshund")
 
# Sebelum __repr__ or __str__ ada
print(miles) # akan return memory addres untuk object/instance miles, seperti : <__main__.JackRussellTerrier object at 0x000002806CAEABB0>
#^ lihat ke catatan bagian prioritas
 
 
#Setelah ada  dunder method __repr__() ATAU __str__()
print(repr(miles))
print(miles.__repr__())
 
print(str(miles))
print(miles.__str__())

class Bulldogs(Dog):
    def __init__(self, name, age, breed, weight_in_lbs):
        super().__init__( name, age, breed)
        self.weight_in_lbs = weight_in_lbs
    
    # Another instance method
    def speak(self):
        return f"{self.name} says Woof Woof"
    def __add__(self, other):
        return self.weight_in_lbs + other.weight_in_lbs

scooby = Bulldogs('Scooby', 2, 'Bulldogs', 15)
scooby_jr = Bulldogs('Scooby JR', 1, 'Bulldogs', 8)

print("Scooby : ", scooby.weight_in_lbs)
print("Scooby JR : ", scooby_jr.weight_in_lbs)