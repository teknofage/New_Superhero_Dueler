# my_dogs.py
import dog

my_dog = dog.Dog("Rex", "SuperDog")
my_dog.bark()

my_other_dog = dog.Dog("Annie", "SuperDog")
print(my_other_dog.name)

my_first_other_dog = dog.Dog("Steve", "Bloodhound")
my_second_other_dog = dog.Dog("Flash", "Labrador")
my_third_other_dog = dog.Dog("Englebert", "Whippet")

my_first_other_dog.bark()
my_second_other_dog.sits()
my_third_other_dog.rolls_over()