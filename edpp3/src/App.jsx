import { useState } from "react";
import Home from "./components/home";
import { BrowserRouter as Router, Route, Routes, Link } from "react-router-dom";
import "./App.css";

function App() {
  return (
    <>
      <Router>
        <Routes>
          <Route path="/" element={<Home />} />
        </Routes>
      </Router>
    </>
  );
}

export default App;
