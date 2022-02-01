import React, { useState, useEffect, useRef } from 'react';

let SERVER: string = process.env.REACT_APP_SERVER_ADDRESS || "";

type SearchResult = {
  emoji: string,
  message: string,
  score: number,
};

async function fetch_search_results(query: string): Promise<Array<SearchResult>> {
  const response = await fetch(SERVER + "/search", {
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
      fetch_search_results(query)
      .then( data => {
          setData(data);
      });
    }
  }, [query]);

  const runSearch = () => {
    if (queryInputRef && queryInputRef.current) {
      setQuery(queryInputRef.current.value);
    }
  }

  const displaySearchResult = (data: Array<SearchResult>) => {
    return (
      <div className="center">
        <table>
          <tbody>
          {data.map((row, i) => {
            return (
              <tr key={i}>
                <td className='emoji'><button onClick={() => {navigator.clipboard.writeText(row.emoji)}} title="Click to copy">{row.emoji}</button></td>
                <td className='message'>{row.message}</td>
                <td className='score'>{row.score.toFixed(2)}</td>
              </tr>
            )
          })}
          </tbody>
        </table>
       </div>
    );
  }

  return (
    <>
      <h1>Emoji Search</h1>
      <input ref={queryInputRef} type="text"
        onKeyPress={(e) => e.key === 'Enter' && runSearch()}
        placeholder="Find the most relevant emojis." />
      &nbsp;
      <button onClick={runSearch}>Search</button>
      {data.length > 0 && displaySearchResult(data)}
    </>
  );
}

export default App;