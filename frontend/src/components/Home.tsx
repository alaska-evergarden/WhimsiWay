import Navbar from "./Navbar";
import Heatmap from "./Heatmap";
import { Link } from "react-router-dom";

const Home = () => {
  return (
    <>
      <div className="h-lvh lora-font">
        <Navbar />
        <img className="bg-img" src="road.png" alt="" />
        <div className="flex justify-around items-center mt-16">
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
          <img className="rounded-lg" src="/trip.jpeg" alt="" />
        </div>
      </div>
      <div>
        <Heatmap />
      </div>
    </>
  );
};

export default Home;
