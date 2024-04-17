from pydantic import BaseModel
from enum import Enum


class PatientsStatus(str, Enum):
    OPEN = "ENABLED"
    CLOSED = "DISABLED"

class Patients(BaseModel):
    id: int
    name: str
    age: str
    sex: str
    weight: str
    height: str
    phone: str
    active: PatientsStatus = PatientsStatus.OPEN


class PatientsCreate(BaseModel):
    name: str
    age: str
    sex: str
    weight: str
    height: str
    phone: str
    active: PatientsStatus = PatientsStatus.OPEN