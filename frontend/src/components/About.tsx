import React from "react";
import Navbar from "./Navbar";

const About = () => {
  return (
    <>
      <Navbar />
      <div className="flex flex-col p-10 justify-center items-center lora-font">
        <span className="text-4xl mb-5 font-bold">
          Smarter Routes, Safer Commutes
        </span>
        <span>
          This initiative is our commitment to ethics and excellence in vehicle
          safety. Here's how we do it:
        </span>
      </div>
      <div
        className="flex justify-center items-center p-10"
        style={{ backgroundColor: "#F4EEE5" }}
      >
        <div className="flex flex-col lora-font w-4/12 p-10 rounded-lg bg-white mr-24">
          <span className="font-bold text-3xl mb-5">Our Mission</span>
          <span className="text-lg leading-relaxed">
            WhimsiWay is dedicated to promoting safer journeys by empowering
            individuals to make informed decisions about their routes. We are
            commited to innovation through providing users with insightful
            access to historical accident data and the ability to avoid
            accident-prone areas. We strive to create a platform that not only
            helps users navigate but also raises awareness about traffic safety.
          </span>
        </div>
        <img className="w-2/5 rounded-lg" src="roadtrip.jpeg" alt="" />
      </div>
      <div className="flex justify-around items-end p-10 px-32 lora-font">
        <div className="flex flex-col justify-center items-center">
          <img src="explore.png" alt="" className="mb-5" />
          <span>Explore Historical Accident Data</span>
        </div>
        <div className="flex flex-col justify-center items-center">
          <img src="/favicon.svg" alt="" className="mb-5" />
          <span>Identify Accident-Prone Areas</span>
        </div>
        <div className="flex flex-col justify-center items-center">
          <img src="/icons8-route.gif" alt="" className="mb-5" />
          <span>Prioritize Route Safety</span>
        </div>
      </div>
      <div
        className="flex flex-col items-center justify-center lora-font"
        style={{ backgroundColor: "#F4EEE5", letterSpacing: "0.3em" }}
      >
        <span className="text-5xl font-bold my-16">
          Plan Your Next Trip On Us
        </span>
        <img className="w-10/12 pb-12" src="/collage.png" alt="" />
      </div>
    </>
  );
};

export default About;
