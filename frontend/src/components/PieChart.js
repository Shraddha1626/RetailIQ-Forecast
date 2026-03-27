import React from 'react';
import { Pie } from 'react-chartjs-2';
import { Chart as ChartJS, ArcElement, Tooltip, Legend } from 'chart.js';

ChartJS.register(ArcElement, Tooltip, Legend);

export default function PieChart({ data }) {
  const options = { responsive: true, maintainAspectRatio: false, plugins: { legend: { position: 'bottom' } } };
  return (
    <div style={{ width: '300px', height: '300px', margin: 'auto' }}>
      <Pie data={data} options={options} />
    </div>
  );
}