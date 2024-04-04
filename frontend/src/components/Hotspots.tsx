import { useEffect, useState } from "react";
import Navbar from "./Navbar";
import axios from "axios";

const Hotspots = () => {
  const [city, setCity] = useState("");
  const [reload, setReload] = useState(false);

  const handleKeyDown = (event: any) => {
    if (event.key === "Enter") submit();
  };

  const submit = async () => {
    try {
      const res = await axios.get(
        "https://us-central1-ashs-wrld.cloudfunctions.net/collections_api/endpoint",
        {
          params: {
            city: city,
          },
        }
      );
      console.log(res.data);
      setReload(true);
    } catch (error) {
      console.log(error);
    }
  };

  useEffect(() => {
    // Reset reload state after iframe has remounted
    if (reload) {
      setReload(false);
    }
  }, [reload]);

  return (
    <>
      <Navbar />
      <div className="flex lora-font">
        <div
          className="flex my-5 rounded-lg bg-white"
          style={{ marginLeft: "4em" }}
        >
          <input
            type="text"
            className="p-2 m-2 rounded"
            placeholder="Enter a city in Texas"
            onChange={(e) => setCity(e.target.value)}
            onKeyDown={handleKeyDown}
          />
          <button className="p-2 m-2 w-10" onClick={submit}>
            <img src="search-interface-symbol.png" alt="" />
          </button>
        </div>
        <iframe
          key={reload.toString()}
          style={{
            width: "100%",
            height: 600,
            position: "absolute",
            zIndex: -1,
          }}
          src={"top_5_hotspots_map.html"}
        ></iframe>
      </div>
    </>
  );
};

export default Hotspots;
