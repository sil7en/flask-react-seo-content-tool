import React, {useState, useEffect} from 'react';

function App() {

  const [data, setData] = useState([]);

  useEffect(() => {
    const api = async () => {
      const getData = await fetch('/keywords', {method: "GET"});
      const jsonData = await getData.json();
      setData(jsonData.keywords);
    }

    api();
  }, []);


  return (
    <div>
      {(typeof data === 'undefined') ? (
        <p>Loading...</p>
      ) : (
        <div>
          {data.map((e) => {
            return(
              <p>{e}</p>
            )
          })}
        </div>
      )}
    </div>
  );
}

export default App;
