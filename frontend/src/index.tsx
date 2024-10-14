import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './app';


/*
index.tsx は Reactアプリの エントリーポイント（アプリケーションの開始地点）
*/

// ルートとなる要素を取得
const rootElement = document.getElementById('root');

// rootElement が null でないことをチェックしてから createRoot
if (rootElement) {
  const root = ReactDOM.createRoot(rootElement);
  
  // レンダリング
  root.render(
    <React.StrictMode>
      <App />
    </React.StrictMode>
  );
}
