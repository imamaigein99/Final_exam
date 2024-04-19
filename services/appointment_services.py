from fastapi import HTTPException
from logger.logger import logger
import time
from schemas.appointment_schemas import Appointments, AppointmentStatus, appointment
from schemas.doctors_schema import doctors, Doctors
from services.doctors_services import DoctorSerivce

class AppointmentsSerivce:


    @staticmethod
    def get_appointment_by_id(appointment_id):
        if appointment_id in appointment:
            return appointment[appointment_id]
        else: 
            logger.error("Appointment with ID %s does not exist", appointment_id)
            return {"ResponseCode": "01", "ResponseMessage": "Appointment Does Not Exist"}
        
        
    @staticmethod
    def create_appointment(patient_phone: str, date_timer: str, duration: str, reasons: str, notes: str, location: str):
        timestamp_ms = int(time.time() * 1000)
        free_doctor = DoctorSerivce.find_free_doctor()
        #print (free_doctor)
        if free_doctor is None:
            logger.warning("No free doctors available at the moment.")
            return {"ResponseCode": "01", "ResponseMessage": "There are no Free Doctors at the moment"}
    
        appointment_id = timestamp_ms
        new_appointment = Appointments(
            appointment_id=appointment_id, 
            patient_phone=patient_phone,
            doctor_name=free_doctor.name,
            date_timer=date_timer,
            duration=duration,
            reasons=reasons,
            notes=notes,
            location=location,
            status="scheduled"
        )

        appointment[appointment_id] = new_appointment
        DoctorSerivce.update_doctors_status_busy(free_doctor.id)
        logger.info("Appointment created with ID %s and doctor %s", appointment_id, free_doctor.name)
        return {"ResponseCode": "00", "ResponseMessage": f"Appointment: {appointment_id} has been scheduled with {free_doctor.name}"}

    
    # @staticmethod
    # def create_appointment(patient_phone: str, date_timer: str, duration: str, reasons: str, notes: str, location: str):
    #     timestamp_ms = int(time.time() * 1000)

    #     # Check if the phone number already exists in appointments
    #     for appointment_id, appointment in appointments.items():
    #         if appointment.patient_phone == patient_phone:
    #             logger.warning("Appointment creation failed. Phone number '%s' already exists.", patient_phone)
    #             return {"ResponseCode": "02", "ResponseMessage": "Phone number already exists. Cannot create appointment."}

    #     free_doctor = DoctorSerivce.find_free_doctor()
    #     if free_doctor is None:
    #         logger.warning("No free doctors available at the moment.")
    #         return {"ResponseCode": "01", "ResponseMessage": "There are no Free Doctors at the moment"}

    #     appointment_id = timestamp_ms
    #     new_appointment = Appointments(
    #         appointment_id=appointment_id, 
    #         patient_phone=patient_phone,
    #         doctor_name=free_doctor.name,
    #         date_timer=date_timer,
    #         duration=duration,
    #         reasons=reasons,
    #         notes=notes,
    #         location=location,
    #         status="scheduled"
    #     )

    #     appointment[appointment_id] = new_appointment
    #     DoctorSerivce.update_doctors_status_busy(free_doctor.id)
    #     logger.info("Appointment created with ID %s and doctor %s", appointment_id, free_doctor.name)
    #     return {"ResponseCode": "00", "ResponseMessage": f"Appointment: {appointment_id} has been scheduled with {free_doctor.name}"}


    @staticmethod
    def update_appointment_status(appointment_id: int, status: AppointmentStatus):
        if appointment_id not in appointment:
            logger.error("Appointment with ID %s does not exist", appointment_id)
            return {"ResponseCode": "01", "ResponseMessage": "Appointment does not exist"}

        appointment_instance = appointment[appointment_id]

        if status == AppointmentStatus.OPEN:
            if appointment_instance.status == AppointmentStatus.OPEN:
                logger.warning("Appointment with ID %s is already confirmed", appointment_id)
                return {"ResponseCode": "01", "ResponseMessage": "Appointment status cannot be updated to CONFIRMED again."}
            else:
                appointment_instance.status = AppointmentStatus.OPEN
                logger.info("Appointment with ID %s updated to Confirm state", appointment_id)
                return {"ResponseCode": "00", "ResponseMessage": f"Appointment: {appointment_id} updated to Confirm state."}
        elif status == AppointmentStatus.CLOSED:
            if appointment_instance.status == AppointmentStatus.CLOSED:
                logger.warning("Appointment with ID %s is already closed", appointment_id)
                return {"ResponseCode": "01", "ResponseMessage": "Appointment status cannot be updated from CLOSED to CLOSED."}
            else:
                appointment_instance.status = AppointmentStatus.CLOSED
                logger.info("Appointment with ID %s updated to Closed state", appointment_id)
                return {"ResponseCode": "00", "ResponseMessage": f"Appointment: {appointment_id} updated to Closed state."}
        else:
            logger.error("Invalid appointment status: %s", status)
            return {"ResponseCode": "02", "ResponseMessage": "Invalid appointment status."}





