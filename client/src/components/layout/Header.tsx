/* eslint-disable @typescript-eslint/ban-ts-comment */
/* eslint-disable react-hooks/exhaustive-deps */

import { AlignJustify, ShoppingCart, User } from "lucide-react"
import { useEffect, useRef } from "react"
import { useDispatch, useSelector } from "react-redux"

import { Link } from "react-router-dom"
import { useScreenSize } from "../../helpers"
import { toggleSidebar } from "../../redux/pageStatusSlice"
import { RootState } from "../../redux/store"
import Logo from "./Logo"

const Header = () => {
  const dispatch = useDispatch()
  const screenSize = useScreenSize()
  const sidebarRef = useRef<HTMLButtonElement>(null)
  const showSidebar = useSelector(
    (state: RootState) => state.pageStatus.showSidebar
  )

  useEffect(() => {
    const handleClickSidebarOutside = (event: MouseEvent): void => {
      if (
        sidebarRef.current &&
        showSidebar &&
        !sidebarRef.current.contains(event.target as HTMLButtonElement)
      ) {
        dispatch(toggleSidebar())
      }
    }
    //@ts-ignore
    document.addEventListener("mousedown", handleClickSidebarOutside)
    return () => {
      //@ts-ignore
      document.removeEventListener("mousedown", handleClickSidebarOutside)
    }
  }, [sidebarRef, showSidebar])

  return (
    <div className="w-full max-w-6xl fixed flex flex-row py-2 px-6 justify-between center">
      {screenSize.width <= 640 ? (
        <button
          className="p-2 rounded-full hover:bg-red-900"
          onClick={() => dispatch(toggleSidebar())}
          ref={sidebarRef}
        >
          <AlignJustify />
        </button>
      ) : (
        <Logo />
      )}
      <div className="flex flex-row center space-x-4">
        <Link
          to={"/"}
          className="p-2 rounded-lg hover:bg-red-900 hidden sm:block"
        >
          Manage movie
        </Link>
        <Link to={"/"} className="p-2 rounded-full hover:bg-red-900">
          <ShoppingCart />
        </Link>
        <Link to={"/"} className="p-2 rounded-full hover:bg-red-900">
          <User />
        </Link>
      </div>
    </div>
  )
}

export default Header
