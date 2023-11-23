import { configureStore } from "@reduxjs/toolkit";
import pageStatusReducer from './pageStatusSlice';

export const store = configureStore({
  reducer: {
    pageStatus: pageStatusReducer
  }
})

export type RootState = ReturnType<typeof store.getState>
export type AppDispatch = typeof store.dispatch