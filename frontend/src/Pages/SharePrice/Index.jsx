import React, { useEffect, useState } from "react";
import MyTable from "../../Components/MyTable";
import LineChart from "../../Components/LineChart";

const months = {
  1: "Jan",
  2: "Feb",
  3: "Mar",
  4: "Apr",
  5: "May",
  6: "Jun",
  7: "Jul",
  8: "Aug",
  9: "Sep",
  10: "Oct",
  11: "Nov",
  12: "Dec",
};

const getMonth = (monthNumber) => {
  return months[monthNumber];
};

const currDateData = (tmpData, date) => {
  let { close, open, volume, low, high } = tmpData["Time Series (Daily)"][date];
  return [open, high, low, close, volume];
};

const tableCols = [
  "DATE",
  "OPEN",
  "HIGH",
  "LOW",
  "CLOSE",
  "VOLUME",
  "MOVEMENT",
];

const Index = ({ selectedYear }) => {
  const [tableData, setTableData] = useState([]);
  const [chartData, setChartData] = useState(null);
  const getTableData = async () => {
    const res = await fetch(
      "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&outputsize=full&apikey=demo"
    );
    const data = await res.json();
    setTableData(data);
  };

  const getChartData = async () => {
    const res = await fetch(
      "https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY&symbol=IBM&apikey=demo"
    );
    const data = await res.json();
    setChartData(data);
  };

  useEffect(() => {
    getTableData();
  }, []);

  useEffect(() => {
    getChartData();
  }, []);

  const dataTableData = tableData["Time Series (Daily)"];

  const finalData = [];

  for (const key in dataTableData) {
    let dataDict = {};
    dataDict["date"] = formateDate(key);

    dataDict["open"] = dataTableData[key]["1. open"];
    dataDict["high"] = dataTableData[key]["2. high"];
    dataDict["low"] = dataTableData[key]["3. low"];
    dataDict["close"] = dataTableData[key]["4. close"];
    dataDict["volume"] = dataTableData[key]["5. volume"];
    finalData.push(dataDict);
    break;
  }

  function formateDate(date) {
    const [year, month, day] = date.split("-");
    return `${day} ${getMonth(parseInt(month))} ${year}`;
  }

  return (
    <>
      {chartData && (
        <LineChart selectedYear={selectedYear} chartDataSet={chartData} />
      )}
      <MyTable data={finalData} tableColumns={tableCols} />
    </>
  );
};

export default Index;
