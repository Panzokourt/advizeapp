import React from "react";
import ReactDOM from "react-dom/client";
import App from "./App.jsx"; // Επέκταση με .jsx
import "./styles/index.css"; // Σύνδεση με Tailwind CSS

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
