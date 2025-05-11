# 🌍 EPIC Earth Image of the Day

This repository updates daily with the latest image of Earth taken by NASA's [EPIC Camera](https://epic.gsfc.nasa.gov/) on the DSCOVR satellite.

## 🗓️ Today's Image (2025-05-11)

![Earth Image](https://epic.gsfc.nasa.gov/archive/natural/2025/05/11/jpg/epic_1b_20250511001509.jpg)

**📍 Location:** Lagrange Point 1 (L1) — 1 million miles from Earth  
**📷 Instrument:** EPIC (Earth Polychromatic Imaging Camera)  
**🕒 Last updated:** 2025-05-11T10:00:01Z

---

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

---

