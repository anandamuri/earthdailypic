# 🌍 EPIC Earth Image of the Day

This repository updates daily with the latest image of Earth taken by NASA's [EPIC Camera](https://epic.gsfc.nasa.gov/) on the DSCOVR satellite.

## 🗓️ Today's Image

*(This section is auto-filled every day)*

## 📂 Archive

Past images are stored in the [/history](./history) folder, named by date (e.g., `2025-05-11.jpg`).

---

## 🛠 How This Works

- Fetches NASA's EPIC metadata daily using GitHub Actions
- Downloads the latest image from 2 days ago (due to NASA's data delay)
- Updates this README and logs the change
- Auto-commits changes every morning at 5:00 AM EST (10:00 UTC)

---

## 📡 Data Source

[NASA EPIC API](https://epic.gsfc.nasa.gov/about/api)
