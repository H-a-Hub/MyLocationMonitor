import React from 'react';
import MapPage from './components/MapPage';

/**
 * アプリ本体 Reactコンポーネント
 * 
 * サブコンポーネントを紐づけることで各機能を実現します
 * 
 * @returns {JSX.Element} JSX要素
 */
const App: React.FC = () => {
  return (
    <div className="App">
      <div>test</div>
      <MapPage />
    </div>
  );
};

export default App;
