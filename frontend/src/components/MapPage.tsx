import React, { useEffect, useState } from 'react';
import Map from '../components/Map';
import { fetchLocationHistory, Location } from '../api/locationService';

/**
 * 地図ページのReactコンポーネント
 * 
 * このコンポーネントは地図を表示するためのメインページです。
 * ロード中の表示に対応しています
 * 
 * @returns {JSX.Element} 地図を含むJSX要素
 */
const MapPage: React.FC = () => {  

  const [locations, setLocations] = useState<Location[]>([]);

  // 初回起動時のエフェクト
  useEffect(() => {
    const getLocations = async () => {
      try {
        const data = await fetchLocationHistory();
        setLocations(data);
      } catch (error) {
        console.error('Failed to fetch locations:', error);
      }
    };

    getLocations();
  }, []);

  return (
    <div>
      {locations.length > 0 ? <Map locations={locations} /> : <p>Loading...</p>}
    </div>
  );
};

export default MapPage;
