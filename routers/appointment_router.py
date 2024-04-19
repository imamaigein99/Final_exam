from fastapi import APIRouter, HTTPException
#from schemas.appointment_schemas import Appointments, AppointmentsCreate, AppointmentStatus, appointment
from schemas.appointment_schemas import Appointments, AppointmentStatus, appointment

from services.appointment_services import AppointmentsSerivce

appointment_router = APIRouter()

@appointment_router.get('/GetAllAppointment', status_code=200)
def getAllAppointment():
    return {'message': 'successful', 'data': appointment}

@appointment_router.get('/GetAppointmentByID/{appointment_id}', status_code=200)
def GetAppointmentByID(appointment_id: int):
    data = AppointmentsSerivce.get_appointment_by_id(appointment_id)
    return {'message': 'successful', 'data': data}

@appointment_router.post('/CreateAppointment', status_code=201)
def CreateAppointment(patient_phone: str, date_timer: str, duration: str, reasons: str, notes: str, location: str):
    data = AppointmentsSerivce.create_appointment(patient_phone, date_timer, duration, reasons, notes, location)
    return {'message': 'successful', 'data': data}