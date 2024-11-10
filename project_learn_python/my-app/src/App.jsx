import React, { useEffect, useState } from 'react';

function App() {
    const [data, setData] = useState(null);

    useEffect(() => {
        fetch('http://127.0.0.1:5000/api/data')
            .then(response => response.json())
            .then(data => setData(data))
            .catch(error => console.error('Error:', error));
    }, []);

    return (
        <div>
            <h1>Data from Python Backend</h1>
            {data ? <p>{data.message}</p> : <p>Loading...</p>}
        </div>
    );
}

console.log(App)

export default App;
