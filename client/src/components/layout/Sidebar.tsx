/* eslint-disable @typescript-eslint/ban-ts-comment */
/* eslint-disable react-hooks/exhaustive-deps */

import "./layout.css"

import { Clapperboard, HomeIcon, Settings, User } from "lucide-react"
import { ElementType, MouseEvent, useEffect, useRef } from "react"
import { useDispatch, useSelector } from "react-redux"

import { Link } from "react-router-dom"
import { toggleSidebar } from "../../redux/pageStatusSlice"
import { RootState } from "../../redux/store"
import Logo from "./Logo"

const SidebarItem = ({
  Icon,
  title,
  url,
}: {
  Icon: ElementType
  title: string
  url: string
}) => {
  return (
    <Link
      to={url}
      className="p-4 flex flex-row space-x-3 align-center hover:bg-red transition duration-300"
    >
      <Icon className="w-7 h-7" />
      <div className="text-base">{title}</div>
    </Link>
  )
}

const Sidebar = () => {
  const sidebarRef = useRef<HTMLElement>(null)
  const showSidebar = useSelector(
    (state: RootState) => state.pageStatus.showSidebar
  )
  const dispatch = useDispatch()

  useEffect(() => {
    const handleClickSidebarOutside = (
      event: MouseEvent<Element, MouseEvent>
    ): void => {
      if (
        sidebarRef.current &&
        !sidebarRef.current.contains(event.target as Node)
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
  }, [sidebarRef])

  return (
    <aside
      className={`h-screen fixed z-[10] bg-black left-0 overflow-y-auto sm:hidden sidebar-slide-in ${
        showSidebar ? "visible" : ""
      }`}
      ref={sidebarRef}
    >
      <div className="py-6">
        <div className="pb-4 px-4">
          <Logo />
        </div>
        <SidebarItem Icon={HomeIcon} title="Home" url="/" />
        <SidebarItem
          Icon={Clapperboard}
          title="Manage movie"
          url="manage-movie"
        />
        <SidebarItem Icon={User} title="Profile" url="profile" />
        <SidebarItem Icon={Settings} title="Setting" url="setting" />
      </div>
      <div className="absolute inset-x-0 bottom-0 py-6 flex justify-center align-center px-4">
        <Link
          to="log-in"
          className="text-center bg-red-900 rounded-lg py-2 w-full hover:bg-red transition duration-300"
        >
          Sign in
        </Link>
      </div>
    </aside>
  )
}

export default Sidebar
