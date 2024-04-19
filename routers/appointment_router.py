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
    if location not in ["Virtual", "Onsite"]:
        raise HTTPException(status_code=400, detail="Invalid status. Please provide 'Virtual' or 'Onsite'.")
    data = AppointmentsSerivce.create_appointment(patient_phone, date_timer, duration, reasons, notes, location)
    return {'message': 'successful', 'data': data}


@appointment_router.post('/UpdateAppointmentStatus/{appointment_id}', status_code=200)
def update_appointment_status(appointment_id: int, status: str):
    if status not in ["confirmed", "closed"]:
        # If the status is not valid, raise an HTTPException with a 400 status code
        raise HTTPException(status_code=400, detail="Invalid status. Please provide 'confirmed' or 'closed'.")
    data = AppointmentsSerivce.update_appointment_status(appointment_id, status)
    return {'message': 'successful', 'data': data}