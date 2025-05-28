# Daily 🌎 Image

![Earth Image](./history/2025-05-25/161612.jpg)

**Coordinates:** 42.2808, -83.743  
**Caption:** Fallback image from previous successful day.

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

_Last updated: Wed May 28 19:37:50 UTC 2025_
