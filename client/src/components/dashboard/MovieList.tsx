import "slick-carousel/slick/slick-theme.css"
import "slick-carousel/slick/slick.css"
import "../styles.css"

import { ArrowLeft, ArrowRight } from "lucide-react"

import Slider from "react-slick"
import data from "../../dummy/movie.json"

//Must put the arrows inside of a stateless component and reference them in the settings
const ArrowNextButton = (props) => {
  const { onClick } = props
  return (
    <button
      className="transition duration-300 ease-in-out p-2 rounded-full hover:bg-red-900 hover:scale-125"
      onClick={onClick}
    >
      <ArrowRight />
    </button>
  )
}

const ArrowPreviousButton = (props) => {
  const { onClick } = props
  return (
    <button
      className="transition duration-300 ease-in-out p-2 rounded-full hover:bg-red-900 hover:scale-125"
      onClick={onClick}
    >
      <ArrowLeft />
    </button>
  )
}

const MovieList = ({ isAvailable }: { isAvailable: boolean }) => {
  const list = [...data].filter((movie) =>
    !isAvailable
      ? Date.now() > Date.parse(movie.release_date)
      : Date.now() <= Date.parse(movie.release_date)
  )
  return (
    <div className="w-full mb-4">
      <h1 className="text-2xl font-bold py-2">
        {isAvailable ? "Now playing" : "Coming soon"}
      </h1>
      <Slider
        slidesToShow={3}
        slidesToScroll={1}
        dots={true}
        speed={500}
        nextArrow={<ArrowNextButton />}
        prevArrow={<ArrowPreviousButton />}
        responsive={[
          {
            breakpoint: 768,
            settings: {
              slidesToShow: 2,
              slidesToScroll: 1,
            },
          },
        ]}
      >
        {list.map((movie) => (
          <div key={movie.id} className="w-[30%] px-2">
            <img src={movie.poster} alt="movie" className="w-full" />
          </div>
        ))}
      </Slider>
    </div>
  )
}

export default MovieList
