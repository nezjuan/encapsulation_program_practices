from defined_pet_class_file import PetClass

pet_name= input("Please insert your Pet's name: ")
pet_type= input("What is your pet? (i.e. Dog, Cat, Bird): ")
pet_age= input("How old is your pet? (Years): ")

pet_info = PetClass(pet_name, pet_type, pet_age)

print(f"\n[Your Pet's Info]" \
f"\n[Pet Name]: {pet_info.get_name()}" \
f"\n[Type]: {pet_info.get_animal_type()}" \
f"\n[Age]: {pet_info.get_age()} Years Old")