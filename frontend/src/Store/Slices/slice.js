import { createSlice } from "@reduxjs/toolkit";

const initState = {
  isError: "",
  productsArr: [],
  isLoading: true,
};

const productSlice = createSlice({
  name: "products",
  initialState: initState,
  reducers: {
    fetchData(state) {
      //   state.isLoading = true;
    },
  },
});

export const { fetchData } = productSlice.actions;

export default productSlice.reducer;
