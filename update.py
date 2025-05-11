import requests
import os
from datetime import datetime, timedelta, timezone

API_KEY = os.getenv("NASA_API_KEY", "DEMO_KEY")

def fetch_epic_image():
    date = datetime.now().date() - timedelta(days=2)
    date_str = date.strftime('%Y-%m-%d')

    # Get metadata
    meta_url = f"https://api.nasa.gov/EPIC/api/natural/date/{date_str}?api_key={API_KEY}"
    response = requests.get(meta_url)
    data = response.json()
    if not data:
        print("No EPIC image found for this date.")
        return

    image_name = data[0]['image']
    image_url = f"https://epic.gsfc.nasa.gov/archive/natural/{date.year}/{date.strftime('%m')}/{date.strftime('%d')}/jpg/{image_name}.jpg"
    explanation = data[0].get("caption", "Image captured by NASA's EPIC camera on DSCOVR.")
    coords = data[0].get("centroid_coordinates", {})
    lat = coords.get("lat", "N/A")
    lon = coords.get("lon", "N/A")

    # Download and save image
    os.makedirs("history", exist_ok=True)
    with open(f"history/{date_str}.jpg", "wb") as f:
        f.write(requests.get(image_url).content)
    with open("image.jpg", "wb") as f:
        f.write(requests.get(image_url).content)

    # Create README.md content
    with open("README.md", "w") as f:
        f.write(f"""# 🌍 EPIC Earth Image of the Day

This repository demonstrates my ability to automate GitHub workflows using GitHub Actions, interact with external APIs, and format live content.

---

## 📆 Date
**{date_str}**

---

## 🖼 Image
![EPIC Earth Image]({image_url})

---

## 📌 Metadata
- **Image Name:** `{image_name}`
- **Coordinates:** Latitude `{lat}`, Longitude `{lon}`
- **Description:** {explanation}

---

## 📡 About EPIC
The EPIC camera (Earth Polychromatic Imaging Camera) aboard NOAA's DSCOVR satellite captures full-color images of the Earth from Lagrange Point 1 (L1), 1 million miles away. These images are delayed 12–36 hours for processing.

- [NASA EPIC API](https://epic.gsfc.nasa.gov/about/api)
- [Image Archive](https://epic.gsfc.nasa.gov/)

---

## 📦 Archive
All past images saved to the `/history/` folder by date.

---

**Last updated:** {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}  
📸 Courtesy of NASA EPIC API
""")

if __name__ == "__main__":
    fetch_epic_image()
