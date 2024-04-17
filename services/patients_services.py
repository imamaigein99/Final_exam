from schemas.patient_schema import PatientsCreate, Patients, PatientsStatus, patients, PatientsUpdate

class PatientsSerivce:
     

    @staticmethod
    def get_patient_by_id(id):
        if id in patients:
            return patients[id]
        else: 
            return {"ResponseCode": "01", "ResponseMessage": "Patient Does Not Exist"}
        
        
    @staticmethod
    def get_patient_by_msisdn(phone):  
        matching_patients = []
        for patient_id, patient in patients.items():
            if phone == patient.phone:
                matching_patients.append(patient)
        if matching_patients:
            return matching_patients
        else:
            return {"ResponseCode": "01", "ResponseMessage": "Patient Does Not Exist"}
    

    @staticmethod
    def create_patient(patient_data: PatientsCreate):
    # Check if the phone number already exists
        for patient_id, patient in patients.items():  # Corrected 'patient' to 'patients'
            if patient.phone == patient_data.phone:
                return {"ResponseCode": "01", "ResponseMessage": "Patient with the same msisdn already exists"}
    
        new_id = max(patients.keys(), default=0) + 1

        
        patient_instance = Patients(
            id=new_id,
            **patient_data.model_dump()
        )
        patients[new_id] = patient_instance 

        return {"ResponseCode": "00", "ResponseMessage": "Patient Created Successfully"}
    

    @staticmethod
    def update_patient_status(active: PatientsStatus, patient_id: int):
        if patient_id in patients: 
            patient = patients[patient_id]
            # Check if the user is already in the desired state
            if active == PatientsStatus.OPEN and patient.active == PatientsStatus.OPEN:
                return {"ResponseCode": "01", "ResponseMessage": f"Patient {patient.name} is already ENABLED"}
            elif active == PatientsStatus.CLOSED and patient.active == PatientsStatus.CLOSED:
                    return {"ResponseCode": "01", "ResponseMessage": f"Patient {patient.name} is already DISABLED"}
                # Update the status based on the value of 'active' parameter
            elif active == PatientsStatus.OPEN:
                patient.active = PatientsStatus.OPEN
                return {"ResponseCode": "00", "ResponseMessage": f"Patient {patient.name} is now ENABLED"}
            elif active == PatientsStatus.CLOSED:
                patient.active = PatientsStatus.CLOSED
                return {"ResponseCode": "00", "ResponseMessage": f"Patient {patient.name} is now DISABLED"}
            else: 
                raise ValueError("Invalid value for 'active'. Please provide 'ENABLED' or 'DISABLED'.") 
        else:
            return {"ResponseCode": "02", "ResponseMessage": "Patient does not exist"}


    @staticmethod
    def update_patients_status_id(patient_data: PatientsUpdate):
        # Check if the phone number already exists for a different doctor
        for patient_id, patient in patients.items():
            if patient.phone == patient_data.phone:
                # If the phone number already exists for another doctor, return an error response
                return {"ResponseCode": "01", "ResponseMessage": "Phone number already exists for another Patient"}

        # If the phone number doesn't exist for another doctor, update the doctor's status
        if patient_data.id in patients:
            patient = patients[patient_data.id]
            patient.name = patient_data.name
            patient.age = patient_data.age
            patient.sex = patient_data.sex
            patient.weight = patient_data.weight
            patient.height = patient_data.height
            patient.phone = patient_data.phone
            # Return a success response
            return {"ResponseCode": "00", "ResponseMessage": f"Patient with ID {patient_data.id} updated successfully"}
        else:
            # If the specified doctor ID doesn't exist, return an error response
            return {"ResponseCode": "02", "ResponseMessage": "Patient with the specified ID does not exist"}