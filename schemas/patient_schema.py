from pydantic import BaseModel
from enum import Enum
from decimal import Decimal


class PatientsStatus(str, Enum):
    OPEN = "ENABLED"
    CLOSED = "DISABLED"

class Patients(BaseModel):
    id: int
    name: str
    age: int
    sex: str
    weight: str
    height: str
    phone: str
    active: PatientsStatus = PatientsStatus.OPEN


class PatientsCreate(BaseModel):
    name: str
    age: int
    sex: str
    weight: str
    height: str
    phone: str
    active: PatientsStatus = PatientsStatus.OPEN

class PatientsUpdate(BaseModel):
    id: int
    name: str
    age: int
    sex: str
    weight: str
    height: str
    phone: str


patients: dict[int, Patients] = {
    0: Patients(
        id=0, name='Kunle Elusade', age=76, sex='male',weight= '58kg', height='180cm', phone= '08068632113',  active='ENABLED'),
    1: Patients(
        id=1, name='Kunle Elusade', age=76, sex='male',weight= '58kg', height='180cm', phone= '08068632113',  active='ENABLED'),
    2: Patients(
        id=2, name='Kunle Elusade', age=76, sex='male',weight= '58kg', height='180cm', phone= '08068632113',  active='ENABLED'),
}
