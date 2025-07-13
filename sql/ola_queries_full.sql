-- Query 1: Retrieve all successful bookings
SELECT * FROM rides WHERE booking_status = 'Success';

-- Query 2: Average ride distance for each vehicle type
SELECT vehicle_type, ROUND(AVG(ride_distance), 2) AS avg_distance_km
FROM rides GROUP BY vehicle_type ORDER BY avg_distance_km DESC;

-- Query 3: Total number of cancelled rides by customers
SELECT COUNT(*) AS customer_cancelled_rides
FROM rides WHERE booking_status = 'Cancelled by Customer';

-- Query 4: Top 5 customers who booked the highest number of rides
SELECT customer_id, COUNT(*) AS total_rides
FROM rides GROUP BY customer_id ORDER BY total_rides DESC LIMIT 5;

-- Query 5: Rides cancelled by drivers due to personal and car-related issues
SELECT canceled_rides_by_driver, COUNT(*) AS total_cancellations
FROM rides WHERE booking_status = 'Cancelled by Driver'
AND canceled_rides_by_driver IS NOT NULL
GROUP BY canceled_rides_by_driver;

-- Query 6: Max and Min driver ratings for Prime Sedan bookings
SELECT MAX(driver_ratings) AS max_rating, MIN(driver_ratings) AS min_rating
FROM rides WHERE vehicle_type = 'Prime Sedan';

-- Query 7: Retrieve all rides where payment was made using UPI
SELECT * FROM rides WHERE payment_method = 'UPI';

-- Query 8: Average customer rating per vehicle type
SELECT vehicle_type, ROUND(AVG(customer_rating), 2) AS avg_customer_rating
FROM rides GROUP BY vehicle_type ORDER BY avg_customer_rating DESC;

-- Query 9: Total booking value of rides completed successfully
SELECT ROUND(SUM(booking_value), 2) AS total_success_revenue
FROM rides WHERE booking_status = 'Success';

-- Query 10: List all incomplete rides along with the reason
SELECT booking_id, customer_id, vehicle_type, booking_status, incomplete_rides_reason
FROM rides WHERE incomplete_rides = 'Yes';
