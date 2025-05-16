# Daily 🌍 Image

<div style="text-align: center;">
    <img src="./history/2025-05-15/162534.jpg" alt="Earth at 16:25:34" width="400" title="This image was taken by NASA's EPIC camera onboard the NOAA DSCOVR spacecraft"><br>
    <sub><strong>16:25:34 UTC</strong></sub><br>
    <sub>19.445801, -79.49707</sub>
</div>

---

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

_Last updated: Fri May 16 15:36:12 UTC 2025_
