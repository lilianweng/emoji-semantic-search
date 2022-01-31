import React, { useState, useEffect, useRef } from 'react';

type SearchResult = {
  emoji: string,
  message: string,
  score: number,
};

async function fetch_search_results(query: string): Promise<Array<SearchResult>> {
  const response = await fetch("http://localhost:12358/search", {
      method: 'POST',
      headers: {
        'content-type': 'application/json;charset=UTF-8',
      },
      body: JSON.stringify({
        query: query,
      }),
  });
  const response_json = await response.json();
  if (response_json.error !== null) {
    return [];
  } else {
    return response_json.result;
  }
}

function App() {
  const [query, setQuery] = useState<string>("");
  const [data, setData] = useState<Array<SearchResult>>([]);
  const queryInputRef = useRef<HTMLInputElement | null>(null);

  useEffect(() => {
    if (query.length > 0) {
      console.log("query:", query);
      fetch_search_results(query)
      .then( data => {
          setData(data);
          console.log(data);
      });
    }
  }, [query]);

  const runSearch = () => {
    if (queryInputRef && queryInputRef.current) {
      setQuery(queryInputRef.current.value);
      console.log(query);
    }
  }

  return (
    <>
      <input ref={queryInputRef} type="text"
        onKeyPress={(e) => e.key === 'Enter' && runSearch()} />
      <button onClick={runSearch}>Search</button>
      {data && data.map(row => {
        return <div>{row}</div>
      })}
    </>
  );
}

export default App;