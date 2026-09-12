from owner import PetOwner
from petClass import create_pet
from appointment import Appointment
from clinic_database import ClinicDatabase
from datetime import datetime
import random

def main():
    database = ClinicDatabase()

    while True:
        print("\n===== PAWS AND CARE VETERINARY CLINIC =====")
        print("1. Register Pet Owner")
        print("2. View Pet Owners")
        print("3. Add Pet")
        print("4. View Pets")
        print("5. Schedule Appointment")
        print("6. View Appointments")
        print("7. Cancel Appointment")
        print("8. Update Appointment Status")
        print("9. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("\nEnter Owner Name: ")
            contact_number = input("Enter Contact Number: ")

            while True:
                owner_id = "O" + str(random.randint(1000, 9999))

                if database.get_owner(owner_id) is None:
                    break

            owner = PetOwner(owner_id, name, contact_number)

            try:
                database.register_owner(owner)
                print("Pet owner registered successfully.")
                print("Generated Owner ID:", owner_id)
            except ValueError as e:
                print(e)

        elif choice == "2":
            owners = database.get_owners()

            if len(owners) == 0:
                print("No pet owners registered.")
            else:
                print("\n===== PET OWNERS =====")

                for owner in owners:
                    print(owner)

        elif choice == "3":
            pet_type = input("\nEnter Pet Type (Dog/Cat/Bird/Rabbit): ")
            name = input("Enter Pet Name: ")
            age = int(input("Enter Pet Age: "))
            owner_id = input("Enter Owner ID: ")

            owner = database.get_owner(owner_id)

            if owner is None:
                print("Owner not found.")
            else:
                breed = input("Enter Breed: ")

                while True:
                    pet_id = "P" + str(random.randint(1000, 9999))

                    if database.get_pet(pet_id) is None:
                        break

                chip_number = random.randint(100000000000000, 999999999999999)

                pet = create_pet(
                    pet_type,
                    pet_id,
                    name,
                    age,
                    owner,
                    breed,
                    chip_number
                )

                try:
                    database.add_pet(pet)
                    print("Pet added successfully.")
                    print("Generated Pet ID:", pet_id)
                    print("Generated Chip Number:", chip_number)
                except ValueError as e:
                    print(e)

        elif choice == "4":
            pets = database.get_pets()

            if len(pets) == 0:
                print("No pets registered.")
            else:
                print("\n===== PETS =====")

                for pet in pets:
                    print(pet)

        elif choice == "5":
            owner_id = input("\nEnter Owner ID: ")
            pet_id = input("Enter Pet ID: ")

            owner = database.get_owner(owner_id)
            pet = database.get_pet(pet_id)

            if owner is None:
                print("Owner not found.")
            elif pet is None:
                print("Pet not found.")
            else:
                date = input("Enter appointment date (YYYY-MM-DD): ")
                time = input("Enter appointment time (HH:MM): ")
                reason = input("Enter reason: ")

                date_time = datetime.strptime(
                    date + " " + time,
                    "%Y-%m-%d %H:%M"
                )

                while True:
                    appointment_id = "A" + str(random.randint(1000, 9999))

                    if database.get_appointment(appointment_id) is None:
                        break

                appointment = Appointment(
                    appointment_id,
                    owner,
                    pet,
                    date_time,
                    reason
                )

                try:
                    database.schedule_appointment(appointment)
                    print("Appointment scheduled successfully.")
                    print("Generated Appointment ID:", appointment_id)
                except ValueError as e:
                    print(e)

        elif choice == "6":
            appointments = database.get_appointments()

            if len(appointments) == 0:
                print("No appointments scheduled.")
            else:
                print("\n===== APPOINTMENTS =====")

                for appointment in appointments:
                    print(appointment)

        elif choice == "7":
            appointment_id = input("\nEnter Appointment ID to cancel: ")

            try:
                database.cancel_appointment(appointment_id)
                print("Appointment cancelled successfully.")
            except ValueError as e:
                print(e)

        elif choice == "8":
            appointment_id = input("\nEnter Appointment ID: ")
            status = input(
                "Enter new status (Scheduled/Completed/Cancelled): "
            )

            try:
                database.update_appointment_status(
                    appointment_id,
                    status
                )
                print("Appointment status updated successfully.")
            except ValueError as e:
                print(e)

        elif choice == "9":
            print("\nThank you for using Paws and Care Veterinary Clinic!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
