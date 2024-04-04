import Navbar from "./Navbar";

const RouteFinder = () => {
  return (
    <>
      <Navbar />
      <div className="flex w-lvw h-lvh">
        <iframe className="w-lvw" src="/route_finder.html"></iframe>
      </div>
    </>
  );
};

export default RouteFinder;
