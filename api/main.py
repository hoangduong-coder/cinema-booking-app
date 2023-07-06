from util.helper import convert_to_mins
from fastapi import FastAPI, Path
app = FastAPI()

film_list = {
    1: {
        "name": "Fast X",
        "length": 141,
        "release": "17.5.2023",
        "language": "English",
        "genre": ["Action"]
    },
    2: {
        "name": "Spider-Man: Across the Spider-Verse",
        "length": 140,
        "release": "31.5.2023",
        "language": "English",
        "genre": ["Action", "Adventure", "Animation"]
    },
    3: {
        "name": "Elemental",
        "length": 109,
        "release": "7.7.2023",
        "language": "English",
        "genre": ["Comedy", "Adventure", "Animation", "Family"]
    }
}


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/all-film")
async def get_all_film():
    result = []
    for i in film_list:
        film_list[i]["length"] = convert_to_mins(film_list[i]["length"])
        result.append(film_list[i])
    return result


@app.get("/get-film/{film_id}")
async def get_film(film_id: int = Path(description="Select ID of your film:")):
    film_list[film_id]["length"] = convert_to_mins(
        film_list[film_id]["length"])
    return film_list[film_id]
