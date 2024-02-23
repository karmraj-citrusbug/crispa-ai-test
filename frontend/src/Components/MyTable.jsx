import { useEffect } from "react";
import { styled } from "@mui/material/styles";
import {Table} from "@mui/material";
import TableBody from "@mui/material/TableBody";
import { TableCell,tableCellClasses } from "@mui/material";
import {TableContainer} from "@mui/material";
import {TableHead} from "@mui/material";
import {TableRow} from "@mui/material";
import {Paper} from "@mui/material";
import { useState } from "react";

const StyledTableCell = styled(TableCell)(({ theme }) => ({
  [`&.${tableCellClasses.head}`]: {
    backgroundColor: "white",
    color: "#666666",
    fontWeight: "700",
  },
  [`&.${tableCellClasses.body}`]: {
    fontSize: 15,
    fontWeight: "400",
    lineHeight: "19px",
  },
}));

const StyledTableRow = styled(TableRow)(({ theme }) => ({
  "&:nth-of-type(even)": {
    backgroundColor: "#F0F2FE",
  },
  "td, th": {
    border: 0,
  },
}));

export default function MyTable({ data, tableColumns }) {
  return (
    <TableContainer
      component={Paper}
      sx={{ maxHeight: 580, boxShadow: "none" }}
    >
      <Table sx={{ minWidth: 700 }} aria-label="customized table">
        <TableHead
          sx={{ borderBottom: "2px solid #efefef" }}
          stickyHeader
          aria-label="sticky table"
        >
          <TableRow>
            {tableColumns.map((currTableCol, index) => {
              return (
                <StyledTableCell key={index}>{currTableCol}</StyledTableCell>
              );
            })}
          </TableRow>
        </TableHead>
        <TableBody>
          {data.map((row, index) => (
            <StyledTableRow key={row.date}>
              {tableColumns.map((currTableCol, index) => {
                return (
                  <StyledTableCell>
                    {row[currTableCol.toLowerCase()]}
                  </StyledTableCell>
                );
              })}
            </StyledTableRow>
          ))}
        </TableBody>
      </Table>
    </TableContainer>
  );
}
