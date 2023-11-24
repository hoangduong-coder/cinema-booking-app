import { RouterProvider, createBrowserRouter } from "react-router-dom"

import ErrorPage from "./pages/ErrorPage"
import Root from "./pages/Root"

function App() {
  const router = createBrowserRouter([
    {
      path: "/",
      element: <Root />,
      errorElement: <ErrorPage />,
    },
  ])

  return <RouterProvider router={router} />
}

export default App
