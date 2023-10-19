from fastapi import FastAPI, Path
from util.helper import convert_to_mins

app = FastAPI()

movie_list = {
    1: {
        "name": "Fast X",
        "length": 141,
        "release": "7.5.2023",
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


@app.get("/all-movie")
async def get_all_movie():
    result = []
    for i in movie_list:
        movie_list[i]["length"] = convert_to_mins(movie_list[i]["length"])
        result.append(movie_list[i])
    return result


@app.get("/get-movie/{search_movie_id}")
async def get_movie_by_id(search_movie_id: int = Path(description="Select ID of your movie:")):
    for movie_id in movie_list:
        if (search_movie_id == movie_id):
            movie_list[search_movie_id]["length"] = convert_to_mins(
                movie_list[search_movie_id]["length"])
            return movie_list[search_movie_id]
    return {"Data": "Not found"}
