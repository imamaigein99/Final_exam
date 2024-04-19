from fastapi import FastAPI
from routers.doctors_router import doctor_router
from routers.patients_router import patient_router
from routers.appointment_router import appointment_router

app = FastAPI()

app.include_router(router=doctor_router, prefix='/doctors', tags=['doctors'])
app.include_router(router=patient_router, prefix='/patients', tags=['patients'])
app.include_router(router=appointment_router, prefix='/appointment', tags=['appointment'])


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8234)
