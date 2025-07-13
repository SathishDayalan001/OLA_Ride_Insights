
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# --- Page Setup ---
st.set_page_config(page_title="Dashboard", layout="wide")
st.title("📊 OLA Insights Dashboard (CSV Version)")

# --- Load CSV ---
@st.cache_data
def load_data():
    df = pd.read_csv(r"data/ola_cleaned.csv", parse_dates=["datetime"])
    return df

df_csv = load_data()

# --- Query Options ---
query_options = {
    "1. Retrieve all successful bookings": {
        "data": df_csv[df_csv["booking_status"] == "Success"],
        "visual": "table"
    },
    "2. Average ride distance for each vehicle type": {
        "data": df_csv.groupby("vehicle_type")["ride_distance"].mean().reset_index().sort_values(by="ride_distance", ascending=False).rename(columns={"ride_distance": "avg_distance_km"}),
        "visual": "bar",
        "x": "vehicle_type",
        "y": "avg_distance_km"
    },
    "3. Total cancelled rides by customers": {
        "data": df_csv[df_csv["booking_status"] == "Cancelled by Customer"].groupby("booking_status").size().reset_index(name="total"),
        "visual": "pie",
        "label": "booking_status",
        "value": "total"
    },
    "4. Top 5 customers by total rides": {
        "data": df_csv.groupby("customer_id").size().reset_index(name="total_rides").sort_values(by="total_rides", ascending=False).head(5),
        "visual": "bar",
        "x": "customer_id",
        "y": "total_rides"
    },
    "5. Driver cancellations (reasons)": {
        "data": df_csv[(df_csv["booking_status"] == "Cancelled by Driver") & (df_csv["canceled_rides_by_driver"].notnull())].groupby("canceled_rides_by_driver").size().reset_index(name="total_cancellations"),
        "visual": "pie",
        "label": "canceled_rides_by_driver",
        "value": "total_cancellations"
    },
    "6. Max/Min driver ratings for Prime Sedan": {
        "data": df_csv[df_csv["vehicle_type"] == "Prime Sedan"]["driver_ratings"].agg(["max", "min"]).reset_index().rename(columns={"index": "stat", "driver_ratings": "value"}),
        "visual": "table"
    },
    "7. Rides paid via UPI": {
        "data": df_csv[df_csv["payment_method"] == "UPI"],
        "visual": "table"
    },
    "8. Avg customer rating per vehicle type": {
        "data": df_csv.groupby("vehicle_type")["customer_rating"].mean().reset_index().rename(columns={"customer_rating": "avg_customer_rating"}).sort_values(by="avg_customer_rating", ascending=False),
        "visual": "hbar",
        "x": "avg_customer_rating",
        "y": "vehicle_type"
    },
    "9. Total booking value of successful rides": {
        "data": pd.DataFrame([{"total_success_revenue": df_csv[df_csv["booking_status"] == "Success"]["booking_value"].sum()}]),
        "visual": "table"
    },
    "10. Incomplete rides with reason": {
        "data": df_csv[df_csv["incomplete_rides"] == "Yes"][["booking_id", "customer_id", "vehicle_type", "booking_status", "incomplete_rides_reason"]],
        "visual": "table"
    }
}

# --- Sidebar Filter ---
st.sidebar.header("🔍 Select Query")
selected = st.sidebar.selectbox("Choose a query", list(query_options.keys()))

query_data = query_options[selected]["data"]
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
    st.info("This query only needs a table view.")
