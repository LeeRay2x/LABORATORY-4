class PetOwner:
    def __init__(self, owner_id, name, contact_number):
        self.owner_id = owner_id
        self.name = name
        self.contact_number = contact_number
        self.pets = []

    def add_pet(self, pet):
        self.pets.append(pet)

    def __str__(self):
        return f"Owner ID: {self.owner_id}, Name: {self.name}, Contact: {self.contact_number}"