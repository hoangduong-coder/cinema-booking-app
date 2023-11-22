/* eslint-disable @typescript-eslint/no-unused-vars */

import Header from "../components/layout/Header"
import { Outlet } from "react-router-dom"
import Sidebar from "../components/layout/Sidebar"

const Root = () => {
  // const location = useLocation()
  return (
    <div className="max-h-screen mx-auto w-full max-w-6xl flex flex-col justify-center">
      <Header />
      <div className="w-full grid grid-cols-[auto,1fr] overflow-auto">
        <Sidebar />
        <Outlet />
      </div>
      {/*  */}
      {/* <div>{location.pathname !== "/" ? <Outlet /> : <Home />}</div> */}
    </div>
  )
}

export default Root
