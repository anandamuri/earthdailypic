import os
import requests
from datetime import datetime, timedelta, timezone
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

def fetch_metadata_for_date(date):
    url = f"{EPIC_API_URL}/date/{date}?api_key={API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data:
            return data
    return None

# === Try yesterday's metadata first ===
target_date = (datetime.now(timezone.utc) - timedelta(days=1)).date()
print(f"📅 Trying to fetch EPIC image metadata for {target_date}")
data = fetch_metadata_for_date(target_date)

if not data:
    print(f"❌ No EPIC metadata for {target_date}. Using most recent image from history...")
    subfolders = sorted(Path(HISTORY_DIR).iterdir(), reverse=True)
    for folder in subfolders:
        if folder.is_dir():
            image_files = list(folder.glob("*.jpg"))
            if image_files:
                image_path = image_files[0]
                date_obj = datetime.strptime(folder.name, "%Y-%m-%d")
                filename = image_path.name
                image_name = filename.replace(".jpg", "")
                target_date = date_obj
                day_folder = folder
                print(f"📁 Using fallback image from {folder.name}")
                break
    else:
        raise Exception("❌ No fallback image found in history folder.")

    # Populate fake metadata fields
    closest_entry = {
        "image": image_name,
        "date": date_obj.strftime("%Y-%m-%d %H:%M:%S"),
        "caption": "Fallback image from previous successful day.",
        "centroid_coordinates": {"lat": ANN_ARBOR_LAT, "lon": ANN_ARBOR_LON}
    }

else:
    print(f"✅ Found metadata for {target_date}")
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
    try:
        img_response = requests.get(image_url, timeout=15)
        img_response.raise_for_status()
        with open(image_path, 'wb') as f:
            f.write(img_response.content)
        print(f"✅ Downloaded {filename} (closest to Ann Arbor)")
    except requests.exceptions.RequestException as e:
        raise Exception(f"❌ Failed to download image: {e}")

# === PREPARE README IMAGE BLOCK ===
image_rel_path = f"./{day_folder}/{filename}"
time_str = date_obj.strftime('%H:%M:%S')
caption = closest_entry.get("caption", "")
coords = closest_entry.get("centroid_coordinates", {})

readme_content = f"""# Daily 🌎 Image

![Earth Image]({image_rel_path})

**Coordinates:** {coords.get("lat")}, {coords.get("lon")}  
**Caption:** {caption}

---

## Credits

- Updated using NASA's EPIC API 
- Imagery © NASA EPIC / NOAA DSCOVR spacecraft  
- This repo is powered by a GitHub Actions workflow that automates the entire process.

## What it does

- Runs daily at 13:00 UTC  
- Downloads the EPIC image closest to Ann Arbor, Michigan  
- Updates this README with the latest image and its metadata  
- If NASA's EPIC API does not publish a new image, the script will display the most recent available image.

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
