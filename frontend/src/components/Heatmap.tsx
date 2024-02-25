import "../App.css";

const Heatmap = () => {
  return (
    <div className="flex h-lvh justify-center items-center">
      <iframe
        style={{ width: "80%", height: 600 }}
        src={"heatmap.html"}
      ></iframe>
    </div>
  );
};

export default Heatmap;
