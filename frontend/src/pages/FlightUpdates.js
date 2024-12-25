import React, { useEffect, useState } from "react";
import axios from "axios";

const FlightUpdates = () => {
    const [flights, setFlights] = useState([]);

    // Fetch flights from backend
    useEffect(() => {
        axios.get("http://127.0.0.1:8000/flights")
            .then((response) => setFlights(response.data))
            .catch((error) => console.error("Error fetching flights:", error));
    }, []);

    return (
        <div>
            <h1>Real-Time Flight Updates</h1>
            <ul>
                {flights.map((flight) => (
                    <li key={flight.id}>
                        Flight {flight.id}: {flight.status} at Gate {flight.gate}
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default FlightUpdates;
