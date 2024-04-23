import sqlite3
import socket
from ..models import Event, Sensor, Patient


def updatedb(data):
    # EXCEPTION HANDLING
    try:
       connection = sqlite3.connect("../../db.sqlite3")
    except:
        print("Error conencting to the database")
        return
        
    # Checks for an event already existing
    if Event.objects.filter(event_id=data["event_id"]).exists():
        return
    
        # Checks if patient already exists    
    if Patient.objects.filter(patient_id=data["patient_id"]).exists():
        patient = Patient.objects.get(patient_id=data["patient_id"]) # Creates an instance of a patient matching the given id. 
    else:
        # Creates a new instance of the patient
        patient = Patient(patient_id = data["patient_id"], 
                          caregiver_id = data["caregiver_id"],
                          monitor_id = data["monitor_id"],
                          location = data["location"],
                          street_address = data["street_address"],
                          city = data["city"],
                          postal_code = data["postal_code"],
                          site = data["site"])
        patient.save()
    
    # Checks if sensor already exists
    if Sensor.objects.filter(sensor_id=data["sensor_id"]):
        sensor = Sensor.objects.get(sensor_id=data["sensor_id"]) # Creates an instance of the sensor matching the id
    else:
        # The sensor is new and a new instance of the sensor is registered.
        sensor = Sensor(sensor_id = data["sensor_id"],
                        sensor_type = data["sensor_type"],
                        sensor_location = data["sensor_location"],
                        device_model = data["device_model"],
                        device_vendor = data["device_vendor"],
                        accuracy = data["accuracy"],
                        sensor_blind_duration = data["sensor_blind_duration"])
        sensor.save()
        
    # Creates the new event and logs it
    newEvent = Event(event_id = data["event_id"],
                     sensor = sensor,
                     patient = patient,
                     event_type = data["event_type"],
                     event_type_enum = data["event_type_enum"],
                     description = data["description"],
                     advanced = data["advanced"],
                     timestamp = data["timestamp"],
                     start_time = data["start_time"],
                     end_time = data["end_time"],
                     length = data["length"],
                     value = data["value"],
                     unit = data["unit"])

    
    newEvent.save()
    
    ##
      
    """       
     HER   
    cursor = connection.cursor()

    #patient = data["patient_id"]
    #patient_id = cursor.execute(f"SELECT id FROM KitchenGuardServer_patient WHERE patient_id={patient}")

    #sensor = data["sensor_id"]
    #sensor_id = cursor.execute(f"SELECT id FROM KitchenGuardServer_sensor WHERE sensor_id={sensor}")
    print("FØR pik og patter")
    cursor.execute("SELECT * FROM KitchenGuardServer_event")
    print(cursor.fetchall())
    print("Mellem pik og patter")
    cursor.execute("INSERT INTO KitchenGuardServer_event(event_id, sensor_id, patient_id, event_type, event_type_enum, description, advanced, timestamp, start_time, end_time, length, value, unit) VALUES ('s', 1, 1, 'sads', 1, 'hej', 'advanced', 1000, 1000, 100000, 10000000, 'sad', 'rqsd');")
    print("PIK OG PATTER")
    connection.commit()

    connection.close()
    
    TIL HER
    """
    """
    cursor.execute(f'''INSERT INTO KitchenGuardServer_event(event_id, sensor_id, patient_id, event_type, event_type_enum, description, advanced, timestamp, start_time, end_time, length, value, unit) 
                   VALUES ({data["event_id"]}, {sensor_id}, {patient_id}, {data["event_type"]}, 
                   {data["event_type_enum"]}, {data["description"]}, {data["advanced"]}, {data["timestamp"]}, 
                   {data["start_time"]}, {data["end_time"]}, {data["length"]}, {data["value"]}, {data["unit"]})''')
    """
    

