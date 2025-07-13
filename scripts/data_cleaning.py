import pandas as pd

# Step 1: Load the Excel dataset
df = pd.read_excel('../data/OLA_DataSet.xlsx')   # Adjust path if needed
print("Original Data Loaded:")
print(df.head())

# Step 2: Drop unnecessary columns
df.drop(columns=['V_TAT', 'C_TAT', 'Vehicle Images'], inplace=True, errors='ignore')

# Step 3: Handle missing values
df = df.dropna(subset=['Customer_ID'])  # Drop rows missing Customer_ID
df['Driver_Ratings'].fillna(df['Driver_Ratings'].mean(), inplace=True)
df['Customer_Rating'].fillna(df['Customer_Rating'].mean(), inplace=True)

# Step 4: Rename columns
df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]

# Step 5: Fix data types
df['date'] = pd.to_datetime(df['date'], errors='coerce')
df['time'] = pd.to_datetime(df['time'], format='%H:%M:%S', errors='coerce').dt.time
df['datetime'] = pd.to_datetime(df['date'].astype(str) + ' ' + df['time'].astype(str), errors='coerce')
df['hour'] = df['datetime'].dt.hour
df['day'] = df['datetime'].dt.day_name()

df['ride_distance'] = pd.to_numeric(df['ride_distance'], errors='coerce')
df['booking_value'] = pd.to_numeric(df['booking_value'], errors='coerce')
df['booking_status'] = df['booking_status'].astype('category')
df['vehicle_type'] = df['vehicle_type'].astype('category')

# Step 6: Drop duplicates
df.drop_duplicates(inplace=True)

# Step 7: Save cleaned CSV
df.to_csv('../data/ola_cleaned.csv', index=False)
print("Cleaned data saved to ola_cleaned.csv")
