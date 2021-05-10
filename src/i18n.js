import i18n from "i18next";
import Backend from "i18next-xhr-backend";
import { initReactI18next } from "react-i18next";

const languages = ["en", "hi", "ru", "tr", "ua"];

i18n
  .use(Backend) // load translation using xhr -> see /public/locales. We will add locales in the next step

  .use(initReactI18next) // pass the i18n instance to react-i18next.

  .init({
    fallbackLng: "en", //default lang
    debug: true,
    whitelist: languages,

    interpolation: {
      escapeValue: false,
    },
    react: {
      wait: true,
    },
  });

export default i18n;
