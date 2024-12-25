import React, { useEffect, useState } from "react";
import axios from "axios";

const QueuePrediction = () => {
    const [queueData, setQueueData] = useState({ current: {}, predicted: {} });

    useEffect(() => {
        // Fetch queue data from backend
        axios.get("http://127.0.0.1:8000/queue-times")
            .then((response) => setQueueData(response.data))
            .catch((error) => console.error("Error fetching queue times:", error));
    }, []);

    return (
        <div>
            <h1>Queue Time Prediction</h1>
            <h2>Current Queue Times</h2>
            <ul>
                {Object.entries(queueData.current).map(([key, value]) => (
                    <li key={key}>
                        {key}: {value} minutes
                    </li>
                ))}
            </ul>
            <h2>Predicted Queue Times</h2>
            <ul>
                {Object.entries(queueData.predicted).map(([key, value]) => (
                    <li key={key}>
                        {key}: {value} minutes
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default QueuePrediction;
