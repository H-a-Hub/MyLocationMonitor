import axios from 'axios';

const API_BASE_URL = 'http://localhost:5000/api';

export interface Location {
  lat: number;
  lng: number;
}

export const fetchLocationHistory = async (): Promise<Location[]> => {
  try {
    const response = await axios.get<Location[]>(`${API_BASE_URL}/locations`);
    return response.data;
  } catch (error) {
    console.error('Error fetching location data:', error);
    throw error;
  }
};
