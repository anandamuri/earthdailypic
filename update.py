import requests
import datetime

API_KEY = 'SmrpI2PL8Ahh38cgYqhGskeRpauFtKIERaubKBAT'

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
    with open("image.jpg", "wb") as f:
        f.write(img_data)

    with open("README.md", "w") as f:
        f.write(f"""# 🌍 EPIC Earth Image of the Day\n\n![Earth Image]({image_url})\n\n**Date:** {date_str}\n\n**Image Name:** {image_name}\n\nMetadata:\n\n```json\n{str(data[0])}\n```\n\n📸 Image provided by NASA EPIC API\n""")

if __name__ == "__main__":
    fetch_epic_image()
