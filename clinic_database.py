class ClinicDatabase:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ClinicDatabase, cls).__new__(cls)

            cls._instance.owners = {}
            cls._instance.pets = {}
            cls._instance.appointments = {}

        return cls._instance

    def register_owner(self, owner):
        if owner.owner_id in self.owners:
            raise ValueError("Owner ID already exists.")

        self.owners[owner.owner_id] = owner

        return owner

    def get_owner(self, owner_id):
        return self.owners.get(owner_id)

    def get_owners(self):
        return list(self.owners.values())

    def add_pet(self, pet):
        if pet.pet_id in self.pets:
            raise ValueError("Pet ID already exists.")

        if pet.owner.owner_id not in self.owners:
            raise ValueError("Owner must be registered first.")

        self.pets[pet.pet_id] = pet

        pet.owner.add_pet(pet)

        return pet

    def get_pet(self, pet_id):
        return self.pets.get(pet_id)

    def get_pets(self):
        return list(self.pets.values())

    def schedule_appointment(self, appointment):
        if appointment.appointment_id in self.appointments:
            raise ValueError("Appointment ID already exists.")

        if appointment.owner.owner_id not in self.owners:
            raise ValueError("Owner must be registered first.")

        if appointment.pet.pet_id not in self.pets:
            raise ValueError("Pet must be registered first.")

        # Check for scheduling conflicts
        for existing in self.appointments.values():
            if (
                existing.pet.pet_id == appointment.pet.pet_id
                and existing.date_time == appointment.date_time
                and existing.status == "Scheduled"
            ):
                raise ValueError(
                    "Scheduling conflict: pet already has an appointment at this time."
                )

        self.appointments[appointment.appointment_id] = appointment

        return appointment

    def get_appointment(self, appointment_id):
        return self.appointments.get(appointment_id)

    def get_appointments(self):
        return list(self.appointments.values())

    def cancel_appointment(self, appointment_id):
        appointment = self.get_appointment(appointment_id)

        if appointment is None:
            raise ValueError("Appointment not found.")

        appointment.cancel()

        return appointment

    def update_appointment_status(self, appointment_id, status):
        appointment = self.get_appointment(appointment_id)

        if appointment is None:
            raise ValueError("Appointment not found.")

        appointment.update_status(status)

        return appointment

    def clear(self):
        """Clear all records. Useful for unit testing."""
        self.owners.clear()
        self.pets.clear()
        self.appointments.clear()
