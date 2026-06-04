from abstract_fan_class_file import Fan
from getters_file import Getters
from setters_file import Setters

class FanFile(Setters, Getters, Fan):

    def __init__(self, speed, radius, color, on_status=False):
        self.__speed= speed
        self.__radius= radius
        self.__color= color
        self.__on_status= on_status

    def __str__(self):
        return f"Fan(speed={self.__speed}, radius={self.__radius}, color={self.__color}, on={self.__on_status})"