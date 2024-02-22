import React from "react";
import { QueryClient, QueryClientProvider, useQuery } from "react-query";

// Create a client
const queryClient = new QueryClient();

function FetchHelloWorld() {
  const { isLoading, error, data } = useQuery("fetchHello", () =>
    fetch("http://localhost:8000/api/hello/").then((res) => res.json())
  );

  if (isLoading) return "Loading...";

  if (error) return "An error has occurred: " + error.message;

  return <div>{data.message}</div>;
}

function App() {
  return (
    <QueryClientProvider client={queryClient}>
      <div className="App">
        <header className="App-header">
          <FetchHelloWorld />
        </header>
      </div>
    </QueryClientProvider>
  );
}

export default App;
