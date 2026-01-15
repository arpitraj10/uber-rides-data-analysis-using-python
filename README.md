# 🚗 Uber Rides Data Analysis Dashboard

An interactive **data analysis and visualization dashboard** built using **Python** and **Streamlit** to explore Uber ride data. This project provides insights into ride patterns by time, category, distance, and purpose, along with a sleek **UI/UX interface** and deployable web application.

---

## 📌 Project Overview

This repository contains a full-stack project that transforms raw Uber ride data into an interactive web dashboard.  
It shows trends and insights using charts and filters — perfect for analysis and real-world usage.

The project includes:
- 🚀 A **Streamlit web app**
- 📊 Interactive visualizations
- 💡 Filters for **Category** and **Purpose**
- 📁 Modular & clean code structure

---

## 📁 Folder Structure

uber-rides-data-analysis/
│
├── app.py # Streamlit main app
├── requirements.txt # Python dependencies
│
├── data/
│ └── uber_rides.csv # Dataset used for analysis
│
├── utils/
│ ├── init.py # Makes utils a package
│ ├── data_loader.py # Loads data
│ ├── preprocessing.py # Cleans and preprocesses data
│ └── visualizations.py # Charting functions
│
├── assets/
│ └── screenshots/ # Screenshots for README/demo
│
└── README.md # Project description


---

## 📊 What You Can Do With the App

🔹 Visualize rides by hour of the day  
🔹 Compare rides by category (Business vs Personal)  
🔹 See purpose distribution (Meetings, Errands, Personal, etc.)  
🔹 Dynamic filtering of data  
🔹 Beautiful KPI cards to highlight key metrics  
🔹 Ideally styled with dark mode UI/UX enhancements

---

## 🛠 Technology Stack

| Layer | Technology |
|-------|-----------|
| Frontend | Streamlit |
| Backend | Python |
| Data | Pandas, NumPy |
| Visualizations | Plotly |

---

## 📥 Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/arpitraj10/uber-rides-data-analysis-using-python.git
cd uber-rides-data-analysis-using-python


2. Create and activate a virtual environment (optional)
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

3. Install dependencies
pip install -r requirements.txt

4. Run the app locally
https://uber-rides-data-analysis-using-python-atr48kllyz8npbojknzumq.streamlit.app/

