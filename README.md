# VERIFY360 Scam Verification System (Truecaller-like)

A web-based scam detection platform that allows users to verify whether a **mobile number, website, WhatsApp account, or Instagram ID** is genuine or associated with scams.

This system checks the input against a **centralized database** and instantly classifies it as:

✅ Genuine
❌ Scam
⚠ Not Found

---

## Problem Statement

Online fraud and scam activities are increasing rapidly through phone calls, fake websites, and social media accounts.
Users often cannot identify whether a contact or website is trustworthy.

This project provides a **simple verification tool** to help users detect suspicious entities using stored scam records.

---

## Features

* Search any mobile number
* Verify websites/URLs
* Check WhatsApp contacts
* Verify Instagram IDs
* Instant classification (Safe / Scam / Not Found)
* Centralized database storage
* Simple and responsive web interface

---

## Tech Stack

**Frontend**

* HTML
* CSS
* Bootstrap

**Backend**

* Python Flask

**Database**

* SQLite

---

## System Architecture

User Input → Flask Server → SQLite Database → Result Display

1. User enters value
2. Backend checks database
3. Matching record found
4. Displays result instantly

---

## Project Structure

```
scam-detection-system/
│
├── app.py               # Flask backend
├── scam.db              # SQLite database
├── requirements.txt     # Dependencies
├── README.md            # Documentation
│
├── templates/
│     ├── index.html     # Home page
│     └── result.html    # Result page
```

---

## How to Run the Project

### Step 1 — Install dependencies

```
pip install -r requirements.txt
```

### Step 2 — Run server

```
python app.py
```

### Step 3 — Open browser

```
http://127.0.0.1:5000
```

---

## Sample Test Inputs

| Value              | Type    | Result    |
| ------------------ | ------- | --------- |
| 9876543210         | Mobile  | Scam      |
| realstore.com      | Website | Genuine   |
| amazon-support.net | Website | Scam      |
| random123          | Any     | Not Found |

---

## Future Enhancements

* Integration with Truecaller API
* Machine Learning based scam prediction
* Real-time crowd-sourced reporting
* Admin dashboard
* CSV bulk upload
* Cloud deployment

---

## Applications

* Fraud detection
* Cybersecurity awareness
* Phone number verification
* Fake website detection
* Social media scam identification

---

## Team Members

* MUGUNDAN V Y - 311422104063
* PRANAV A - 311422104072
* SHANMUGAM GOWTHAM S - 311422104084
* JAGADEESH R K - 311422104304

---
## License

This project is developed for educational and academic purposes.

