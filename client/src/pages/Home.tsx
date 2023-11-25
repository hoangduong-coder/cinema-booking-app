import MovieList from "../components/dashboard/MovieList"

const Home = () => {
  return (
    <div className="flex flex-col py-2 px-6">
      <MovieList isAvailable={true} />
      <MovieList isAvailable={false} />
    </div>
  )
}

export default Home
