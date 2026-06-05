from abstract_pet_class_file import AbstractPetClass

pet_name= input("Please insert your Pet's name: ")
pet_type= input("What is your pet? (i.e. Dog, Cat, Bird): ")
pet_age= input("How old is your pet? (Years): ")

pet_info = AbstractPetClass(pet_name, pet_type, pet_age)

print(f"\n Your Pet's Info" \
f"\nPet Name: {pet_info.get_name()}" \
f"\nType: {pet_info.get_animal_type()}" \
f"\nAge: {pet_info.get_age()}")