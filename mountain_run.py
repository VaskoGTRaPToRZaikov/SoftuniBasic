import math

FIFTY_METERS_DELAY = 30

record_seconds = float(input())
distance_meters = float(input())
time_per_meter = float(input())

delays = math.floor(distance_meters / 50)
delay_time = delays * FIFTY_METERS_DELAY

georgi_time = distance_meters * time_per_meter

overall_georgi_time = georgi_time + delay_time

if overall_georgi_time < record_seconds:
    print(f"Yes! The new record is {overall_georgi_time:.2f} seconds.")
else:
    print(f"No! He was {overall_georgi_time - record_seconds:.2f} seconds slower.")