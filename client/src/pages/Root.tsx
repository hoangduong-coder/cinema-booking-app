import { Outlet } from "react-router-dom"
import Header from "../components/layout/Header"
import Sidebar from "../components/layout/Sidebar"

const Root = () => {
  // const location = useLocation()
  return (
    <div className="h-screen mx-auto w-full max-w-6xl flex flex-col overflow-hidden">
      <Header />
      <div className="w-full flex h-full">
        <Sidebar />
        <Outlet />
      </div>
      {/* <div>{location.pathname !== "/" ? <Outlet /> : <Home />}</div> */}
    </div>
  )
}

export default Root
