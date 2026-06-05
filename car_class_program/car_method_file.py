from abstract_car_method_file import Car

class CarFile(Car):
    def __init__(self,  year_model, make, speed=0):
        self.__year_model = year_model
        self.__make = make
        self.__speed = speed

    def accelerate(self):
        self.__speed+=5 

    def brake(self):
        self.__speed-=5
        if self.__speed < 0:
            self.__speed = 0

    def get_speed(self):
        return self.__speed
    
    def __str__(self):
        return f"Car(year_model={self.__year_model}, make={self.__make}, speed={self.__speed})"