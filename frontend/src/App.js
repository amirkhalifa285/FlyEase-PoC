import React, { useEffect, useState } from "react";
import axios from "axios";
import './App.css';
import InteractiveNavigation from "./pages/InteractiveNavigation";

function App() {
    const [flights, setFlights] = useState([]);
    const [queueData, setQueueData] = useState({ current: {}, predicted: {} });

    useEffect(() => {
        axios.get("http://127.0.0.1:8000/flights")
            .then((response) => setFlights(response.data))
            .catch((error) => console.error("Error fetching flights:", error));
    }, []);

    useEffect(() => {
        axios.get("http://127.0.0.1:8000/queue-times")
            .then((response) => setQueueData(response.data))
            .catch((error) => console.error("Error fetching queue times:", error));
    }, []);

    return (
        <div className="App">
            <header className="App-header">
                <h1>FlyEase PoC</h1>
                <section>
                    <h2>Real-Time Flight Updates</h2>
                    <ul>
                        {flights.map((flight) => (
                            <li key={flight.id}>
                                Flight {flight.id}: {flight.status} at Gate {flight.gate}
                            </li>
                        ))}
                    </ul>
                </section>

                <section>
                    <h2>Queue Time Prediction</h2>
                    <h3>Current Queue Times</h3>
                    <ul>
                        {Object.entries(queueData.current).map(([key, value]) => (
                            <li key={key}>
                                {key}: {value} minutes
                            </li>
                        ))}
                    </ul>
                    <h3>Predicted Queue Times</h3>
                    <ul>
                        {Object.entries(queueData.predicted).map(([key, value]) => (
                            <li key={key}>
                                {key}: {value} minutes
                            </li>
                        ))}
                    </ul>
                </section>
            </header>

            {/* Map in its own "window" container */}
            <section
                style={{
                    width: "80%",
                    maxWidth: "600px",
                    height: "300px",
                    margin: "0 auto",
                    border: "1px solid #ccc",
                    borderRadius: "8px",
                    boxShadow: "0 2px 6px rgba(0,0,0,0.3)",
                    overflow: "hidden",
                    flex: 1
                }}
            >
                <InteractiveNavigation />
            </section>
        </div>
    );
}

export default App;
