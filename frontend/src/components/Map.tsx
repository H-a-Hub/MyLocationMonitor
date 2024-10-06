import React from 'react';
import { MapContainer, TileLayer, Polyline } from 'react-leaflet';
import 'leaflet/dist/leaflet.css';
import { Location } from '../api/locationService';

interface MapProps {
  locations: Location[];
}

const Map: React.FC<MapProps> = ({ locations }) => {
  return (
    <MapContainer center={[locations[0].lat, locations[0].lng]} zoom={13}>
      <TileLayer
        url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
        attribution="&copy; OpenStreetMap contributors"
      />
      <Polyline positions={locations.map(loc => [loc.lat, loc.lng])} />
    </MapContainer>
  );
};

export default Map;
