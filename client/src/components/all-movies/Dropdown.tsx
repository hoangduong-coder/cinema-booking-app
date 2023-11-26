/* eslint-disable @typescript-eslint/no-explicit-any */

import { useEffect, useRef, useState } from "react"

import { ChevronDown } from "lucide-react"

const Dropdown = ({
  dropdownList,
  defaultSelection,
}: {
  dropdownList: any[]
  defaultSelection: string
}) => {
  const [showDropdown, setShowDropdown] = useState(false)
  const selectDropdownRef = useRef<HTMLButtonElement>(null)
  const [dropdownOption, setDropdownOption] = useState<string>(defaultSelection)

  useEffect(() => {
    const handleOutsideClick = (event: MouseEvent) => {
      if (
        selectDropdownRef.current &&
        !selectDropdownRef.current.contains(event.target as Node)
      ) {
        setShowDropdown(false)
      }
    }

    document.addEventListener("click", handleOutsideClick)
    return () => {
      document.removeEventListener("click", handleOutsideClick)
    }
  }, [selectDropdownRef])
  return (
    <div className="w-full">
      <button
        className="w-full flex flex-row justify-between p-2.5 bg-transparent border-b-8 border-red text-white"
        ref={selectDropdownRef}
        onClick={() => setShowDropdown(true)}
      >
        <span>{dropdownOption}</span>
        <ChevronDown />
      </button>
      <div
        className={`absolute z-10 w-1/5 rounded-b-lg ${
          showDropdown ? "block" : "hidden"
        }`}
      >
        <div className="w-full bg-black text-white p-2.5 hover:bg-red cursor-pointer">
          {defaultSelection}
        </div>
        {dropdownList.map((dropdownItem) => (
          <button
            className="w-full bg-black text-white p-2.5 hover:bg-red cursor-pointer text-left"
            key={dropdownItem.id}
            onClick={(event) => {
              event.stopPropagation()
              setDropdownOption(dropdownItem.name)
              setShowDropdown(false)
            }}
          >
            {dropdownItem.name}
          </button>
        ))}
      </div>
    </div>
  )
}

export default Dropdown
