import streamlit as st
import pandas as pd
import mysql.connector

# MySQL connection setup
connection = mysql.connector.connect(
    username = "xxx", #give your username
    password = "xxx", #give your password
    database = "xxx", #give database name which you want to use
    database="MAE3"
)
cursor = connection.cursor()

st.set_page_config(layout="wide", page_title="🚖 Ola Ride Insights Dashboard")
st.title("🚖 Ola Ride Insights Dashboard")

#st.sidebar.header("🔍 Filters (Only Applied on Few Views)")
#status_filter = st.sidebar.selectbox("Select Booking Status", ["Success", "Cancelled", "Incomplete"], index=0)
#payment_filter = st.sidebar.selectbox("Select Payment Method", ["All", "UPI", "Cash", "Wallet"], index=0)

# 1. Successful Bookings
with st.expander("1️⃣ Successful Bookings"):
    cursor.execute("SELECT * FROM ola WHERE Booking_Status = 'Success';")
    result = cursor.fetchall()
    columns = [i[0] for i in cursor.description]
    st.dataframe(pd.DataFrame(result, columns=columns))

# 2. Average Ride Distance by Vehicle Type
with st.expander("2️⃣ Average Ride Distance by Vehicle Type"):
    cursor.execute("""
        SELECT Vehicle_Type, AVG(Ride_Distance) AS average_ride_distance 
        FROM ola 
        GROUP BY Vehicle_Type;
    """)
    result = cursor.fetchall()
    st.dataframe(pd.DataFrame(result, columns=["Vehicle_Type", "Average_Ride_Distance"]))

# 3. Total Cancelled Rides by Customer
with st.expander("3️⃣ Total Cancelled Rides by Customers"):
    cursor.execute("SELECT COUNT(Canceled_Rides_by_Customer) FROM ola;")
    result = cursor.fetchone()[0]
    st.metric("Total Rides Cancelled by Customer", result)

# 4. Top 5 Customers by Booking Count
with st.expander("4️⃣ Top 5 Customers by Bookings"):
    cursor.execute("""
        SELECT Customer_ID, COUNT(Booking_ID) AS Total_Booking 
        FROM ola 
        GROUP BY Customer_ID 
        ORDER BY Total_Booking DESC 
        LIMIT 5;
    """)
    result = cursor.fetchall()
    st.dataframe(pd.DataFrame(result, columns=["Customer_ID", "Total_Booking"]))

# 5. Driver Cancellations for Personal/Car Issues
with st.expander("5️⃣ Driver Cancellations (Personal/Car Issues)"):
    cursor.execute("""
        SELECT COUNT(Canceled_Rides_by_Driver) 
        FROM ola 
        WHERE Canceled_Rides_by_Driver = 'Personal & Car related issue';
    """)
    result = cursor.fetchone()[0]
    st.metric("Driver Cancellations (Personal/Car Issues)", result)

# 6. Driver Rating Stats for Prime Sedan
with st.expander("6️⃣ Driver Ratings for Prime Sedan"):
    cursor.execute("""
        SELECT MAX(Driver_Ratings), MIN(Driver_Ratings) 
        FROM ola 
        WHERE Vehicle_Type = 'Prime Sedan';
    """)
    max_rating, min_rating = cursor.fetchone()
    st.metric("Max Rating", max_rating)
    st.metric("Min Rating", min_rating)

# 7. UPI Payment Ride Details
with st.expander("7️⃣ Rides Paid via UPI"):
    query = """
        SELECT Booking_ID, Customer_ID, Pickup_Location, Drop_Location, Date, Time, 
               Booking_Value, Ride_Distance, Payment_Method 
        FROM ola 
        WHERE Payment_Method = 'UPI';
    """
    cursor.execute(query)
    result = cursor.fetchall()
    cols = [i[0] for i in cursor.description]
    st.dataframe(pd.DataFrame(result, columns=cols))

# 8. Average Customer Rating by Vehicle Type
with st.expander("8️⃣ Avg Customer Rating by Vehicle Type"):
    cursor.execute("""
        SELECT Vehicle_Type, AVG(Customer_Rating) AS Average_Customer_Rating 
        FROM ola 
        GROUP BY Vehicle_Type;
    """)
    result = cursor.fetchall()
    st.dataframe(pd.DataFrame(result, columns=["Vehicle_Type", "Average_Customer_Rating"]))

# 9. Total Booking Value for Successful Rides
with st.expander("9️⃣ Total Booking Value (Success Only)"):
    cursor.execute("""
        SELECT SUM(Booking_Value) 
        FROM ola 
        WHERE Booking_Status = 'Success';
    """)
    total_value = cursor.fetchone()[0]
    st.metric("Total Booking Value", f"₹{total_value:,.2f}")

# 10. Incomplete Rides and Reasons
with st.expander("🔟 Incomplete Rides and Reasons"):
    cursor.execute("""
        SELECT Booking_ID, Customer_ID, Vehicle_Type, Pickup_Location, Drop_Location, 
               Incomplete_Rides, Incomplete_Rides_Reason 
        FROM ola 
        WHERE Incomplete_Rides = 'Yes';
    """)
    result = cursor.fetchall()
    columns = [i[0] for i in cursor.description]
    st.dataframe(pd.DataFrame(result, columns=columns))

# Close DB connection
cursor.close()
connection.close()
