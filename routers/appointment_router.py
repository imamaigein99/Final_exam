from fastapi import APIRouter, HTTPException
from logger.logger import logger
#from schemas.appointment_schemas import Appointments, AppointmentsCreate, AppointmentStatus, appointment
from schemas.appointment_schemas import Appointments, AppointmentStatus, appointment

from services.appointment_services import AppointmentsSerivce


appointment_router = APIRouter()

@appointment_router.get('/GetAllAppointment', status_code=200)
def getAllAppointment():
        logger.info(f"All appointments fetched successfully {appointment}")
        return {'message': 'successful', 'data': appointment}


@appointment_router.get('/GetAppointmentByID/{appointment_id}', status_code=200)
def GetAppointmentByID(appointment_id: int):
    try:
        data = AppointmentsSerivce.get_appointment_by_id(appointment_id)
        logger.info(f"Appointment: {appointment_id} fetched successfully - {data}")
        return {'message': 'successful', 'data': data}
    except Exception as e:
        logger.error(f"Error fetching appointments {appointment_id}")
        raise HTTPException(status_code=500, detail="Internal Server Error")



@appointment_router.post('/CreateAppointment', status_code=201)
def CreateAppointment(patient_phone: str, date_timer: str, duration: str, reasons: str, notes: str, location: str):
    try:
        if location not in ["Virtual", "Onsite"]:
            logger.error(f"Error Creating an appointment, Please provide 'Virtual' or 'Onsite' ")
            raise HTTPException(status_code=400, detail="Invalid status. Please provide 'Virtual' or 'Onsite'.")
        data = AppointmentsSerivce.create_appointment(patient_phone, date_timer, duration, reasons, notes, location)
        logger.info(f"Appointment for {patient_phone} created successfully - {data}")
        return {'message': 'successful', 'data': data}
    except Exception as e:
        logger.error(f"Error Creating an appointment for patient {patient_phone}")
        raise HTTPException(status_code=500, detail="Internal Server Error")


@appointment_router.post('/UpdateAppointmentStatus/{appointment_id}', status_code=200)
def update_appointment_status(appointment_id: int, status: str):
    try:
        if status not in ["confirmed", "closed"]:
            logger.error(f"Error Updating an appointment {appointment_id}, Please provide 'confirmed' or 'closed' ")
            raise HTTPException(status_code=400, detail="Invalid status. Please provide 'confirmed' or 'closed'.")
        data = AppointmentsSerivce.update_appointment_status(appointment_id, status)
        logger.info(f"Appointment for {appointment_id} Updated successfully - {data}")
        return {'message': 'successful', 'data': data}
    except Exception as e:
        logger.error(f"Error Updating an appointment for patient {appointment_id}")
        raise HTTPException(status_code=500, detail="Internal Server Error")