import React from "react";
import { TextField, MenuItem, ThemeProvider, Button } from "@material-ui/core";
import "./Inputs.css";
import languages from "../../data/languages";
import poSpeech from "../../data/poSpeech";

const Inputs = ({ language, setLanguage, poSp, setpoSpeech, word, setWord}) => {
  return (
    <div classname="inputs">
      <br />
      <TextField
        className="search_field"
        id="filled-basic"
        value={word}
        label="Search a Word"
        onChange={(e) => setWord(e.target.value)}
      />
      <Button class="find_button" />

      <br />
      <br />
      <TextField
        select
        label="Part of Speech"
        value={poSp}
        onChange={(e) => setpoSpeech(e.target.value)}
        className="part_of_speech_field"
      >
        {poSpeech.map((item) => (
          <MenuItem key={item.label} value={item.label}>
            {item.value}
          </MenuItem>
        ))}
      </TextField>
         
      <TextField
        select
        label="Language"
        value={language}
        onChange={(e) => setLanguage(e.target.value)}
        className="language_select"
      >
        {languages.map((item) => (
          <MenuItem key={item.label} value={item.label}>
            {item.value}
          </MenuItem>
        ))}
      </TextField>

      
    </div>
  );
};
export default Inputs;
