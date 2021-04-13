import "./App.css";
import { useEffect, useState } from "react";
import { Container } from "@material-ui/core";
import Header from "./components/Header/Header";
import Inputs from "./components/Inputs/Inputs";
import Definitions from "./components/Definitions/Definitions";

function App() {
  const [meanings, setMeanings] = useState([]);
  const [word, setWord] = useState("");
  const [language, setLanguage] = useState("English");
  const [partOfSpeech, setPartOfSpeech] = useState("Noun");

  useEffect(() => {}, []);

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
            partOfSpeech={partOfSpeech}
            setPartOfSpeech={setPartOfSpeech}
            word={word}
            setWord={setWord}
            setMeanings={setMeanings}
            meanings={meanings}
          />
        </center>
        <Definitions
          language={language}
          partOfSpeech={partOfSpeech}
          word={word}
          meanings={meanings}
        />
      </Container>
    </div>
  );
}

export default App;
