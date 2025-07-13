-- 1. Successful bookings
SELECT *
FROM rides
WHERE booking_status = 'Success';

-- 2. Average ride distance by vehicle type
SELECT vehicle_type, 
       ROUND(AVG(ride_distance), 2) AS avg_distance_km
FROM rides
GROUP BY vehicle_type
ORDER BY avg_distance_km DESC;

-- 3. Total cancelled rides by customers
SELECT COUNT(*) AS customer_cancelled_rides
FROM rides
WHERE booking_status = 'Cancelled by Customer';

-- 4. Top 5 customers by number of rides
SELECT customer_id, COUNT(*) AS total_rides
FROM rides
GROUP BY customer_id
ORDER BY total_rides DESC
LIMIT 5;

-- 5. Rides cancelled by driver - reasons
SELECT canceled_rides_by_driver, COUNT(*) AS total_cancellations
FROM rides
WHERE booking_status = 'Cancelled by Driver'
  AND canceled_rides_by_driver IS NOT NULL
GROUP BY canceled_rides_by_driver;
