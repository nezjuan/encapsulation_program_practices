from abc import ABC, abstractmethod

class Car(ABC):
    @abstractmethod
    def __init__(self, year_model, make, speed=0):
        pass
    
    @abstractmethod
    def accelerate(self):
        pass

    @abstractmethod
    def brake(self):
        pass
    
    @abstractmethod
    def get_speed(self):
        pass