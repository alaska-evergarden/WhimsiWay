import React from "react";
import Navbar from "./Navbar";
import Heatmap from "./Heatmap";
import { Link } from "react-router-dom";

const Home = () => {
  return (
    <>
      <Navbar />
      <div className="h-lvh lora-font">
        <img className="bg-img" src="road.png" alt="" />
        <div className="flex flex-col px-16 py-10">
          <span className="mb-8" style={{ fontSize: "3.5em" }}>
            Steering Clear <br /> of Trouble
          </span>
          <span className="mb-8" style={{ fontSize: "1.5em" }}>
            Plan and navigate your routes with ease.
          </span>
          <button className="nav-button">
            <p style={{ fontSize: "1em", fontWeight: "bold" }}>
              <Link to="/routefinder">FIND YOUR NEXT JOURNEY</Link>
            </p>
          </button>
        </div>
      </div>
      <Heatmap />
    </>
  );
};

export default Home;
