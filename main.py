from fastapi import FastAPI
from routers.doctors_router import doctor_router
from routers.patients_router import patient_router


app = FastAPI()

app.include_router(router=doctor_router, prefix='/doctors', tags=['doctors'])
app.include_router(router=patient_router, prefix='/patients', tags=['patients'])


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8234)
