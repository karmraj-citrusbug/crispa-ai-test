import React, { useEffect, useState } from "react";
import MyTable from "../../Components/MyTable";

const apiRes = [
  {
    uid: "5e2d984f-4960-46d9-8a86-2074233dcd57",
    description: "test description",
    accounting_date: "2024-02-23",
    account: {
      number: "0000",
      name: "test 0000",
      default_accounting_type: "debit",
    },
    currency: {
      code: "EUR",
    },
    amount: 550,
    state: "debit",
    accounting_type: "draft",
    reconciled: true,
  },
];

const Index = () => {
  const [tableData, setTableData] = useState([]);
  const getData = async () => {
    const res = await fetch("http://localhost:8000/api/journal-entry-lines/");
    const data = await res.json();
    console.log(data);
    setTableData(data);
  };

  useEffect(() => {
    // getData();
  }, []);

  const tableRows = [
    {
      id: apiRes[0].uid.substr(apiRes[0].uid.length - 6),
      description: apiRes[0].description,
      date: apiRes[0].accounting_date,
      account: apiRes[0].account.number,
      type: apiRes[0].account.default_accounting_type,
      input_currency: "EUR",
      input_net: apiRes[0].amount,
      fix_rate: 7.45,
      converted_currency: "DKK",
      converted_net: apiRes[0].amount * 7.45,
      type: apiRes[0].accounting_type,
      status: apiRes[0].state,
      reconciled: apiRes[0].reconciled,
    },
  ];

  const tableCols = [
    "ID",
    "DESCRIPTION",
    "DATE",
    "ACCOUNT",
    "TYPE",
    "INPUT_CURRENCY",
    "INPUT_NET",
    "FIX_RATE",
    "CONVERTED_CURRENCY",
    "CONVERTED_NET",
    "TYPE",
    "STATUS",
    "RECONCILED",
  ];


  return (
    <>
      <MyTable data={tableRows} tableColumns={tableCols} />
    </>
  );
};

export default Index;
