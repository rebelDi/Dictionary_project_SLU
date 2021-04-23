import React from "react";
import "./Definitions.css";
import { Divider } from "@material-ui/core";

const Definitions = ({ meanings, word, language, partOfSpeech }) => {
  console.log(word, language, partOfSpeech);
  console.log("meaningssss", meanings);

  return (
    <div className="meanings">
      {meanings.map !== undefined ? (
        meanings.map((m) => {
          return [m].map((e) => {
            console.log(e);
            return e.meanings.meaning.map((def) => {
              console.log(def);
              return def.examples.map((d) => {
                return (
                  <div className="definition" key={d.id}>
                    <b>
                      {d.id === 1 ? (
                        <div>
                          <h3>Meaning {def.id}:</h3>
                          <Divider />
                        </div>
                      ) : null}
                      <span className="arrow">arrow</span>
                      {d.example}
                    </b>
                  </div>
                );
              });
            });
          });
        })
      ) : (
        <div>
          <span className="arrow">arrow</span>
          {"There is no result for "}
          {word}
        </div>
      )}
    </div>
  );
};
export default Definitions;
