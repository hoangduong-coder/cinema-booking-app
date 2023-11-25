import { RouterProvider, createBrowserRouter } from "react-router-dom"

import AllMovies from "./pages/AllMovies"
import ErrorPage from "./pages/ErrorPage"
import Root from "./pages/Root"

function App() {
  const router = createBrowserRouter([
    {
      path: "/",
      element: <Root />,
      errorElement: <ErrorPage />,
      children: [
        {
          path: "/movies",
          element: <AllMovies />,
        },
      ],
    },
  ])

  return <RouterProvider router={router} />
}

export default App
