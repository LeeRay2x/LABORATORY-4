class pet:
    def __init__(self, pet_id: str, breed: str, name: str, age: int, chip_number: int, owner):
        self.pet_id = pet_id
        self.breed = breed
        self.name = name
        self.age = age
        self.chip_number = chip_number
        self.owner = owner

    @property
    def pet_type(self):
        return self.__class__.__name__

    def __str__(self):
        return f"name: {self.name}, age: {self.age}, breed: {self.breed}, type: {self.pet_type}, chip number: {self.chip_number}, owner: {self.owner.name}"

class dog(pet):
    pass

class cat(pet):
    pass

class bird(pet):
    pass

class rabbit(pet):
    pass

def create_pet(pet_type: str, pet_id: str, name: str, age: int, owner, breed="", chip_number=0):
    pet_type = pet_type.lower()
    if pet_type == "dog":
        return dog(pet_id, breed, name, age, chip_number, owner)
    elif pet_type == "cat":
        return cat(pet_id, breed, name, age, chip_number, owner)
    elif pet_type == "bird":
        return bird(pet_id, breed, name, age, chip_number, owner)
    elif pet_type == "rabbit":
        return rabbit(pet_id, breed, name, age, chip_number, owner)
    else:
        raise ValueError(
            f"Invalid pet type: {pet_type}. Valid types are: dog, cat, bird, rabbit."
        )
