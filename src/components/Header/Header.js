import React, { Component } from "react";
import "./Header.css";
import { MenuItem, TextField } from "@material-ui/core";
import languages from "../../data/languages";

export default class Header extends Component {
  render() {
    return (
      <div>
        <div className="language">
          <TextField select value={"English"} size="small" variant="outlined">
            {languages.map((item) => (
              <MenuItem key={item.label} value={item.label}>
                {item.value}
              </MenuItem>
            ))}
          </TextField>
        </div>
        <div className="header">
          {<span className="title">Dictionary</span>}
        </div>
      </div>
    );
  }
}
