import { ShoppingCart, User } from "lucide-react"

import { Link } from "react-router-dom"
import Logo from "./Logo"

const Header = () => {
  return (
    <div className="w-full max-w-6xl fixed flex flex-row py-2 px-6 justify-between center">
      <Logo />
      <div className="flex flex-row center space-x-4">
        <Link to={"/"} className="p-2 rounded-lg hover:bg-red-900">
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
