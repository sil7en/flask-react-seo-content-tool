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
      <p className='font-bold text-3xl'>
        Hola soy un párrafo estilizado con Tailwind
      </p>
      {(typeof data === 'undefined') ? (
        <p>Loading...</p>
      ) : (
        <div>
          {data.map((e) => {
            return(
              <span>{e}</span>
            )
          })}
        </div>
      )}
    </div>
  );
}

export default App;
