from fastapi import FastAPI
from routers.doctors_router import doctor_router


app = FastAPI()

app.include_router(router=doctor_router, prefix='/doctors', tags=['doctors'])


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8234)
