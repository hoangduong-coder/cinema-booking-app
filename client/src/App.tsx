import { RouterProvider, createBrowserRouter } from "react-router-dom"

import Error from "./pages/Error"
import Root from "./pages/Root"

function App() {
  const router = createBrowserRouter([
    {
      path: "/",
      element: <Root />,
      errorElement: <Error />,
    },
  ])

  return <RouterProvider router={router} />
}

export default App
