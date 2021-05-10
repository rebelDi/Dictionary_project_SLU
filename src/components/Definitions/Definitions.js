import React from "react";
import "./Definitions.css";
import ListView from "../ListView/ListView";
import { List, ListSubheader } from "@material-ui/core";
import uniqid from "uniqid";

const Definitions = ({ t, meanings, word }) => {
  return (
    <div className="meanings">
      <List
        component="nav"
        aria-labelledby="nested-list-subheader"
        subheader={
          <ListSubheader component="div" id="nested-list-subheader">
            {t("Meaning List")}
          </ListSubheader>
        }
      >
        {meanings.map !== undefined ? (
          meanings.map((m) => {
            return [m].map((e) => {
              console.log(e);
              return e.meanings.meaning.map((def) => {
                console.log(def);

                return (
                  <div className="definition">
                    {<ListView key={uniqid()} meaning={def} t={t} />}
                  </div>
                );
              });
            });
          })
        ) : (
          <div>
            <span className="arrow">arrow</span>
            {t("There is No Result")}
            {" "}
            {word}
          </div>
        )}
      </List>
    </div>
  );
};
export default Definitions;
