from database import sql_models
from database.settings import engine
from fastapi import FastAPI

from .router import cinema, movie

app = FastAPI()
sql_models.Base.metadata.create_all(bind=engine)

app.include_router(cinema.router)
app.include_router(movie.router)


@app.get("/")
async def root():
    return {"message": "Welcome to Cinema Booking Application Server!"}
