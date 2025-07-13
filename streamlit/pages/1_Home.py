import streamlit as st

st.set_page_config(page_title="Home", layout="wide")

st.title("🏠 Welcome to OLA Ride Insights Dashboard")

st.markdown("""
---

## 🚕 Project Summary

The **OLA Ride Insights** project is focused on analyzing ride-sharing data to improve customer experience, operational efficiency, and business strategies. This interactive web application uses **Streamlit** and **SQL** to present real-time insights from OLA’s ride history.

---

## 🎯 Key Objectives

- Identify booking trends and peak hours  
- Understand customer behavior through ratings and ride data  
- Detect cancellations and explore reasons  
- Analyze payment preferences and vehicle performance  
- Visualize data interactively for better decision-making

---

## 🛠️ Tools & Technologies Used

- **Python (Pandas, Streamlit)**
- **SQL (MySQL)**
- **Matplotlib / Seaborn**

---

## 📊 Application Features

- 🔍 **Dashboard with 10 SQL-based insights**
- 📋 Real-time table and graph visualizations
- 📁 Cleaned and structured dataset from raw Excel

---

## 🧠 Business Use Cases

- Optimize driver allocation during high-demand hours  
- Tailor marketing strategies based on customer history  
- Reduce cancellations and understand user pain-points  
- Monitor ride revenue across different payment methods  
- Track performance of vehicle categories

---

> 🚀 Navigate to the **Dashboard** from the sidebar to explore all insights!

---
""")
