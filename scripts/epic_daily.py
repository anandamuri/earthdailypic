import os
import requests
from datetime import datetime
from pathlib import Path

# === CONFIG ===
API_KEY = os.getenv("NASA_API_KEY", "DEMO_KEY")
EPIC_API_URL = "https://api.nasa.gov/EPIC/api/natural"
IMAGE_BASE_URL = "https://epic.gsfc.nasa.gov/archive/natural"
HISTORY_DIR = "history"
README_FILE = "README.md"

# === CREATE FOLDER ===
Path(HISTORY_DIR).mkdir(exist_ok=True)

# === FETCH LATEST IMAGE METADATA ===
response = requests.get(f"{EPIC_API_URL}?api_key={API_KEY}")
response.raise_for_status()
data = response.json()

if not data:
    raise Exception("No image data found from EPIC API.")

latest = data[0]
image_name = latest['image']
date_str = latest['date']
date_obj = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
date_path = date_obj.strftime("%Y/%m/%d")
filename = f"{date_obj.strftime('%Y-%m-%d')}_{image_name}.jpg"
image_url = f"{IMAGE_BASE_URL}/{date_path}/jpg/{image_name}.jpg"
image_path = os.path.join(HISTORY_DIR, filename)

# === DOWNLOAD IMAGE ===
img_response = requests.get(image_url)
img_response.raise_for_status()
with open(image_path, 'wb') as f:
    f.write(img_response.content)

print(f"✅ Downloaded image to: {os.path.abspath(image_path)}")

# === UPDATE README ===
metadata = {
    "date": date_obj.strftime("%Y-%m-%d"),
    "caption": latest.get("caption", "No caption available."),
    "coords": latest["centroid_coordinates"]
}

readme_content = f"""# Daily 🌍 Image

![Earth Image](./{HISTORY_DIR}/{filename})

**Date:** {metadata['date']}  
**Caption:** {metadata['caption']}  
**Centroid Coordinates:** (Lat: {metadata['coords']['lat']}, Lon: {metadata['coords']['lon']})

*Updated daily using NASA's EPIC API.*  
Imagery © NASA EPIC / DSCOVR  
This repo is powered by a GitHub Actions workflow that automates the entire process.

---

## 🛰️ What it does

- Runs automatically every day at 12:00 UTC  
- Fetches NASA's Earth image via the EPIC API  
- Updates this README with space imagery and descriptions  
- Commits and pushes these changes automatically  

## 🧠 Why I built this

This project showcases:

- GitHub Actions and CI/CD workflows  
- Automation scripts  
- Git operations from within workflows  
- Working with external APIs  

## ⚙️ How it works

The GitHub Action workflow:

1. Runs on a schedule (daily)  
2. Fetches NASA's EPIC Earth Image of the Day  
3. Updates this README  
4. Commits and pushes the changes  

_Last updated: {datetime.utcnow().strftime('%a %b %d %H:%M:%S UTC %Y')}_
"""

with open(README_FILE, "w", encoding="utf-8") as f:
    f.write(readme_content)

print("✅ README.md updated.")
