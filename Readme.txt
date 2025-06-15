# 🚖 Ola Ride Insights – Data Preprocessing

This repository contains a preprocessing script for the **Ola Ride Insights** project, which prepares the dataset for downstream analytics, dashboarding, and machine learning.

---

## 📁 Dataset

- **File Name:** `OLA_DataSet.xlsx`
- **Location:** `D:\BONEYS\WEB\PYTHON\Project\Ola_Ride_Insights\`
- **Format:** Excel (.xlsx)

The dataset includes ride-level information such as:
- Booking details
- Driver and customer ratings
- Trip distances and values
- Cancellation and payment metadata

---

## 🔧 Features of the Script

### 1. **Load Data**
```python
data = pd.read_excel(path)
Reads the dataset from a local path using pandas.

2. Handle Missing Values
python
Copy
Edit
df = df.bfill()
df = df.ffill()
Performs backward and forward fill to handle missing data.

3. Encode Categorical Variables
Label Encoding for ordinal and ID fields.

One-Hot Encoding for multi-class categorical variables.

python
Copy
Edit
from sklearn.preprocessing import LabelEncoder
4. Remove Outliers
Outliers in the following features are removed based on ±3 standard deviations:

Booking_Value

C_TAT (Customer Turnaround Time)

V_TAT (Vehicle Turnaround Time)

python
Copy
Edit
(df['column_name'] - mean) / std
🧹 Output
Cleaned and encoded DataFrame

Outliers removed based on standard normalization

Ready for use in visualization (Power BI), web apps (Streamlit), or ML models

📦 Dependencies
pandas

scikit-learn

openpyxl (required for reading .xlsx files)

You can install the required packages using:

bash
Copy
Edit
pip install pandas scikit-learn openpyxl
🚀 Usage
python
Copy
Edit
python ola_preprocessing.py
Ensure the path to your Excel file is updated appropriately if you're not using the original directory structure.

📌 Notes
This script is intended for preprocessing only. For visualization or modeling, use the cleaned output df.

# 🛢️ Ola Ride Insights – Storing Data in MySQL

This script is a component of the **Ola Ride Insights** project. It takes a cleaned and processed DataFrame (typically after data preprocessing and feature engineering) and stores it into a structured MySQL table for further querying, analysis, or integration with BI tools like Power BI.

---

## 🔧 What This Script Does

- Connects to a MySQL database.
- Creates a table named `Ola` with predefined schema matching the dataset.
- Iterates through a pandas DataFrame (`df`) and inserts the data into the table.
- Commits the transaction to persist data in the database.

---

## 📋 Table Schema

```sql
CREATE TABLE Ola (
    Date DATE,
    Time TIME,
    Booking_ID VARCHAR(20),
    Booking_Status VARCHAR(500),
    Customer_ID VARCHAR(20),
    Vehicle_Type VARCHAR(20),
    Pickup_Location VARCHAR(50),
    Drop_Location VARCHAR(50),
    C_TAT FLOAT,
    V_TAT FLOAT,
    Canceled_Rides_by_Customer VARCHAR(100),
    Canceled_Rides_by_Driver VARCHAR(100),
    Incomplete_Rides VARCHAR(6),
    Incomplete_Rides_Reason VARCHAR(100),
    Booking_Value INT,
    Payment_Method VARCHAR(20),
    Ride_Distance INT,
    Driver_Ratings FLOAT,
    Customer_Rating FLOAT
);
🧑‍💻 Script Overview
python
Copy
Edit
import mysql.connector
Establishes a connection to the MySQL database using mysql.connector.

python
Copy
Edit
cursor.execute(query1)
Creates the Ola table if it doesn't exist.

python
Copy
Edit
cursor.executemany(query2, data)
Inserts rows from the DataFrame into the MySQL table.

✅ Prerequisites
A running MySQL Server

A database created in advance (replace "xxx" in script)

Install the MySQL connector:

bash
Copy
Edit
pip install mysql-connector-python
🛠️ Configuration
Update the following parameters in the script before running:

python
Copy
Edit
connection = mysql.connector.connect(
    host="localhost",
    username = "your_username",
    password = "your_password",
    database = "your_database"
)
Ensure your DataFrame df contains columns in the same order as defined in the table schema.

🚀 Usage
Preprocess your dataset and assign it to df.

Run this script to create the table and insert data into MySQL.

Use SQL tools or BI software (like Power BI) to query the stored data.


Feel free to try different queries and analyse different results of your choice.

# 🚖 Ola Ride Insights Dashboard (Streamlit + MySQL)

This repository hosts a **Streamlit web application** that connects to a **MySQL database** and displays dynamic analytics on Ola ride-sharing data.

> 🔍 This dashboard helps uncover trends in bookings, cancellations, payments, ride distance, ratings, and more — empowering ride-sharing business insights.

---

## 📊 Features

The dashboard includes **10 interactive sections**, each backed by live SQL queries:

1. ✅ **Successful Bookings** – View all completed rides.
2. 📏 **Average Ride Distance by Vehicle Type** – Insights into trip length per vehicle.
3. ❌ **Total Cancelled Rides by Customers** – Quick cancellation metrics.
4. 🧍‍♂️ **Top 5 Customers by Bookings** – Identify high-value users.
5. 🧰 **Driver Cancellations for Personal/Car Issues** – Tracks reliability issues.
6. ⭐ **Driver Ratings for Prime Sedan** – View min/max driver performance.
7. 💸 **UPI Payment Ride Details** – Analyze cashless transactions.
8. 🧑‍⚖️ **Average Customer Rating by Vehicle Type** – Gauge rider satisfaction by vehicle.
9. 💰 **Total Booking Value (Success Only)** – Revenue-focused KPI.
10. 🛑 **Incomplete Rides and Reasons** – Highlight failed rides and root causes.

---

## 🧠 Technologies Used

- **Streamlit**: For building interactive dashboards
- **MySQL**: Backend database storage
- **Pandas**: Data manipulation and display
- **SQL**: For data retrieval and aggregation

---

## 🛠️ Setup Instructions

### 1. 📦 Install Dependencies

```bash
pip install streamlit pandas mysql-connector-python
2. ⚙️ Configure MySQL
Update the credentials in the script:

python
Copy
Edit
connection = mysql.connector.connect(
    host="localhost",
    user="your_username",
    password="your_password",
    database="your_database"
)
Ensure your MySQL database includes a table named ola with the relevant columns.

3. 🚀 Run the App
bash
Copy
Edit
streamlit run app.py