from datetime import datetime, timedelta
import time

def convert_time(utc_time):
    # Define the time zone offsets
    utc_offset = timedelta(hours=8)  # UTC+8 offset
    gmt_offset = timedelta(hours=8)  # GMT+8 offset

    # Convert the UTC time to datetime object
    utc_datetime = datetime.strptime(utc_time, "%Y-%m-%d %H:%M:%S")
    
    # Apply the UTC+8 offset
    utc_plus8 = utc_datetime + utc_offset
    
    # Convert to GMT+8 time
    gmt_plus8 = utc_plus8 - gmt_offset
    
    # Format the time in 12-hour format
    gmt_plus8_12h = gmt_plus8.strftime("%Y-%m-%d %I:%M:%S %p")
    
    return gmt_plus8_12h

# Example usage
while True:
    utc_time = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
    gmt_plus8_12h = convert_time(utc_time)
    print("\rGMT+8 Time (12-hour format):", gmt_plus8_12h, end="", flush=True)
    time.sleep(1)  # Delay for 1 second before updating again
