import "react-calendar/dist/Calendar.css"

import { useEffect, useRef, useState } from "react"

import Calendar from "react-calendar"
import cinemaList from "../../dummy/cinema.json"
import Dropdown from "./Dropdown"

const SearchBox = () => {
  const calendarRef = useRef<HTMLDivElement>(null)

  const [newDate, setNewDate] = useState()
  const [showCalendar, setShowCalendar] = useState(false)

  const sortByOptionList = [
    { id: "name", name: "Name (A to Z)" },
    { id: "trending", name: "Trending" },
    { id: "rating", name: "Highest rating" },
    { id: "date", name: "Latest publication date" },
  ]

  useEffect(() => {
    const handleOutsideClick = (event: MouseEvent) => {
      if (
        calendarRef.current &&
        !calendarRef.current.contains(event.target as Node)
      ) {
        setShowCalendar(false)
      }
    }

    document.addEventListener("click", handleOutsideClick)
    return () => {
      document.removeEventListener("click", handleOutsideClick)
    }
  }, [calendarRef])

  return (
    <div className="flex flex-col sm:flex-row w-full mb-4 sm:space-x-2">
      <Dropdown dropdownList={cinemaList} defaultSelection="Select a cinema" />
      <div className="w-full" ref={calendarRef}>
        <input
          type="text"
          className="appearance-none w-full bg-transparent border-b-8 text-white p-2.5 border-red"
          placeholder="Select date"
          onClick={() => setShowCalendar(true)}
          value={newDate ? new Date(newDate).toLocaleDateString("en-GB") : ""}
        />
        <Calendar
          onChange={(date) => {
            setNewDate(date)
          }}
          value={newDate}
          className={showCalendar ? "block" : "hidden"}
        />
      </div>
      <Dropdown dropdownList={sortByOptionList} defaultSelection="Sort by" />
    </div>
  )
}

export default SearchBox
