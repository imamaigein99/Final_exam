from pydantic import BaseModel
from enum import Enum


class AppointmentStatus(str, Enum):
    OPEN = "confirmed"
    CLOSED = "closed"
    PENDING = "scheduled"

class Appointments(BaseModel):
    appointment_id: int
    patient_phone: str
    doctor_name: str
    date_timer: str
    duration: str
    reasons: str
    notes: str
    location: str
    status: AppointmentStatus = AppointmentStatus.OPEN


# class AppointmentsCreate(BaseModel):
#     patient_phone: str
#     doctor_name: str
#     date_timer: str
#     duration: str
#     reasons: str
#     notes: str
#     location: str
#     status: AppointmentStatus = AppointmentStatus.OPEN



appointment: dict[int, Appointments] = {
    0: Appointments(
        appointment_id=0, patient_phone='test test', doctor_name='Imama Igein', date_timer='2023-04-14 14:42', duration= '60M', reasons='routine check-up', notes='We need to run some test', location='virtual',  status=AppointmentStatus.OPEN)
}
