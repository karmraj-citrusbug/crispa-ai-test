import { configureStore } from "@reduxjs/toolkit";
import productSlice from "./Slices/slice";

const store = configureStore({
  reducer: {
    products: productSlice,
  },
  middleware: (getDefaultMiddle) => {
    return [...getDefaultMiddle()];
  },
});

export default store;
