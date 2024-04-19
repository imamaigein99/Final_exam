from fastapi import HTTPException
from logger.logger import logger
from schemas.doctors_schema import DoctorsCreate, Doctors, doctors, is_available, DoctorsStatus, DoctorsUpdate

class DoctorSerivce:


    @staticmethod
    def get_doctor_by_id(id):
        if id in doctors:
            logger.info("Doctor with ID %s exist", id)
            return doctors[id]
        else:
            logger.error("Doctor with ID %s does not exist", id)
            return {"ResponseCode": "01", "ResponseMessage": "Doctor Does Not Exist"}
        
    @staticmethod
    def get_doctor_all_active():
        active_doctors = []
        for doctor_id, doctor in doctors.items():
            if doctor.active == DoctorsStatus.OPEN:
                active_doctors.append(doctor)
        logger.info("All Active doctors fetched -- Successfully ")
        return active_doctors
    logger.error("All Active doctors fetched -- Failed")

    @staticmethod
    def get_doctor_all_deactive():
        deactive_doctors = []
        for doctor_id, doctor in doctors.items():
            if doctor.active == DoctorsStatus.CLOSED:
                deactive_doctors.append(doctor)
        logger.info("All Deactive doctors fetched -- Successfully ")        
        return deactive_doctors
    logger.error("All Deactive doctors fetched -- Failed")



    @staticmethod
    def create_doctors(Doctor_data: DoctorsCreate):
        # Check if the phone number already exists
        for doctor_id, doctor in doctors.items():
            if doctor.phone == Doctor_data.phone:
                logger.warning(f"Doctor with the same msisdn already exists {Doctor_data}")
                return {"ResponseCode": "01", "ResponseMessage": "Doctor with the same msisdn already exists"}
        
        new_id = max(doctors.keys(), default=0) + 1

        # If the phone number does not exist, create a new doctor
        id = len(doctors)
        doctor = Doctors(
            id=new_id,
            **Doctor_data.model_dump()
        )
        doctors[id] = doctor

        logger.info(f"Doctor Created Successfully -- {doctor.name} ")
        return {"ResponseCode": "00", "ResponseMessage": "Doctor Created Successfully"}
    


    @staticmethod
    def update_doctors_status_busy(id):
        # Check if the doctor exists in the dictionary
        if id in doctors:
            # Access the doctor object using the id
            doctor = doctors[id]
        
            # Check the current status of the doctor
            if doctor.status == is_available.OPEN and doctor.active == DoctorsStatus.OPEN:
                # Update the status to "BUSY"
                doctor.status = is_available.CLOSED
                logger.info(f"Doctor {doctor.name} Status Updated Successfully") 
                return {"ResponseCode": "00", "ResponseMessage": "Doctor Status Updated Successfully"}
            elif doctor.status == is_available.CLOSED and doctor.active == DoctorsStatus.OPEN:
                logger.error(f"Doctor {doctor.name} already in Busy state.") 
                return {"ResponseCode": "02", "ResponseMessage": "Doctor Already in Busy state"}
        else:
            # If the doctor does not exist in the dictionary
            logger.error(f"Doctor Does Not Exist") 
            return {"ResponseCode": "01", "ResponseMessage": "Doctor Does Not Exist"}

        # If the code reaches this point, it indicates an internal logic issue
        logger.error(f"Doctor {doctor.name} is no longer a staff") 
        return {"ResponseCode": "05", "ResponseMessage": f"Doctor {doctor.name} is no longer a staff"}
    

    @staticmethod
    def update_doctors_status_free(id):
        # Check if the doctor exists in the dictionary
        if id in doctors:
            # Access the doctor object using the id
            doctor = doctors[id]
        
            # Check the current status of the doctor
            if doctor.status == is_available.CLOSED and doctor.active == DoctorsStatus.OPEN:
                # Update the status to "BUSY"
                doctor.status = is_available.OPEN
                logger.info(f"Doctor {doctor.name} Status Updated Successfully") 
                return {"ResponseCode": "00", "ResponseMessage": "Doctor Status Updated Successfully"}
            elif doctor.status == is_available.OPEN and doctor.active == DoctorsStatus.OPEN:
                logger.info(f"Doctor {doctor.name} Already in Free state") 
                return {"ResponseCode": "02", "ResponseMessage": "Doctor Already in Free state"}
        else:
            # If the doctor does not exist in the dictionary
            logger.info(f"Doctor Does Not Exist") 
            return {"ResponseCode": "01", "ResponseMessage": "Doctor Does Not Exist"}

        # If the code reaches this point, it indicates an internal logic issue
        logger.error(f"Doctor {doctor.name} is no longer a staff") 
        return {"ResponseCode": "05", "ResponseMessage": f"Doctor {doctor.name} is no longer a staff"}
    

    @staticmethod
    def update_doctors_status(active: DoctorsStatus, doctor_id: int):
        if doctor_id in doctors: 
            doctor = doctors[doctor_id]
            # Check if the user is already in the desired state
            if active == DoctorsStatus.OPEN and doctor.active == DoctorsStatus.OPEN:
                logger.warning(f"Doctor {doctor.name} is already ENABLED") 
                return {"ResponseCode": "01", "ResponseMessage": f"Doctor {doctor.name} is already ENABLED"}
            elif active == DoctorsStatus.CLOSED and doctor.active == DoctorsStatus.CLOSED:
                    logger.warning(f"Doctor {doctor.name} is already DISABLED") 
                    return {"ResponseCode": "01", "ResponseMessage": f"Doctor {doctor.name} is already DISABLED"}
                # Update the status based on the value of 'active' parameter
            elif active == DoctorsStatus.OPEN:
                doctor.active = DoctorsStatus.OPEN
                logger.warning(f"Doctor {doctor.name} is now ENABLED") 
                return {"ResponseCode": "00", "ResponseMessage": f"Doctor {doctor.name} is now ENABLED"}
            elif active == DoctorsStatus.CLOSED:
                doctor.active = DoctorsStatus.CLOSED
                logger.warning(f"Doctor {doctor.name} is now DISABLED") 
                return {"ResponseCode": "00", "ResponseMessage": f"Doctor {doctor.name} is now DISABLED"}
            else: 
                logger.error(f"Invalid value for 'active'. Please provide 'ENABLED' or 'DISABLED'") 
                raise ValueError("Invalid value for 'active'. Please provide 'ENABLED' or 'DISABLED'.") 
        else:
            logger.warning(f"Doctor does not exist")
            return {"ResponseCode": "02", "ResponseMessage": "Doctor does not exist"}



    @staticmethod
    def update_doctors_status_id(Doctor_data: DoctorsUpdate):
        # Check if the phone number already exists for a different doctor
        for doctor_id, doctor in doctors.items():
            if doctor.phone == Doctor_data.phone:
                # If the phone number already exists for another doctor, return an error response
                logger.warning(f"{doctor.phone} Phone number already exists for another doctor")
                return {"ResponseCode": "01", "ResponseMessage": "Phone number already exists for another doctor"}

        # If the phone number doesn't exist for another doctor, update the doctor's status
        if Doctor_data.id in doctors:
            doctor = doctors[Doctor_data.id]
            doctor.name = Doctor_data.name
            doctor.specialization = Doctor_data.specialization
            # Return a success response
            logger.info(f"Doctor with ID {Doctor_data.id} updated successfully")
            return {"ResponseCode": "00", "ResponseMessage": f"Doctor with ID {Doctor_data.id} updated successfully"}
        else:
            logger.info(f"Doctor with the specified ID does not exist")
            return {"ResponseCode": "02", "ResponseMessage": "Doctor with the specified ID does not exist"}
        

    @staticmethod
    def find_free_doctor():
        # Initialize an empty list to store free doctors
        free_doctors = []

        # Iterate over the doctors dictionary to find free doctors
        for doctor_id, doctor in doctors.items():
            if doctor.status == is_available.OPEN and doctor.active == DoctorsStatus.OPEN:
                logger.info(f"Check free Doctor passed to the Appointment class") 
                return doctor
        return None


    # @staticmethod
    # def delete_doctors_by_id(id):
    # # Check if the Doctor ID exists
    #     if id in doctors:
    #         # Delete the doctor with the provided ID
    #         del doctors[id]
    #         return {"ResponseCode": "00", "ResponseMessage": "Doctor Deleted Successfully"}
    #     else:
    #         return {"ResponseCode": "01", "ResponseMessage": "Doctor with ID does not exist"}
