import requests
import datetime
import os
from datetime import datetime, timezone

API_KEY = os.getenv("NASA_API_KEY", "DEMO_KEY")

def fetch_epic_image():
    date = datetime.date.today() - datetime.timedelta(days=2)
    date_str = date.strftime('%Y-%m-%d')

    meta_url = f"https://api.nasa.gov/EPIC/api/natural/date/{date_str}?api_key={API_KEY}"
    response = requests.get(meta_url)
    data = response.json()

    if not data:
        print("No image found for the date.")
        return

    image_name = data[0]['image']
    image_url = f"https://epic.gsfc.nasa.gov/archive/natural/{date.year}/{date.strftime('%m')}/{date.strftime('%d')}/jpg/{image_name}.jpg"

    img_data = requests.get(image_url).content

    # Save to history folder
    os.makedirs("history", exist_ok=True)
    with open(f"history/{date_str}.jpg", "wb") as f:
        f.write(img_data)

    # Save as latest image
    with open("image.jpg", "wb") as f:
        f.write(img_data)

    # Read existing README
    with open("README.md", "r") as f:
        readme = f.read()

    # Define auto-update block
    start_tag = "<!-- BEGIN AUTO-UPDATE -->"
    end_tag = "<!-- END AUTO-UPDATE -->"

    before = readme.split(start_tag)[0]
    after = readme.split(end_tag)[1]

    auto_content = f"""{start_tag}
![Earth Image]({image_url})

**Date:** {date_str}  
**Image Name:** {image_name}

Metadata:
```json
{data[0]}
```

📸 Image provided by NASA EPIC API  
🕒 Last updated: {datetime.now(timezone.utc).isoformat()}
{end_tag}"""

    # Combine and write back
    new_readme = before + auto_content + after
    with open("README.md", "w") as f:
        f.write(new_readme)

if __name__ == "__main__":
    fetch_epic_image()
