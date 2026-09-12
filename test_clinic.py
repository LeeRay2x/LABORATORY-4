import unittest
from datetime import datetime

from owner import PetOwner
from petClass import dog, cat, bird, rabbit, create_pet
from appointment import Appointment
from clinic_database import ClinicDatabase


class TestClinic(unittest.TestCase):

    def setUp(self):
        # Get the Singleton ClinicDatabase instance
        self.database = ClinicDatabase()

        # Clear previous test data
        self.database.clear()

        # Create and register an owner
        self.owner = PetOwner(
            "O001",
            "Alyssa",
            "09123456789"
        )

        self.database.register_owner(self.owner)

    def test_register_pet_owner(self):
        owner = PetOwner(
            "O002",
            "Maria",
            "09987654321"
        )

        self.database.register_owner(owner)

        self.assertEqual(
            self.database.get_owner("O002"),
            owner
        )

        self.assertEqual(
            owner.name,
            "Maria"
        )

    def test_add_pet_record(self):
        pet = PetFactory.create_pet(
            "Dog",
            "P001",
            "Buddy",
            3,
            self.owner
        )

        self.database.add_pet(pet)

        self.assertEqual(
            self.database.get_pet("P001"),
            pet
        )

        self.assertEqual(
            pet.owner,
            self.owner
        )

        self.assertIn(
            pet,
            self.owner.pets
        )

    def test_schedule_appointment(self):
        pet = PetFactory.create_pet(
            "Cat",
            "P002",
            "Milo",
            2,
            self.owner
        )

        self.database.add_pet(pet)

        appointment = Appointment(
            "A001",
            self.owner,
            pet,
            datetime(2026, 9, 15, 10, 0),
            "Regular check-up"
        )

        self.database.schedule_appointment(appointment)

        self.assertEqual(
            self.database.get_appointment("A001"),
            appointment
        )

        self.assertEqual(
            appointment.status,
            "Scheduled"
        )

    def test_cancel_appointment(self):
        pet = PetFactory.create_pet(
            "Bird",
            "P003",
            "Sunny",
            1,
            self.owner
        )

        self.database.add_pet(pet)

        appointment = Appointment(
            "A002",
            self.owner,
            pet,
            datetime(2026, 9, 15, 11, 0)
        )

        self.database.schedule_appointment(appointment)

        self.database.cancel_appointment("A002")

        self.assertEqual(
            appointment.status,
            "Cancelled"
        )

    def test_singleton_instance(self):
        another_database = ClinicDatabase()

        self.assertIs(
            self.database,
            another_database
        )


if __name__ == "__main__":
    unittest.main()
