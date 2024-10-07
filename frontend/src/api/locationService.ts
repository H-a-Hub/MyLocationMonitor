import axios from 'axios';

const API_BASE_URL = 'http://localhost:5000/api';

export interface Location {
  lat: number;
  lng: number;
}

/**
 * 位置情報履歴をフェッチ
 * 
 * backendのWebAPIにリクエストして位置情報を取得します
 * 
 * @returns {response.data} レスポンスデータ（JSON形式）
 */
export const fetchLocationHistory = async (): Promise<Location[]> => {
  try {
    // backend API へ位置情報履歴をリクエスト
    const response = await axios.get<Location[]>(`${API_BASE_URL}/locations`);
    return response.data;
  } catch (error) {
    console.error('Error fetching location data:', error);
    throw error;
  }
};
