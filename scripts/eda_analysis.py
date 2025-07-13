# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set seaborn style for better visuals
sns.set(style='whitegrid')

# Load the cleaned dataset (adjust path if needed)
df = pd.read_csv('../data/ola_cleaned.csv', parse_dates=['datetime'])

# -------------------------------
# 1. Ride Volume Over Time (Line Chart)
# -------------------------------
rides_per_day = df.groupby(df['datetime'].dt.date).size()

plt.figure(figsize=(12, 5))
rides_per_day.plot(kind='line', marker='o', color='dodgerblue')
plt.title("Ride Volume Over Time")
plt.xlabel("Date")
plt.ylabel("Number of Rides")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("../docs/eda_ride_volume_over_time.png")  # Optional: save as image
plt.show()

# -------------------------------
# 2. Booking Status Breakdown (Bar Chart)
# -------------------------------
plt.figure(figsize=(6, 4))
sns.countplot(data=df, x='booking_status', order=df['booking_status'].value_counts().index, palette='Set2')
plt.title("Booking Status Breakdown")
plt.xticks(rotation=15)
plt.tight_layout()
plt.savefig("../docs/eda_booking_status.png")
plt.show()

# -------------------------------
# 3. Average Ride Distance by Vehicle Type (Bar Chart)
# -------------------------------
avg_distance = df.groupby('vehicle_type')['ride_distance'].mean().sort_values(ascending=False)

plt.figure(figsize=(6, 4))
avg_distance.plot(kind='bar', color='orange')
plt.title("Average Ride Distance per Vehicle Type")
plt.ylabel("Avg. Distance (km)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("../docs/eda_avg_distance_vehicle.png")
plt.show()

# -------------------------------
# 4. Ratings Distribution (Boxplots)
# -------------------------------

# Driver Ratings
plt.figure(figsize=(6, 4))
sns.boxplot(data=df, y='driver_ratings')
plt.title("Driver Ratings Distribution")
plt.tight_layout()
plt.savefig("../docs/eda_driver_ratings.png")
plt.show()

# Customer Ratings
plt.figure(figsize=(6, 4))
sns.boxplot(data=df, y='customer_rating')
plt.title("Customer Ratings Distribution")
plt.tight_layout()
plt.savefig("../docs/eda_customer_ratings.png")
plt.show()

# -------------------------------
# 5. Revenue by Payment Method (Bar Chart)
# -------------------------------
if 'payment_method' in df.columns:
    revenue_by_payment = df.groupby('payment_method')['booking_value'].sum().sort_values(ascending=False)

    plt.figure(figsize=(7, 4))
    revenue_by_payment.plot(kind='bar', color='seagreen')
    plt.title("Total Revenue by Payment Method")
    plt.ylabel("Booking Value")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("../docs/eda_revenue_by_payment.png")
    plt.show()

# -------------------------------
# 6. Ride Distance Distribution (Histogram)
# -------------------------------
plt.figure(figsize=(6, 4))
sns.histplot(df['ride_distance'], bins=20, kde=True, color='teal')
plt.title("Ride Distance Distribution")
plt.xlabel("Distance (km)")
plt.tight_layout()
plt.savefig("../docs/eda_ride_distance_dist.png")
plt.show()

# -------------------------------
# 7. Day-wise Ride Frequency (Bar Chart)
# -------------------------------
plt.figure(figsize=(6, 4))
sns.countplot(data=df, x='day', order=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"], palette='coolwarm')
plt.title("Rides by Day of Week")
plt.xticks(rotation=15)
plt.tight_layout()
plt.savefig("../docs/eda_daywise_rides.png")
plt.show()
