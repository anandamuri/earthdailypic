# Daily 🌍 Image Closest to Ann Arbor, MI

![Earth Image](./history/2025-05-15/162534.jpg)

**Time (UTC):** 16:25:34  
**Coordinates:** Latitude 19.445801, Longitude -79.49707  
**Caption:** This image was taken by NASA's EPIC camera onboard the NOAA DSCOVR spacecraft

---

## Credits
Updated using NASA's EPIC API 
Imagery © NASA EPIC / NOAA DSCOVR spacecraft  
This repo is powered by a GitHub Actions workflow that automates the entire process.

## What it does

- Runs daily at 9:00 UTC  
- Downloads the EPIC image closest to Ann Arbor, Michigan  
- Updates this README with the latest image and its metadata  

## Why I built this

- GitHub Actions and workflows  
- Automation scripts  
- Git operations from within workflows  
- Working with external APIs  
- Show the side of the Earth with Michigan

## How it works

1. Fetches all available EPIC images  
2. Finds the one closest to Ann Arbor using centroid coordinates  
3. Saves the image  
4. Updates this README  

_Last updated: Fri May 16 15:41:00 UTC 2025_
