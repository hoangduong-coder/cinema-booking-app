import SearchBox from "../components/all-movies/SearchBox"

const AllMovies = () => {
  return (
    <div className="flex flex-col py-2 px-6">
      <h1 className="text-2xl font-bold py-2">All movies</h1>
      <SearchBox />
    </div>
  )
}

export default AllMovies
