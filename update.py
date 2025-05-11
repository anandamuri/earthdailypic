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

    # 🛡️ Check if data is empty
    if not isinstance(data, list) or len(data) == 0:
        print(f"No EPIC image found for date {DATE_STR}. Full response:\n{data}")
        
        # Optional: Update README anyway to reflect status
        with open("README.md", "w") as f:
            f.write(f"# 🌍 EPIC Earth Image of the Day\n\n")
            f.write(f"**Date:** {DATE_STR}\n\n")
            f.write(f"⚠️ No image available for this date.\n\n")
            f.write(f"🕒 Last updated: {datetime.now(timezone.utc).isoformat()}\n\n")
            f.write("## Archive\n")
            f.write("Images stored in the [/history](./history) folder.\n")
        
        with open("update_log.txt", "w") as f:
            f.write(f"Last updated: {datetime.now(timezone.utc).isoformat()}\n")
            f.write("No image available.\n")

        return

    image_name = data[0]['image']
    year, month, day = DATE.strftime('%Y %m %d').split()
    image_url = f"https://epic.gsfc.nasa.gov/archive/natural/{year}/{month}/{day}/jpg/{image_name}.jpg"

    os.makedirs("history", exist_ok=True)

    # Save today's image
    with open("image.jpg", "wb") as f:
        f.write(requests.get(image_url).content)

    # Archive image by date
    with open(f"history/{DATE_STR}.jpg", "wb") as f:
        f.write(requests.get(image_url).content)

    # Update README
    with open("README.md", "w") as f:
        f.write(f"# 🌍 EPIC Earth Image of the Day\n\n")
        f.write(f"**Date:** {DATE_STR}\n\n")
        f.write(f"![Earth Image]({image_url})\n\n")
        f.write(f"📸 Image name: `{image_name}.jpg`\n\n")
        f.write(f"🕒 Last updated: {datetime.now(timezone.utc).isoformat()}\n\n")
        f.write(f"## Archive\n")
        f.write("Images stored in the [/history](./history) folder.\n")

    # Update log file
    with open("update_log.txt", "w") as f:
        f.write(f"Last updated: {datetime.now(timezone.utc).isoformat()}\n")
        f.write(f"Image: {image_name}.jpg\n")
    meta_url = f"https://api.nasa.gov/EPIC/api/natural/date/{DATE_STR}?api_key={API_KEY}"
    response = requests.get(meta_url)
    
    try:
        data = response.json()
    except Exception as e:
        print(f"Failed to parse JSON: {e}")
        return

    if not data:
        print(f"No image found for {DATE_STR}")
        return

    image_name = data[0]['image']
    year, month, day = DATE.strftime('%Y %m %d').split()
    image_url = f"https://epic.gsfc.nasa.gov/archive/natural/{year}/{month}/{day}/jpg/{image_name}.jpg"

    os.makedirs("history", exist_ok=True)

    # Save today's image
    with open("image.jpg", "wb") as f:
        f.write(requests.get(image_url).content)

    # Archive image by date
    with open(f"history/{DATE_STR}.jpg", "wb") as f:
        f.write(requests.get(image_url).content)

    # Update README
    with open("README.md", "w") as f:
        f.write(f"# 🌍 EPIC Earth Image of the Day\n\n")
        f.write(f"**Date:** {DATE_STR}\n\n")
        f.write(f"![Earth Image]({image_url})\n\n")
        f.write(f"📸 Image name: `{image_name}.jpg`\n\n")
        f.write(f"🕒 Last updated: {datetime.now(timezone.utc).isoformat()}\n\n")
        f.write(f"## Archive\n")
        f.write("Images stored in the [/history](./history) folder.\n")

    # Update log file
    with open("update_log.txt", "w") as f:
        f.write(f"Last updated: {datetime.now(timezone.utc).isoformat()}\n")
        f.write(f"Image: {image_name}.jpg\n")

if __name__ == "__main__":
    fetch_epic_image()
