import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './app';
import './styles/map.css';

// ルートとなる要素を取得
const rootElement = document.getElementById('root');

// rootElement が null でないことをチェックしてから createRoot
if (rootElement) {
  const root = ReactDOM.createRoot(rootElement);
  
  root.render(
    <React.StrictMode>
      <App />
    </React.StrictMode>
  );
}
