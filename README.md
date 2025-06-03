# Daily 🌎 Image

![Earth Image](./history/2025-06-02/192312.jpg)

**Coordinates:** 20.002441, -121.325684  
**Caption:** This image was taken by NASA's EPIC camera onboard the NOAA DSCOVR spacecraft

---

## Credits

- Updated using NASA's EPIC API 
- Imagery © NASA EPIC / NOAA DSCOVR spacecraft  
- This repo is powered by a GitHub Actions workflow that automates the entire process.

## What it does

- Runs daily at 13:00 UTC  
- Downloads a random EPIC image of Earth  
- Updates this README with the latest image and its metadata  
- If NASA's EPIC API does not publish a new image, the script will display the most recent available image.

## Why I built this

- GitHub Actions and workflows  
- Automation scripts 
- Python scripts
- Git operations from within workflows  
- Working with external APIs  
- Show a daily random image of Earth

## How it works

- Fetches all available EPIC images  
- Picks one at random  
- Saves the image  
- Updates this README  

_Last updated: Tue Jun 03 13:35:23 UTC 2025_
