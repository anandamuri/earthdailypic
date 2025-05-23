# Daily 🌎 Image

![Earth Image](./history/2025-05-22/162532.jpg)

**Coordinates:** 19.885254, -79.123535  
**Caption:** This image was taken by NASA's EPIC camera onboard the NOAA DSCOVR spacecraft

---

## Credits

- Updated using NASA's EPIC API 
- Imagery © NASA EPIC / NOAA DSCOVR spacecraft  
- This repo is powered by a GitHub Actions workflow that automates the entire process.

## What it does

- Runs daily at 13:00 UTC  
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

_Last updated: Fri May 23 15:31:55 UTC 2025_
