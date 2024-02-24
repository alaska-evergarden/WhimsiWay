import "../App.css";

const Heatmap = () => {
  return (
    <div className="flex justify-center align-middle">
      <iframe
        style={{ width: "50%", height: 400 }}
        src={"heatmap.html"}
      ></iframe>
    </div>
  );
};

export default Heatmap;
