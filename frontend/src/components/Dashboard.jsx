import React, { useEffect, useState } from 'react';
import API_BASE_URL from '../config';

const Dashboard = () => {
  const [data, setData] = useState(null);

  useEffect(() => {
    fetch(`${API_BASE_URL}/api/data-endpoint`)
      .then((response) => response.json())
      .then((data) => setData(data))
      .catch((error) => console.error('Error fetching data:', error));
  }, []);

  return (
    <div>
      <h1>Dashboard</h1>
      {data ? <p>Data: {JSON.stringify(data)}</p> : <p>Loading...</p>}
    </div>
  );
};

export default Dashboard;
