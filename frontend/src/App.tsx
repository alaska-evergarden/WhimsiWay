import "../src/App.css";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import Home from "./components/Home";
import Hotspots from "./components/Hotspots";
import About from "./components/About";
import RouteFinder from "./components/RouteFinder";

const App = () => {
  return (
    <Router>
      <Routes>
        <Route index element={<Home />} />
        <Route path="/" element={<Home />} />
        <Route path="/hotspots" element={<Hotspots />} />
        <Route path="/routefinder" element={<RouteFinder />} />
        <Route path="/about" element={<About />} />
      </Routes>
    </Router>
  );
};

export default App;
