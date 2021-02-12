import React, { Component } from "react";
import "./Header.css"
import Typography from "@material-ui/core/Typography"
import { Paper } from "@material-ui/core";

export default class Header extends Component {
  render() {
    return (
      <div className="header">
        {<span className="title">Dictionary</span>}
      </div>
    );
  }
}
