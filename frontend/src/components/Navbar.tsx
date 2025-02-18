import { Link } from "react-router-dom";

const Navbar = () => {
  return (
    <>
      <div
        className="flex w-lvw justify-center items-center"
        style={{ backgroundColor: "#F4EEE5" }}
      >
        <img src="/favicon.svg" alt="" />
        <div
          className="flex flex-col mx-5 justify-center items-center top-nav lora-font"
          style={{ height: "105px", zIndex: 100 }}
        >
          <span
            style={{ fontSize: 32, fontWeight: "bold", letterSpacing: "0.1em" }}
          >
            WhimsiWay
          </span>
          <span style={{ fontSize: 12, letterSpacing: "0.2em" }}>
            Your Roadside Companion
          </span>
        </div>
      </div>
      <ul className="flex justify-around items-center navbar lora-font">
        <li>
          <Link to="/">Home</Link>
        </li>
        <li>
          <Link to="/hotspots">Accident Hotspots</Link>
        </li>
        <li>
          <Link to="/routefinder">Route Finder</Link>
        </li>
        <li>
          <Link to="/about">About</Link>
        </li>
      </ul>
    </>
  );
};

export default Navbar;
