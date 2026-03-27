import React, { useEffect, useState } from 'react';
import PieChart from './PieChart';

export default function Dashboard() {
  const [forecastData, setForecastData] = useState([]);

  useEffect(() => {
    fetch('http://127.0.0.1:5000/forecast/all')
      .then(res => res.json())
      .then(data => setForecastData(data));
  }, []);

  const chartData = {
    labels: forecastData.map(f => f.product_name),
    datasets: [
      {
        label: 'Sales Quantity',
        data: forecastData.map(f => f.sales_quantity),
        backgroundColor: ['#FF6384', '#36A2EB', '#FFCE56', '#4BC0C0', '#9966FF'],
        borderWidth: 1,
      },
    ],
  };

  return (
    <div style={{ padding: '20px' }}>
      <h3>Sales Forecast Dashboard</h3>
      <PieChart data={chartData} />
    </div>
  );
}
