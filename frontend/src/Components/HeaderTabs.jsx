import * as React from "react";
import PropTypes from "prop-types";
import Tabs from "@mui/material/Tabs";
import Tab from "@mui/material/Tab";
import Typography from '@mui/material/Typography';
import Box from "@mui/material/Box";
import Button from "@mui/material/Button";
import {TextField} from "@mui/material";
// import { DesktopDatePicker } from "@mui/x-date-pickers";
// import { AdapterDayjs } from "@mui/x-date-pickers";
// import { LocalizationProvider } from "@mui/x-date-pickers";
import dayjs from "dayjs";
import SharePriceIndex from "../Pages/SharePrice/Index";
import EntryListIndex from "../Pages/EntryList/Index";

function CustomTabPanel(props) {
  const { children, value, index, ...other } = props;

  return (
    <div
      role="tabpanel"
      hidden={value !== index}
      id={`simple-tabpanel-${index}`}
      aria-labelledby={`simple-tab-${index}`}
      {...other}
    >
      {value === index && (
        <Box sx={{ p: 3 }}>
          <Typography>{children}</Typography>
        </Box>
      )}
    </div>
  );
}

CustomTabPanel.propTypes = {
  children: PropTypes.node,
  index: PropTypes.number.isRequired,
  value: PropTypes.number.isRequired,
};

function a11yProps(index) {
  return {
    id: `simple-tab-${index}`,
    "aria-controls": `simple-tabpanel-${index}`,
  };
}

export default function HeaderTabs(props) {
  const [value, setValue] = React.useState(0);
  const [selectedYear, setSelectedYear] = React.useState(dayjs(new Date()));
  console.log(selectedYear);

  const handleDateChange = (newValue) => {
    setSelectedYear(newValue);
  };

  const handleChange = (event, newValue) => {
    setValue(newValue);
  };

  return (
    <div className="main-section-wrapper">
      <div className="tab-section">
        <Box className="main-box">
          <Box sx={{ width: "fit-content" }}>
            <Tabs
              value={value}
              onChange={handleChange}
              aria-label="basic tabs example"
              className="custom-tabs"
            >
              <Tab label="Share price" {...a11yProps(0)} />
              <Tab label="Dashboard" {...a11yProps(1)} />
              <Tab label="Entry list" {...a11yProps(2)} />
            </Tabs>
          </Box>
          <CustomTabPanel value={value} index={0} className="tab-panel-div">
            <div className="share-price-main-content-wrapper main-content-wrapper">
              <div className="top-section">
                <div className="top-left-sec">
                  <h2>Share Price</h2>
                  <p>USD</p>
                </div>
                <div className="top-right-sec">
                  <h2>Starting Month</h2>
                  <div className="custom-date-feild">
                    {/* <LocalizationProvider dateAdapter={AdapterDayjs}> */}
                    {/* <LocalizationProvider> */}

                      {/* <DesktopDatePicker
                        label="Select"
                        views={["year", "month"]}
                        inputFormat="MM/DD/YYYY"
                        value={selectedYear}
                        onChange={handleDateChange}
                        renderInput={(params) => <TextField {...params} />}
                      /> */}
                    {/* </LocalizationProvider> */}
                  </div>
                  <TextField
                    variant="outlined"
                    placeholder="Enter a stock symbol"
                  />
                  <Button variant="contained" className="theme-btn">
                    Update
                  </Button>
                </div>
              </div>
            </div>
            <div className="main-content-wrapper">
              <SharePriceIndex selectedYear={selectedYear} />
            </div>
          </CustomTabPanel>
          <CustomTabPanel value={value} index={1} className="tab-panel-div">
            <div className="db-main-content-wrapper main-content-wrapper">
              <div className="top-section">
                <div className="top-left-sec">
                  <h2>Dashboard</h2>
                </div>
              </div>
            </div>
          </CustomTabPanel>
          <CustomTabPanel value={value} index={2} className="tab-panel-div">
            <div className="entry-list-main-content-wrapper main-content-wrapper">
              <div className="top-section">
                <div className="top-left-sec">
                  <h2>Entry List</h2>
                </div>
              </div>
            </div>
            <div className="main-content-wrapper">
              <EntryListIndex />
            </div>
          </CustomTabPanel>
        </Box>
      </div>
    </div>
  );
}
