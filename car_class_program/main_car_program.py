from car_method_file import CarFile

car_drip = CarFile(2024, "Ferrari")

print("A C C E L E R A T I N G > > >")
for accelerations in range(5):
    car_drip.accelerate()
    print(f"Speed after accelerating {accelerations+1}: {car_drip.get_speed()}")

print("\n< < < B R E A K I N G")
for decelerations in range(5):
    car_drip.brake()
    print(f"Speed after braking {decelerations+1}: {car_drip.get_speed()}")