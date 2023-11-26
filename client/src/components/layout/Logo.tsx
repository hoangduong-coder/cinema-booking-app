import { Film } from "lucide-react"
import { Link } from "react-router-dom"

const Logo = () => {
  return (
    <div className="flex flex-row items-center space-x-2 text-xl font-extrabold">
      <Film className="w-8 h-8" />
      <Link to={"/"}>
        <h1 className="text-red">
          HelloWorld<span className="text-white">Cinema</span>
        </h1>
      </Link>
    </div>
  )
}

export default Logo
