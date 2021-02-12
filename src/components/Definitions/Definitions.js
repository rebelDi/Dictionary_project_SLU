import React from "react";
import "./Definitions.css";

const Definitions = (meanings, word, language, poSpeech,setpoSpeech) => {
  console.log(meanings.meanings,word,language);

  return (
    <div className="meanings">
      {meanings.meanings.map((item) =>
        item.meanings.map((i) => {
          if (i.partOfSpeech === 'noun')
          return i.definitions.map((def) => (
            <div className="definition">
              <b> <span className="arrow">arrow</span>{def.definition}</b>
              <br/>
              {def.example && <span className="name"> {def.example} </span>}
            </div>
          ));;
        })
      )}
    </div>

  );
};
export default Definitions;
