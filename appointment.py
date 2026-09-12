from datetime import datetime


class Appointment:
    VALID_STATUSES = ("Scheduled", "Completed", "Cancelled")

    def __init__(self, appointment_id, owner, pet, date_time, reason=""):
        self.appointment_id = appointment_id
        self.owner = owner
        self.pet = pet
        self.date_time = date_time
        self.reason = reason
        self.status = "Scheduled"

    def update_status(self, status):
        if status not in self.VALID_STATUSES:
            raise ValueError("Invalid appointment status.")

        self.status = status

    def cancel(self):
        self.status = "Cancelled"

    def __str__(self):
        if isinstance(self.date_time, datetime):
            date_text = self.date_time.strftime("%Y-%m-%d %H:%M")
        else:
            date_text = str(self.date_time)

        return (
            f"Appointment ID: {self.appointment_id}, "
            f"Pet: {self.pet.name}, "
            f"Owner: {self.owner.name}, "
            f"Date: {date_text}, "
            f"Status: {self.status}"
        )