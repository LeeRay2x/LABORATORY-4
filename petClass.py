class pet:
    def __init__(self, breed: str, name: str, age: int, chip_number: int, owner: str):
        self.breed = breed
        self.name = name
        self.age = age
        self.chip_number = chip_number
        self.owner = owner

    @property
    def pet_type(self):
        return self.__class__.__name__

    def __str__(self):
        return f"name: {self.name}, age: {self.age}, breed: {self.breed}, type: {self.pet_type}, chip number: {self.chip_number}, owner: {self.owner}"

class dog(pet):
    pass

class cat(pet):
    pass

class bird(pet):
    pass

class rabbit(pet):
    pass    


