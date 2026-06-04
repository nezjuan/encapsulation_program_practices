from abstract_fan_class_file import Fan

class FanFile(Fan):

    def __init__(self, speed, radius, color, on_status=False):
        self.__speed= speed
        self.__radius= radius
        self.__color= color
        self.__on_status= on_status

    
