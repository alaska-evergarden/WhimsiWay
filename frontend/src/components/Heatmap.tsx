import "../App.css";

const Heatmap = () => {
  return (
    <div className="flex flex-col h-lvh justify-center items-center lora-font">
      <div className="text-4xl font-bold my-10">
        <span>How Do I Avoid Accidents?</span>
      </div>
      <div>
        <span>Historical Texas Accidents (2016-2023)</span>
      </div>
      <div className="flex p-10 w-4/5 bg-white justify-center rounded-xl">
        <iframe
          className="rounded-xl"
          style={{ width: "100%", height: 600 }}
          src={"/heatmap.html"}
        ></iframe>
      </div>
    </div>
  );
};

export default Heatmap;
