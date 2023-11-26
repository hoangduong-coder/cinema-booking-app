/* eslint-disable @typescript-eslint/ban-ts-comment */

import { isRouteErrorResponse, useRouteError } from "react-router-dom"

const ErrorPage = () => {
  const error = useRouteError()
  const errorMessage = (): string => {
    if (isRouteErrorResponse(error)) {
      return error.statusText || error.data.message
    } else if (error instanceof Error) {
      //@ts-ignore
      return error.message
    } else if (typeof error === "string") {
      return error
    } else {
      return "Unknown error"
    }
  }
  return (
    <div>
      <h1>Not found!</h1>
      <p>
        Sorry, an error has occurred. There is no result that you're looking
        for.
      </p>
      <p>
        <i>{errorMessage()}</i>
      </p>
    </div>
  )
}

export default ErrorPage
