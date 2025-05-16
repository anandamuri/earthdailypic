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

readme_images = []
for entry in data:
    image_name = entry['image']
    date_str = entry['date']
    date_obj = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
    date_path = date_obj.strftime("%Y/%m/%d")
    filename = f"{date_obj.strftime('%Y-%m-%d_%H%M%S')}_{image_name}.jpg"
    image_url = f"{IMAGE_BASE_URL}/{date_path}/jpg/{image_name}.jpg"
    image_path = os.path.join(HISTORY_DIR, filename)

    # Download image
    img_response = requests.get(image_url)
    img_response.raise_for_status()
    with open(image_path, 'wb') as f:
        f.write(img_response.content)

    print(f"✅ Downloaded {filename}")

    # Add to README block
    caption = entry.get("caption", "No caption available.")
    coords = entry.get("centroid_coordinates", {})
    readme_images.append(
        f"### 🕒 {date_obj.strftime('%H:%M:%S')} UTC\n"
        f"![Earth Image](./{HISTORY_DIR}/{filename})\n"
        f"**Caption:** {caption}  \n"
        f"**Centroid Coordinates:** (Lat: {coords.get('lat', 'N/A')}, Lon: {coords.get('lon', 'N/A')})\n\n"
    )

# === BUILD README CONTENT ===
readme_content = f"""# Daily 🌍 Earth Images

{''.join(readme_images)}

---

*Updated using NASA's EPIC API*  
Imagery © NASA EPIC / DSCOVR  
This repo is powered by a GitHub Actions workflow that automates the entire process.

## 🛰️ What it does

- Runs automatically every day at 9:00 UTC  
- Fetches NASA's Earth images via the EPIC API  
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
2. Fetches NASA's EPIC Earth Images of the Day  
3. Updates this README  
4. Commits and pushes the changes  

_Last updated: {datetime.utcnow().strftime('%a %b %d %H:%M:%S UTC %Y')}_
"""

# === WRITE TO README ===
with open(README_FILE, "w", encoding="utf-8") as f:
    f.write(readme_content)

print("✅ README.md updated.")
