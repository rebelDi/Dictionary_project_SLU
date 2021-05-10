import "./App.css";
import { useEffect, useState } from "react";
import { Container } from "@material-ui/core";
import Header from "./components/Header/Header";
import Inputs from "./components/Inputs/Inputs";
import Definitions from "./components/Definitions/Definitions";
import { useTranslation } from "react-i18next";
function App() {
  const [meanings, setMeanings] = useState([]);
  const [word, setWord] = useState("");
  const [language, setLanguage] = useState("English");
  const [partOfSpeech, setPartOfSpeech] = useState("Noun");
  const [numberOfCluster, setNumberOfCluster] = useState("2");
  const [locale, setLocale] = useState("en");
  const [t, i18n] = useTranslation();
  useEffect(() => {
    setMeanings([]);
    setNumberOfCluster("2");
    i18n.changeLanguage(locale);
  }, [word, locale]);

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
        <Header t={t} setLocale={setLocale} locale={locale} />
        <center>
          <Inputs
            t={t}
            language={language}
            setLanguage={setLanguage}
            partOfSpeech={partOfSpeech}
            setPartOfSpeech={setPartOfSpeech}
            word={word}
            setWord={setWord}
            meanings={meanings}
            setMeanings={setMeanings}
            setNumberOfCluster={setNumberOfCluster}
            numberOfCluster={numberOfCluster}
          />
        </center>
        <Definitions t={t} word={word} meanings={meanings} />
      </Container>
    </div>
  );
}

export default App;
