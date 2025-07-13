# streamlit/pages/2_Dashboard.py

import streamlit as st
import pandas as pd
import mysql.connector
import matplotlib.pyplot as plt
import seaborn as sns

# --- Page Setup ---
st.set_page_config(page_title="Dashboard", layout="wide")
st.title("📊 OLA Insights Dashboard")

# --- MySQL Connection ---
def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Sathish123",  # My password
        database="ola_db"
    )

def run_query(query):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(query)
    cols = [i[0] for i in cursor.description]
    rows = cursor.fetchall()
    conn.close()
    return pd.DataFrame(rows, columns=cols)

# --- Query Options ---
query_options = {
    "1. Retrieve all successful bookings": {
        "sql": "SELECT * FROM rides WHERE booking_status = 'Success';",
        "visual": "table"
    },
    "2. Average ride distance for each vehicle type": {
        "sql": """
            SELECT vehicle_type, 
                   ROUND(AVG(ride_distance), 2) AS avg_distance_km
            FROM rides
            GROUP BY vehicle_type
            ORDER BY avg_distance_km DESC;
        """,
        "visual": "bar",
        "x": "vehicle_type",
        "y": "avg_distance_km"
    },
    "3. Total cancelled rides by customers": {
        "sql": """
            SELECT booking_status, COUNT(*) AS total
            FROM rides
            WHERE booking_status = 'Canceled by Customer'
            GROUP BY booking_status;
        """,
        "visual": "bar",
        "x": "booking_status",
        "y": "total"
    },
    "4. Top 5 customers by total rides": {
        "sql": """
            SELECT customer_id, COUNT(*) AS total_rides
            FROM rides
            GROUP BY customer_id
            ORDER BY total_rides DESC
            LIMIT 5;
        """,
        "visual": "bar",
        "x": "customer_id",
        "y": "total_rides"
    },
    "5. Driver cancellations (reasons)": {
        "sql": """
            SELECT canceled_rides_by_driver, COUNT(*) AS total_cancellations
            FROM rides
            WHERE booking_status = 'Canceled by Driver'
            AND canceled_rides_by_driver IS NOT NULL
            GROUP BY canceled_rides_by_driver;
        """,
        "visual": "pie",
        "label": "canceled_rides_by_driver",
        "value": "total_cancellations"
    },
    "6. Max/Min driver ratings for Prime Sedan": {
        "sql": """
            SELECT MAX(driver_ratings) AS max_rating,
                   MIN(driver_ratings) AS min_rating
            FROM rides
            WHERE vehicle_type = 'Prime Sedan';
        """,
        "visual": "table"
    },
    "7. Rides paid via UPI": {
        "sql": "SELECT * FROM rides WHERE payment_method = 'UPI';",
        "visual": "table"
    },
    "8. Avg customer rating per vehicle type": {
        "sql": """
            SELECT vehicle_type, 
                ROUND(AVG(customer_rating), 2) AS avg_customer_rating
            FROM rides
            GROUP BY vehicle_type
            ORDER BY avg_customer_rating DESC;
        """,
        "visual": "hbar",
        "x": "avg_customer_rating",
        "y": "vehicle_type"
    },
    "9. Total booking value of successful rides": {
        "sql": """
            SELECT ROUND(SUM(booking_value), 2) AS total_success_revenue
            FROM rides
            WHERE booking_status = 'Success';
        """,
        "visual": "table"
    },
    "10. Incomplete rides with reason": {
        "sql": """
            SELECT booking_id, customer_id, vehicle_type, 
                   booking_status, incomplete_rides_reason
            FROM rides
            WHERE incomplete_rides = 'Yes';
        """,
        "visual": "table"
    }
}

# --- Sidebar Filter ---
st.sidebar.header("🔍 Select Query")
selected = st.sidebar.selectbox("Choose a query", list(query_options.keys()))

# --- Query Execution ---
query_data = run_query(query_options[selected]["sql"])
st.subheader("📋 Query Result")
st.dataframe(query_data)

# --- Visualization ---
vis_type = query_options[selected]["visual"]
st.subheader("📊 Visualization")

if vis_type == "bar":
    x = query_options[selected]["x"]
    y = query_options[selected]["y"]
    fig, ax = plt.subplots(figsize=(8, 4))
    sns.barplot(data=query_data, x=x, y=y, palette='Blues_d')
    plt.xticks(rotation=30)
    st.pyplot(fig)

elif vis_type == "hbar":
    x = query_options[selected]["x"]
    y = query_options[selected]["y"]
    fig, ax = plt.subplots(figsize=(8, 4))
    sns.barplot(data=query_data, x=x, y=y, palette='Greens_d', orient='h')
    st.pyplot(fig)

elif vis_type == "pie":
    label_col = query_options[selected]["label"]
    value_col = query_options[selected]["value"]
    fig, ax = plt.subplots()
    ax.pie(query_data[value_col], labels=query_data[label_col], autopct="%1.1f%%", startangle=90)
    ax.axis("equal")
    st.pyplot(fig)

elif vis_type == "table":
    st.info("Table view only — no chart needed for this query.")
