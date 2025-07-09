import React, { useState } from "react";
import "./Home.css";

const Home = () => {
  // State to hold form data
  const [homeworld, setHomeworld] = useState("");
  const [unitType, setUnitType] = useState("");

  const handleHomeworldChange = (event) => {
    setHomeworld(event.target.value);
  };

  const handleUnitTypeChange = (event) => {
    setUnitType(event.target.value);
  };

  const handleSubmit = async (event) => {
    event.preventDefault();

    const data = {
      homeworld: homeworld,
      unitType: unitType,
    };

    try {
      const response = await fetch("http://127.0.0.1:5000/predict", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(data),
      });

      const result = await response.json();
      console.log(result);

      if (response.ok) {
        alert("Data submitted successfully!");
      } else {
        alert("Error: " + result.error);
      }
    } catch (error) {
      console.error("Error submitting the form:", error);
    }
  };

  return (
    <div className="container">
      <h2 className="heading">User Info</h2>
      <form className="form" onSubmit={handleSubmit}>
        <div className="formGroup">
          <label className="label">Homeworld:</label>
          <input
            type="text"
            name="homeworld"
            className="input"
            value={homeworld}
            onChange={handleHomeworldChange}
          />
        </div>
        <div className="formGroup">
          <label className="label">Unit Type:</label>
          <input
            type="text"
            name="unitType"
            className="input"
            value={unitType}
            onChange={handleUnitTypeChange}
          />
        </div>
        <input type="submit" value="Submit" className="submitButton" />
      </form>
    </div>
  );
};

export default Home;
