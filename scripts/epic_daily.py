import os
import requests
from datetime import datetime, timezone
from pathlib import Path

# === CONFIG ===
API_KEY = os.getenv("NASA_API_KEY", "DEMO_KEY")
EPIC_API_URL = "https://api.nasa.gov/EPIC/api/natural"
IMAGE_BASE_URL = "https://epic.gsfc.nasa.gov/archive/natural"
HISTORY_DIR = "history"
README_FILE = "README.md"

ANN_ARBOR_LAT = 42.2808
ANN_ARBOR_LON = -83.7430

# === CREATE MAIN HISTORY FOLDER ===
Path(HISTORY_DIR).mkdir(exist_ok=True)

# === FETCH LATEST IMAGE METADATA ===
response = requests.get(f"{EPIC_API_URL}?api_key={API_KEY}")
response.raise_for_status()
data = response.json()

if not data:
    raise Exception("No image data found from EPIC API.")

# === Find image closest to Ann Arbor ===
def distance(coord1, coord2):
    return (coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2

target_coord = (ANN_ARBOR_LAT, ANN_ARBOR_LON)
closest_entry = min(
    data,
    key=lambda entry: distance(
        (entry["centroid_coordinates"]["lat"], entry["centroid_coordinates"]["lon"]),
        target_coord
    )
)

# === PROCESS SELECTED IMAGE ===
image_name = closest_entry['image']
date_str = closest_entry['date']
date_obj = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
date_path = date_obj.strftime("%Y/%m/%d")

day_folder = os.path.join(HISTORY_DIR, date_obj.strftime("%Y-%m-%d"))
Path(day_folder).mkdir(parents=True, exist_ok=True)
filename = f"{date_obj.strftime('%H%M%S')}.jpg"
image_url = f"{IMAGE_BASE_URL}/{date_path}/jpg/{image_name}.jpg"
image_path = os.path.join(day_folder, filename)

# Download image
img_response = requests.get(image_url)
img_response.raise_for_status()
with open(image_path, 'wb') as f:
    f.write(img_response.content)

print(f"✅ Downloaded {filename} (closest to Ann Arbor)")

# === PREPARE README IMAGE BLOCK ===
image_rel_path = f"./{day_folder}/{filename}"
time_str = date_obj.strftime('%H:%M:%S')
caption = closest_entry.get("caption", "")
coords = closest_entry.get("centroid_coordinates", {})

readme_content = f"""# Daily 🌍 Image

![Earth Image]({image_rel_path})

**Coordinates:** {coords.get("lat")}, {coords.get("lon")}  
**Caption:** {caption}

---

## Credits

- Updated using NASA's EPIC API 
- Imagery © NASA EPIC / NOAA DSCOVR spacecraft  
- This repo is powered by a GitHub Actions workflow that automates the entire process.

## What it does

- Runs daily at 9:00 UTC  
- Downloads the EPIC image closest to Ann Arbor, Michigan  
- Updates this README with the latest image and its metadata  

## Why I built this

- GitHub Actions and workflows  
- Automation scripts 
- Python scripts
- Git operations from within workflows  
- Working with external APIs  
- Show the side of the Earth with Michigan

## How it works

- Fetches all available EPIC images  
- Finds the one closest to Ann Arbor using centroid coordinates  
- Saves the image  
- Updates this README  

_Last updated: {datetime.now(timezone.utc).strftime('%a %b %d %H:%M:%S UTC %Y')}_
"""

# === WRITE TO README ===
with open(README_FILE, "w", encoding="utf-8") as f:
    f.write(readme_content)

print("✅ README.md updated.")


# make sure any changes you make first git pull -rebase, remove all files from history, then rerun action to test