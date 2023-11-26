import { createSlice } from "@reduxjs/toolkit"

export interface PageStatusState {
  showSidebar: boolean
}

const initialState: PageStatusState = {
  showSidebar: false
}

export const pageStatusSlice = createSlice({
  name: 'pageStatus',
  initialState,
  reducers: {
    toggleSidebar: (state) => {
      state.showSidebar = !state.showSidebar
    }
  }
})

export const { toggleSidebar } = pageStatusSlice.actions
export default pageStatusSlice.reducer