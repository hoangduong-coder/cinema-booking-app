import { Clock } from "lucide-react"
import { Link } from "react-router-dom"
import { convertTime } from "../../helpers"
import { Movie } from "../../types/main"

const description =
  "Bali is predominantly a Hindu country. Bali is known for its elaborate, traditional dancing. The dancing is inspired by its Hindi beliefs. Most of the dancing portrays tales of good versus evil. To watch the dancing is a breathtaking experience. Lombok has some impressive points of interest – the majestic Gunung Rinjani is an active volcano. It is the second highest peak in Indonesia. Art is a Balinese passion. Batik paintings and carved statues make popular souvenirs. Artists can be seen whittling and painting on the streets, particularly in Ubud. It is easy to appreciate each island as an attractive tourist destination. Majestic scenery; rich culture; white sands and warm, azure waters draw visitors like magnets every year. Snorkelling and diving around the nearby Gili Islands is magnificent. Marine fish, starfish, turtles and coral reef are present in abundance. Bali and Lombok are part of the Indonesian archipelago. Bali has some spectacular temples. The most significant is the Mother Temple, Besakih. The inhabitants of Lombok are mostly Muslim with a Hindu minority. Lombok remains the most understated of the two islands. Lombok has several temples worthy of a visit, though they are less prolific. Bali and Lombok are neighbouring islands."

const MovieInfo = ({ movie }: { movie: Movie }) => {
  return (
    <div className="w-full flex flex-row my-4">
      <div className="w-1/4">
        <img src={movie.poster} alt="poster" />
      </div>
      <div className="w-3/4 ml-3 flex flex-col">
        <h1 className="text-2xl font-bold	">
          {String(movie.name).toUpperCase()}
        </h1>
        <p className="line-clamp-3 text-justify">{description}</p>
        <div className="w-full flex flex-row my-1 space-x-2">
          {movie.genres.map((genre) => (
            <p className="p-2 bg-gray-500 hover:bg-red-900 hover:text-white rounded-md cursor-default transition duration-200">
              {genre}
            </p>
          ))}
        </div>
        <div className="w-full grid grid-cols-2 gap-2 my-1">
          <div className="border-r-2 flex flex-row items-center">
            <Clock />
            <span className="ml-2">{convertTime(movie.length)}</span>
          </div>
          <div className="flex flex-row items-center">
            Premiere from{" "}
            {new Date(movie.release_date).toLocaleDateString("en-GB")}
          </div>
        </div>
        <div className="w-full space-x-2 flex flex-row my-1">
          <Link
            className="bg-red rounded-lg grow p-2 text-center hover:bg-red-900 transition duration-300"
            to="/"
          >
            More details
          </Link>
          <Link
            className="bg-red rounded-lg grow p-2 text-center hover:bg-red-900 transition duration-300"
            to="/"
          >
            Tickets
          </Link>
        </div>
      </div>
    </div>
  )
}

export default MovieInfo
