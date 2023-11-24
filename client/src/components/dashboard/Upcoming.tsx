import "slick-carousel/slick/slick-theme.css"
import "slick-carousel/slick/slick.css"
import "./styles.css"

import { ArrowLeft, ArrowRight } from "lucide-react"

import { ElementType } from "react"
import Slider from "react-slick"
import data from "../../dummy/movie.json"

const ArrowButton = ({ Icon }: { Icon: ElementType }) => {
  return (
    <button className="transition duration-300 ease-in-out p-2 rounded-full hover:bg-red-900 hover:scale-125">
      <Icon />
    </button>
  )
}

const UpcomingFilms = () => {
  const list = [...data].filter(
    (movie) => Date.now() > Date.parse(movie.release_date)
  )
  return (
    <div className="w-full">
      <h1 className="text-2xl font-bold py-2">Coming soon</h1>
      <Slider
        slidesToShow={3}
        slidesToScroll={1}
        speed={500}
        nextArrow={<ArrowButton Icon={ArrowRight} />}
        prevArrow={<ArrowButton Icon={ArrowLeft} />}
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
          <img
            key={movie.id}
            src={movie.poster}
            alt="movie"
            className="w-[30%] px-2"
          />
        ))}
      </Slider>
    </div>
  )
}

export default UpcomingFilms
