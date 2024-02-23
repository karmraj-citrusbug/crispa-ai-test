import React from "react";
import Index from "./Pages/Index";
// import { QueryClient, QueryClientProvider } from "@tanstack/react-query";

import "./App.css";

// const client = new QueryClient();

const App = () => {
  return (
    <div style={{ height: "100vh" }}>
      {/* <QueryClientProvider client={client}> */}
      <Index />
      {/* </QueryClientProvider> */}
    </div>
  );
};

export default App;
