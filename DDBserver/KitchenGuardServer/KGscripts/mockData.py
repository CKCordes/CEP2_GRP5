import requests
import time
from heucod import HeucodEvent
import uuid

def heucodCreater(_enum, _desc, _location):
    
    # URL to post the JSON data
    url = "http://127.0.0.1:8000/api/dbupdater"


    # Creating Heucod event
    heucod = HeucodEvent()
    # == Event ==
    heucod.id_ = uuid.uuid4()
    heucod.event_type = "BasicEvent"
    heucod.event_type_enum = _enum # Tracking id: 82099, CookingOperation: 82136
    heucod.description = _desc # Tracking: {Occupied:False}, Cooking: "{State:True}"
    heucod.advanced = "v"
    heucod.timestamp = time.time()
    heucod.start_time = time.time()
    heucod.end_time = -1
    heucod.length = -1
    heucod.sensor_blind_duration = -1
    heucod.value = -1
    heucod.unit = "v"
    heucod.value2 = -1
    heucod.unit2 = ""
    heucod.value3 = -1
    heucod.unit3 = ""
    heucod.direct_event = False
    heucod.sending_delay = -1

    # == Patient ==
    heucod.patient_id = "other_test_patient"
    heucod.caregiver_id = 1
    heucod.monitor_id = 1
    heucod.location = ""
    heucod.street_adress = "hej"
    heucod.city = "Aarhus"
    heucod.postal_code = 8200
    heucod.site = ""
    heucod.room = "" 

    # == Sensor ==
    heucod.sensor_id = _location
    heucod.sensor_type = ""
    heucod.sensor_location = _location
    heucod.sensor_rtc_clock = True
    heucod.device_model = ""
    heucod.device_vendor = ""
    heucod.gateway_id = ""
    heucod.service_id = ""
    heucod.power = 100
    heucod.battery = 100
    heucod.rssi = 1.0
    heucod.measured_power = 1.0
    heucod.signal_to_noise_ratio = 0.5
    heucod.accuracy = 1
    heucod.link_quality = 255

    # Converting to json
    heucod_json = heucod.to_json()

    # Set the headers
    headers = {'Content-Type': 'application/json'}

    try:
        # Send POST request with JSON data
        response = requests.post(url, data=heucod_json, headers=headers)

        # Check if request was successful (status code 200)
        if response.status_code == 200:
            print("Data posted successfully.")
        else:
            print("Failed to post data. Status code:", response.status_code)
            print(response.text)  # Print response text for debugging
    except Exception as e:
        print("An error occurred:", str(e))
        
for i in range(5):
    heucodCreater(82136, "{state:ON}", "kitchen")
    heucodCreater(82136, "{state:ON}", "kitchen")
    time.sleep(2)
    heucodCreater(82099, "{Occupied:True}", "living room")
    time.sleep(2)
    heucodCreater(82099, "{Occupied:True}", "living room")
    heucodCreater(82099, "{Occupied:True}", "living room")
    heucodCreater(82136, "{state:ON}", "kitchen")
    time.sleep(2)
    heucodCreater(82136, "{state:ON}", "kitchen")
    time.sleep(2)
    heucodCreater(82099, "{Occupied:True}", "living room2")
    heucodCreater(82099, "{Occupied:False}", "living room")
    heucodCreater(82099, "{Occupied:True}", "living room2")
    time.sleep(4)
    heucodCreater(82099, "{Occupied:False}", "living room2")
    heucodCreater(82136, "{state:ON}", "kitchen")
    heucodCreater(82136, "{state:OFF}", "kitchen")
    heucodCreater(82136, "{state:ON}", "kitchen")
    time.sleep(3)
    heucodCreater(82136, "{state:OFF}", "kitchen")
    time.sleep(4)
    #def heucodCreater(_enum, _desc, _location):
    # Tracking id: 82099, CookingOperation: 82136
    # Tracking: {Occupied:False}, Cooking: "{State:ON}"