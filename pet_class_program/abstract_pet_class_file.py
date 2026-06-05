from abc import ABC, abstractmethod

class AbstractPetClass(ABC):
    @abstractmethod
    def __init__(self, name, animal_type, age):
        pass

    @abstractmethod
    def set_name():
        pass

    @abstractmethod
    def get_name():
        pass

    @abstractmethod
    def set_animal_type():
        pass

    @abstractmethod
    def get_animal_type():
        pass

    @abstractmethod
    def get_age():
        pass

    @abstractmethod
    def set_age():
        pass
