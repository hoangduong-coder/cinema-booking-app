import { Outlet, useLocation } from "react-router-dom"

import Header from "../components/layout/Header"
import Sidebar from "../components/layout/Sidebar"
import Home from "./Home"

const Root = () => {
  const location = useLocation()
  return (
    <div className="h-screen mx-auto w-full max-w-6xl flex flex-col">
      <Sidebar />
      <div className="w-full max-w-6xl flex flex-col">
        <Header />
        <div className="w-full mt-14">
          {location.pathname !== "/" ? <Outlet /> : <Home />}
        </div>
      </div>
    </div>
  )
}

export default Root
