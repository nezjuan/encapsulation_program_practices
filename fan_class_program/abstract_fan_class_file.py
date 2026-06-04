from abc import ABC,abstractmethod

class Fan():
    slow=1
    medium=2
    fast=3

    @abstractmethod
    def __init__(self, speed, radius, color, on_status = False):
        pass

    @abstractmethod
    def get_speed(self):
        pass
    @abstractmethod
    def get_radius(self):
        pass
    @abstractmethod
    def get_color(self):
        pass
    @abstractmethod
    def get_on_status(self):
        pass

    @abstractmethod
    def set_speed(self):
        pass
    @abstractmethod
    def set_radius(self):
        pass
    @abstractmethod
    def set_color(self):
        pass
    @abstractmethod
    def get_on_status(self):
        pass