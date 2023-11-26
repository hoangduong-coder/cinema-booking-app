import MovieInfo from "../components/all-movies/MovieInfo"
import SearchBox from "../components/all-movies/SearchBox"
import movieList from "../dummy/movie.json"

const AllMovies = () => {
  return (
    <div className="flex flex-col py-2 px-6">
      <h1 className="text-3xl font-bold py-2">All movies</h1>
      <SearchBox />
      {movieList.map((movie) => (
        <MovieInfo key={movie.id} movie={movie} />
      ))}
    </div>
  )
}

export default AllMovies
