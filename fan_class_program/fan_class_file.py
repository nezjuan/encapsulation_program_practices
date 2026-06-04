from abstract_fan_class_file import Fan
from getters_file import Getters

class FanFile(Fan, Getters):

    def __init__(self, speed, radius, color, on_status=False):
        self.__speed= speed
        self.__radius= radius
        self.__color= color
        self.__on_status= on_status