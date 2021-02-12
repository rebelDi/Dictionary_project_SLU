import "./App.css";
import axios from "axios";
import { useEffect, useState } from "react";
import { Container } from "@material-ui/core";
import Header from "./components/Header/Header";
import Inputs from "./components/Inputs/Inputs";
import Definitions from "./components/Definitions/Definitions";

function App() {
  const [meanings, setMeanings] = useState([]);
  const [word, setWord] = useState("");
  const [language, setLanguage] = useState("en_US");
  const [poSpeech, setpoSpeech] = useState("noun");
  const demoApi = async () => {
    try {
      const respone = await axios.get(
        `https://api.dictionaryapi.dev/api/v2/entries/${language}/${word}`
      );

      setMeanings(respone.data);
    } catch (error) {
      console.log(error);
    }
  };

  useEffect(() => {
    demoApi();
  }, [language, word]);

  return (
    <div
      className="App"
      style={{
        height: "100vh",
        backgroundColor: "white",
        color: "whitesmoke",
      }}
    >
      <Container
        maxWidth="lg"
        style={{ display: "flex", flexDirection: "column", height: "100vh" }}
      >
        <Header />
        <center>
          <Inputs
            language={language}
            setLanguage={setLanguage}
            poSpeech={poSpeech}
            setpoSpeech={setpoSpeech}
            word={word}
            setWord={setWord}
          />
        </center>
        <Definitions
          language={language}
          poSpeech={setpoSpeech}
          word={word}
          meanings={meanings}
        />
      </Container>
    </div>
  );
}

export default App;
