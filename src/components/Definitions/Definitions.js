import React from "react";
import "./Definitions.css";

const Definitions = ({ meanings, word, language, partOfSpeech }) => {
  console.log(meanings, word, language, partOfSpeech);

  return (
    <div className="meanings">
      {
        /* {meanings.meanings.map((item) =>
        item.meanings.map((i) => {
          if (i.partOfSpeech === meanings.partOfSpeech)
            return i.definitions.map((def) => (
              <div className="definition">
                <b>
                  {" "}
                  <span className="arrow">arrow</span>
                  {def.definition}
                </b>
                <br />
                {def.example && <span className="name"> {def.example} </span>}
              </div>
            ));
        })
      )} */

        <div className="definition">
          <b>
            {" "}
            <span className="arrow">arrow</span>
            {meanings}
          </b>
          <br />
        </div>
      }
    </div>
  );
};
export default Definitions;
