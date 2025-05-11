import requests
import os
from datetime import datetime, timedelta, timezone

API_KEY = os.getenv("NASA_API_KEY", "DEMO_KEY")
DATE = (datetime.now(timezone.utc) - timedelta(days=2)).date()
DATE_STR = DATE.strftime("%Y-%m-%d")

def fetch_epic_image():
    meta_url = f"https://api.nasa.gov/EPIC/api/natural/date/{DATE_STR}?api_key={API_KEY}"
    response = requests.get(meta_url)

    try:
        data = response.json()
    except Exception as e:
        print(f"Failed to parse JSON: {e}")
        return

    if not isinstance(data, list) or not data:
        print(f"No image data found for {DATE_STR}")
        update_readme_no_image()
        update_log_no_image()
        return

    first_image = data[0]
    image_name = first_image.get('image')
    if not image_name:
        print("Image key missing in first image object.")
        update_readme_no_image()
        update_log_no_image()
        return

    image_date = first_image.get('date', DATE_STR).split()[0]  # Format: 'YYYY-MM-DD'
    year, month, day = image_date.split("-")
    image_url = f"https://epic.gsfc.nasa.gov/archive/natural/{year}/{month}/{day}/jpg/{image_name}.jpg"
    img_data = requests.get(image_url).content

    os.makedirs("history", exist_ok=True)
    with open("image.jpg", "wb") as f:
        f.write(img_data)
    with open(f"history/{DATE_STR}.jpg", "wb") as f:
        f.write(img_data)

    with open("README.md", "w") as f:
        f.write(f"# 🌍 EPIC Earth Image of the Day\n\n")
        f.write(f"## 🗓️ Today's Image ({image_date})\n\n")
        f.write(f"![Earth Image]({image_url})\n\n")
        f.write("**📍 Location:** Lagrange Point 1 (L1) — 1 million miles from Earth  \n")
        f.write("**📷 Instrument:** EPIC (Earth Polychromatic Imaging Camera)  \n")
        f.write(f"**🕒 Last updated:** {datetime.now(timezone.utc).isoformat()}\n\n")
        f.write("## Archive\n")
        f.write("Images stored in the [/history](./history) folder.\n")

    with open("update_log.txt", "w") as f:
        f.write(f"Last updated: {datetime.now(timezone.utc).isoformat()}\n")
        f.write(f"Image: {image_name}.jpg\n")

def update_readme_no_image():
    with open("README.md", "w") as f:
        f.write(f"# 🌍 EPIC Earth Image of the Day\n\n")
        f.write(f"**Date:** {DATE_STR}\n\n")
        f.write("⚠️ No image available for this date.\n\n")
        f.write(f"🕒 Last updated: {datetime.now(timezone.utc).isoformat()}\n\n")
        f.write("## Archive\n")
        f.write("Images stored in the [/history](./history) folder.\n")

def update_log_no_image():
    with open("update_log.txt", "w") as f:
        f.write(f"Last updated: {datetime.now(timezone.utc).isoformat()}\n")
        f.write("No image available.\n")

if __name__ == "__main__":
    fetch_epic_image()
