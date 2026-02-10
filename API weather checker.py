import requests
import json
import time
import os
from datetime import datetime

# --- CONFIGURATION ---
CITY_LAT = 52.52  # Latitude (example: Berlin)
CITY_LON = 13.41  # Longitude
CACHE_FILE = "weather_cache.json"
UPDATE_INTERVAL = 600  # Update every 10 minutes (600 seconds)

def fetch_weather():
    """Tries to get fresh data from the internet."""
    url = f"https://api.open-meteo.com/v1/forecast?latitude={CITY_LAT}&longitude={CITY_LON}&current_weather=true"
    
    try:
        # Timeout set to 5 seconds so the app doesn't hang forever if net is slow
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()
        
        # Add a timestamp so we know when this was last updated
        data['last_updated'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Save to local file (The "Download" part)
        with open(CACHE_FILE, 'w') as f:
            json.dump(data, f)
            
        return data, True # Data, Is_Fresh
        
    except (requests.ConnectionError, requests.Timeout, requests.HTTPError):
        # Internet is down or server is acting up
        return load_cached_data(), False

def load_cached_data():
    """Reads the last successful download from the disk."""
    if os.path.exists(CACHE_FILE):
        with open(CACHE_FILE, 'r') as f:
            return json.load(f)
    return None

def display_weather(data, is_fresh):
    if data is None:
        print("❌ Error: No internet and no cached data available.")
        return

    current = data['current_weather']
    status = "🟢 [LIVE]" if is_fresh else f"🟠 [OFFLINE - Data from {data.get('last_updated', 'unknown')}]"
    
    print("-" * 30)
    print(f"WEATHER REPORT {status}")
    print(f"Temperature: {current['temperature']}°C")
    print(f"Wind Speed:  {current['windspeed']} km/h")
    print(f"Time:        {current['time']}")
    print("-" * 30)

def main():
    print("🚀 Weather Monitor started. Press Ctrl+C to stop.")
    while True:
        weather_data, fresh = fetch_weather()
        display_weather(weather_data, fresh)
        
        print(f"Waiting {UPDATE_INTERVAL//60} minutes for next automatic update...")
        time.sleep(UPDATE_INTERVAL)

if __name__ == "__main__":
    main()
