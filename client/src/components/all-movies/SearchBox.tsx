import "../styles.css"

import { Calendar } from "lucide-react"
import data from "../../dummy/cinema.json"

const SearchBox = () => {
  const cinemaList = [...data]
  return (
    <div className="flex flex-row w-full mb-4 space-x-2">
      <select className="bg-transparent border-b-8 border-red text-white text-sm p-2.5 focus:ring-red w-full">
        <option className="bg-black text-white p-2.5 hover:bg-red" selected>
          Choose a cinema
        </option>
        {cinemaList.map((optionValue) => (
          <option
            key={optionValue.id}
            className="bg-black text-white p-2.5 hover:bg-red"
            value={optionValue.id}
          >
            {optionValue.name}
          </option>
        ))}
      </select>
      <div className="flex flex-row border-b-8 text-white text-sm p-2.5 w-full">
        <Calendar />
        <input type="date" className="" />
      </div>
    </div>
  )
}

export default SearchBox
