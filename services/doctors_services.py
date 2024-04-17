from fastapi import HTTPException
from schemas.doctors_schema import DoctorsCreate, Doctors, doctors, is_available, DoctorsStatus, DoctorsUpdate

class DoctorSerivce:


    @staticmethod
    def get_doctor_by_id(id):
        if id in doctors:
            return doctors[id]
        else: 
            return {"ResponseCode": "01", "ResponseMessage": "Doctor Does Not Exist"}
        
    @staticmethod
    def get_doctor_all_active():
        active_doctors = []
        for doctor_id, doctor in doctors.items():
            if doctor.active == DoctorsStatus.OPEN:
                active_doctors.append(doctor)
        return active_doctors
    

    @staticmethod
    def get_doctor_all_deactive():
        deactive_doctors = []
        for doctor_id, doctor in doctors.items():
            if doctor.active == DoctorsStatus.CLOSED:
                deactive_doctors.append(doctor)
        return deactive_doctors



    @staticmethod
    def create_doctors(Doctor_data: DoctorsCreate):
        # Check if the phone number already exists
        for doctor_id, doctor in doctors.items():
            if doctor.phone == Doctor_data.phone:
                return {"ResponseCode": "01", "ResponseMessage": "Doctor with the same msisdn already exists"}
        
        new_id = max(doctors.keys(), default=0) + 1

        # If the phone number does not exist, create a new doctor
        id = len(doctors)
        doctor = Doctors(
            id=new_id,
            **Doctor_data.model_dump()
        )
        doctors[id] = doctor

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
                return {"ResponseCode": "00", "ResponseMessage": "Doctor Status Updated Successfully"}
            elif doctor.status == is_available.CLOSED and doctor.active == DoctorsStatus.OPEN:
                return {"ResponseCode": "02", "ResponseMessage": "Doctor Already in Busy state"}
        else:
            # If the doctor does not exist in the dictionary
            return {"ResponseCode": "01", "ResponseMessage": "Doctor Does Not Exist"}

        # If the code reaches this point, it indicates an internal logic issue
        return {"ResponseCode": "00", "ResponseMessage": f"Doctor {doctor.name} is no longer a staff"}
    

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
                return {"ResponseCode": "00", "ResponseMessage": "Doctor Status Updated Successfully"}
            elif doctor.status == is_available.OPEN and doctor.active == DoctorsStatus.OPEN:
                return {"ResponseCode": "02", "ResponseMessage": "Doctor Already in Free state"}
        else:
            # If the doctor does not exist in the dictionary
            return {"ResponseCode": "01", "ResponseMessage": "Doctor Does Not Exist"}

        # If the code reaches this point, it indicates an internal logic issue
        return {"ResponseCode": "00", "ResponseMessage": f"Doctor {doctor.name} is no longer a staff"}
    

    @staticmethod
    def update_doctors_status(active: DoctorsStatus, doctor_id: int):
        if doctor_id in doctors: 
            doctor = doctors[doctor_id]
            # Check if the user is already in the desired state
            if active == DoctorsStatus.OPEN and doctor.active == DoctorsStatus.OPEN:
                return {"ResponseCode": "01", "ResponseMessage": f"Doctor {doctor.name} is already ENABLED"}
            elif active == DoctorsStatus.CLOSED and doctor.active == DoctorsStatus.CLOSED:
                    return {"ResponseCode": "01", "ResponseMessage": f"Doctor {doctor.name} is already DISABLED"}
                # Update the status based on the value of 'active' parameter
            elif active == DoctorsStatus.OPEN:
                doctor.active = DoctorsStatus.OPEN
                return {"ResponseCode": "00", "ResponseMessage": f"Doctor {doctor.name} is now ENABLED"}
            elif active == DoctorsStatus.CLOSED:
                doctor.active = DoctorsStatus.CLOSED
                return {"ResponseCode": "00", "ResponseMessage": f"Doctor {doctor.name} is now DISABLED"}
            else: 
                raise ValueError("Invalid value for 'active'. Please provide 'ENABLED' or 'DISABLED'.") 
        else:
            return {"ResponseCode": "02", "ResponseMessage": "Doctor does not exist"}



    @staticmethod
    def update_doctors_status_id(Doctor_data: DoctorsUpdate):
        # Check if the phone number already exists for a different doctor
        for doctor_id, doctor in doctors.items():
            if doctor.phone == Doctor_data.phone:
                # If the phone number already exists for another doctor, return an error response
                return {"ResponseCode": "01", "ResponseMessage": "Phone number already exists for another doctor"}

        # If the phone number doesn't exist for another doctor, update the doctor's status
        if Doctor_data.id in doctors:
            doctor = doctors[Doctor_data.id]
            doctor.name = Doctor_data.name
            doctor.specialization = Doctor_data.specialization
            # Return a success response
            return {"ResponseCode": "00", "ResponseMessage": f"Doctor with ID {Doctor_data.id} updated successfully"}
        else:
            # If the specified doctor ID doesn't exist, return an error response
            return {"ResponseCode": "02", "ResponseMessage": "Doctor with the specified ID does not exist"}









    # @staticmethod
    # def delete_doctors_by_id(id):
    # # Check if the Doctor ID exists
    #     if id in doctors:
    #         # Delete the doctor with the provided ID
    #         del doctors[id]
    #         return {"ResponseCode": "00", "ResponseMessage": "Doctor Deleted Successfully"}
    #     else:
    #         return {"ResponseCode": "01", "ResponseMessage": "Doctor with ID does not exist"}
