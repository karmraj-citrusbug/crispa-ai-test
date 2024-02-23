import React, { useEffect } from "react";
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend,
} from "chart.js";
import { Line } from "react-chartjs-2";

ChartJS.register(
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend
);

export const options = {
  responsive: true,
  plugins: {
    title: {
      display: true,
      text: "Chart.js Line Chart",
    },
    datalabels: {
      anchor: "center",
      color: "rgba(98, 98, 98, 1)",
      font: {
        size: 18,
        weight: 700,
      },
      formatter: (value) => {
        if (value > 0) {
          return "Positive";
        } else if (value < 0) {
          return "Negative";
        } else {
          return "";
        }
      },
    },
    legend: {
      display: false,
    },
    tooltip: {
      enabled: false,
    },
  },
  scales: {
    yAxes: [
      {
        ticks: {
          beginAtZero: true,
        },
        gridLines: {
          display: false,
          drawBorder: false,
        },
      },
    ],
    x: {
      beginwithZero: true,
      grid: {
        display: false,
      },
    },
    y: {
      min: 0,
      max: 600,
    },
  },
};

const labels = [
  "J",
  "F",
  "M",
  "A",
  "M",
  "J",
  "J",
  "A",
  "S",
  "O",
  "N",
  "D",
  "J",
  "F",
  "M",
  "A",
  "M",
  "J",
  "J",
  "A",
  "S",
  "O",
  "N",
  "D",
  "J",
  "F",
  "M",
  "A",
  "M",
  "J",
  "J",
  "A",
  "S",
  "O",
  "N",
  "D",
];

export default function LineChart({ chartDataSet, selectedYear }) {
  const metaData = chartDataSet["Meta Data"];

  const monthlyTimeSeries = Object.entries(
    chartDataSet["Monthly Time Series"]
  ).map(([date, values]) => ({
    date,
    open: values["1. open"],
    high: values["2. high"],
    low: values["3. low"],
    close: values["4. close"],
    volume: values["5. volume"],
  }));

  // Creating the new object with transformed data
  const transformedData = {
    "Meta Data": metaData,
    "Monthly Time Series": monthlyTimeSeries,
  };

  const filter3YearData = transformedData["Monthly Time Series"].filter(
    (currFinalChartData) => {
      if (
        currFinalChartData.date.split("-")[0] >= selectedYear.$y - 2 &&
        currFinalChartData.date.split("-")[0] <= selectedYear.$y
      ) {
        return currFinalChartData;
      }
    }
  );

  const chartFinalData = filter3YearData.map((currObj) => {
    return currObj.open;
  });

  console.log(filter3YearData);

  // console.log(chartFinalData);

  const data = {
    labels,
    datasets: [
      {
        label: "Dataset 1",
        data: chartFinalData,
        borderColor: "rgb(255, 99, 132)",
        backgroundColor: "rgba(255, 99, 132, 0.5)",
      },
    ],
  };

  return (
    <div className="lineChartContainer">
      <Line options={options} data={data} height={50} />
      <div
        className="yearTabs flex
      "
      >
        <p className="currentYear">{selectedYear.$y}</p>
        <p className="prevYear">{selectedYear.$y - 1}</p>
        <p className="nextPrevYear">{selectedYear.$y - 2}</p>
      </div>
    </div>
  );
}
