import { Clapperboard, HomeIcon, Settings, User } from "lucide-react"

import { ElementType } from "react"
import { Link } from "react-router-dom"
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
    <Link to={url}>
      <Icon className="w-6 h-6" />
      <div className="text-sm">{title}</div>
    </Link>
  )
}

const Sidebar = () => {
  return (
    <aside className="sm:hidden">
      <div>
        <Logo />
        <h1>John Doe</h1>
        <SidebarItem Icon={HomeIcon} title="Home" url="/" />
        <SidebarItem
          Icon={Clapperboard}
          title="Manage movie"
          url="manage-movie"
        />
        <SidebarItem Icon={User} title="Profile" url="profile" />
        <SidebarItem Icon={Settings} title="Setting" url="setting" />
      </div>
      <div>
        <Link to="log-in">Sign in</Link>
      </div>
    </aside>
  )
}

export default Sidebar
