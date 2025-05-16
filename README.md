# 🌍 EPIC Earth Image of the Day

This repository updates daily with the latest image of Earth taken by NASA's [EPIC Camera](https://epic.gsfc.nasa.gov/) aboard the DSCOVR satellite.

## 🗓️ Today's Image

*This section is automatically updated every day with the most recent available image and its metadata.*

![Earth Image](./history/placeholder.jpg)  
**Date:** YYYY-MM-DD  
**Caption:** Placeholder caption  
**Centroid Coordinates:** (Lat: 0.0, Lon: 0.0)

## 📂 Archive

Past images are stored in the [`/history`](./history) folder and named by date and image ID (e.g., `2025-05-11_epic_1b_20250511000000.jpg`).

---

## 🛠 How This Works

- A GitHub Actions workflow runs daily at **5:00 AM EST (10:00 UTC)**
- Fetches metadata using [NASA's EPIC API](https://epic.gsfc.nasa.gov/about/api)
- Downloads the most recent natural color image available
- Updates the `README.md` with:
  - The image
  - The capture date
  - Caption
  - Centroid coordinates
- Commits and pushes the update back to this repo
- Older images accumulate in the `history/` folder

---

## 📡 Data Source

- [NASA EPIC API](https://epic.gsfc.nasa.gov/about/api)
- Imagery © NASA EPIC / DSCOVR

---

## 🤖 Automation

This repo is powered by a GitHub Actions workflow that automates the entire process. You can view the workflow file [here](.github/workflows/update.yml).
