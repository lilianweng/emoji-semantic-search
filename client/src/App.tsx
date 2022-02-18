import { useState } from "react";
import Result from "./Result";

let SERVER: string = process.env.REACT_APP_SERVER_ADDRESS || "";

type SearchResult = {
  emoji: string;
  message: string;
  score: number;
};

async function fetchSearchResults(query: string): Promise<Array<SearchResult>> {
  const response = await fetch(SERVER + "/search", {
    method: "POST",
    headers: {
      "content-type": "application/json;charset=UTF-8",
    },
    body: JSON.stringify({ query }),
  });
  const responseJson = await response.json();
  if (responseJson.error !== null) {
    console.log("Fetch error:", responseJson.error);
    return [];
  } else {
    return responseJson.result;
  }
}

function App() {
  const [query, setQuery] = useState<string>("");
  const [data, setData] = useState<Array<SearchResult>>([]);
  const [running, setRunning] = useState<boolean>(false);

  const runSearch: React.FormEventHandler<HTMLFormElement> = (e) => {
    e.preventDefault();
    if (query.length > 0) {
      setData([]);
      setRunning(true);
      fetchSearchResults(query).then((data) => {
        setData(data);
      });
    }
  };

  return (
    <>
      <h1>Emoji Search</h1>
      <form onSubmit={runSearch}>
        <input
          type="text"
          placeholder="Find the most relevant emojis"
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          autoFocus
        />
        <input type="submit" value="Search" />
      </form>
      <div className="result">
        <Result running={running} data={data} />
      </div>
      <div className="footer">
        Powered by{" "}
        <a href="https://openai.com/api/" target="_blank" rel="noreferrer">
          OpenAI
        </a>{" "}
        © 2022{" "}
        <a
          href="https://lilianweng.github.io/lil-log/"
          target="_blank"
          rel="noreferrer"
        >
          Lilian Weng
        </a>
        . All rights reserved.
      </div>
    </>
  );
}

export default App;
