import React, { useEffect, useRef, useState } from "react";
import { GoogleMap, LoadScript } from "@react-google-maps/api";

const containerStyle = {
    width: "100%",
    height: "400px", // Ensures the map container has height
};

const center = {
    lat: 37.7749, // Replace with desired latitude
    lng: -122.4194, // Replace with desired longitude
};

const InteractiveNavigation = () => {
    const mapRef = useRef(null);
    const [mapLoaded, setMapLoaded] = useState(false);

    useEffect(() => {
        if (mapLoaded && mapRef.current) {
            const map = mapRef.current.state.map;
            console.log("Map instance after initialization:", map);

            try {
                // Check if AdvancedMarkerElement is available
                if (window.google?.maps?.marker?.AdvancedMarkerElement) {
                    console.log("Using AdvancedMarkerElement...");
                    const markerElement = document.createElement("div");
                    markerElement.style.backgroundColor = "red";
                    markerElement.style.width = "20px";
                    markerElement.style.height = "20px";
                    markerElement.style.borderRadius = "50%";

                    new window.google.maps.marker.AdvancedMarkerElement({
                        map, // Attach the advanced marker to the map
                        position: center,
                        content: markerElement, // Use custom content for the marker
                    });
                } else {
                    console.log("Fallback to standard Marker...");
                    new window.google.maps.Marker({
                        position: center,
                        map, // Attach marker to the map
                    });
                }
            } catch (error) {
                console.error("Error adding marker:", error);
            }
        }
    }, [mapLoaded]);

    return (
        <LoadScript
            googleMapsApiKey={process.env.REACT_APP_GOOGLE_MAPS_API_KEY}
            onError={(error) => console.error("LoadScript Error:", error)} // Catch API loading errors
        >
            <div style={{ width: "100%", display: "flex", justifyContent: "center" }}>
                <GoogleMap
                    mapContainerStyle={containerStyle}
                    center={center}
                    zoom={14}
                    onLoad={(map) => {
                        console.log("onLoad triggered, map instance:", map);
                        mapRef.current = { state: { map } }; // Save the map instance
                        setMapLoaded(true); // Mark the map as fully loaded
                    }}
                />
            </div>
        </LoadScript>
    );
};

export default InteractiveNavigation;
