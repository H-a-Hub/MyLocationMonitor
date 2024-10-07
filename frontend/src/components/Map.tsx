import React from 'react';
import { MapContainer, TileLayer, Polyline } from 'react-leaflet';
import { LatLngExpression } from 'leaflet';
import 'leaflet/dist/leaflet.css';
import { Location } from '../api/locationService';

interface MapProps {
  locations: Location[];
}

/**
 * 地図 Reactコンポーネント
 * 
 * 地図を表示するコンポーネントです。
 * マーカーやポリラインを描画します。
 * 
 * @returns {JSX.Element} 地図を含むJSX要素
 */
const Map: React.FC<MapProps> = ({ locations }) => {
  // MapContainerPropsに準拠したプロパティを設定
  const center: LatLngExpression = [locations[0].lat, locations[0].lng];
  const zoom: number = 13;

  return (
    // <MapContainer center={center} zoom={zoom}>
    <MapContainer>
      <TileLayer
        url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
        // attribution={'&copy; OpenStreetMap contributors'}
      />
      <Polyline positions={locations.map(loc => [loc.lat, loc.lng] as LatLngExpression)} />
    </MapContainer>
  );
};

export default Map;
