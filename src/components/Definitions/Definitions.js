import React from "react";
import "./Definitions.css";

const Definitions = ({ meanings, word, language, partOfSpeech }) => {
  console.log(word, language, partOfSpeech);
  console.log('meaningssss',meanings);

  return (
    <div className="meanings">
      {meanings.map((m) => {
        return [m].map((e) => {
          console.log(e);
          return e.meanings.meaning.map((def) => {
            console.log(def);
            return def.examples.map((d) => {
              return (
                <div className="definition" key={d.id}>
                  <b>
                    {" "}
                    <span className="arrow">arrow</span>
                    {d.example}
                  </b>
                  <br />
                </div>
              );
            });
          });
        });
      })}
    </div>
  );
};
export default Definitions;
