import requests
import json

# URL to post the JSON data
url = "http://127.0.0.1:8000/KitchenGuardServer/dbupdater"

# Sample JSON data
data = {
    'event_id': 'EV123456789999',
    'sensor': 1, 
    'patient': 1, 
    'event_type': 'Heart Rate',
    'event_type_enum': 1,
    'description': 'Patients heart rate is above normal range.',
    'advanced': 'Advanced monitoring required.',
    'timestamp': 1,
    'start_time': 1,
    'end_time': 1,
    'length': 10, # Length in minutes
    'value': '100',
    'unit': 'bpm',
}

# Convert data to JSON string
json_data = json.dumps(data)

# Set the headers
headers = {'Content-Type': 'application/json'}

try:
    # Send POST request with JSON data
    response = requests.post(url, data=json_data, headers=headers)

    # Check if request was successful (status code 200)
    if response.status_code == 200:
        print("Data posted successfully.")
    else:
        print("Failed to post data. Status code:", response.status_code)
        print(response.text)  # Print response text for debugging
except Exception as e:
    print("An error occurred:", str(e))