import React from "react";
import "./Header.css";
import { MenuItem, TextField } from "@material-ui/core";
import uniqid from "uniqid";

const Header = ({
  t,
  setLocale,
  locale,
  locales = ["en", "hi", "ru", "tr", "ua"],
}) => {
  {
    return (
      <nav>
        <div className="language">
          <TextField
            id="outlined-basic"
            select
            value={locale}
            onChange={(e) => setLocale(e.target.value)}
          >
            {locales.map((item) => (
              <MenuItem key={uniqid()} value={item}>
                {item}
              </MenuItem>
            ))}
          </TextField>
        </div>
        <div className="header">
          {<span className="title">{t("Dictionary")}</span>}
        </div>
      </nav>
    );
  }
};
export default Header;
