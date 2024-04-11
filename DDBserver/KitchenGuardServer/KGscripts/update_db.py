import sqlite3
import socket
from ..models import Event, Sensor, Patient


def updatedb(data):
    # EXCEPTION HANDLING
    try:
       connection = sqlite3.connect("../../db.sqlite3")
    except:
        print("Error")
        
    # Checks for an event already existing
    if Event.objects.filter(event_id=data["event_id"]).exists():
        return
    
    ## Indsat af Mads:
    newEvent = Event()
    
    patient = Patient.objects.get(patient_id='Chris') # Creates an instance of a patient matching the given id. 
    sensor = Sensor.objects.get(sensor_id='pikogpatter87') # Creates an instance of the sensor matching the id
    
    newEvent.event_id = data["event_id"]
    newEvent.sensor = sensor 
    newEvent.patient = patient 
    newEvent.event_type = data["event_type"]
    newEvent.event_type_enum = data["event_type_enum"]
    newEvent.description = data["description"]
    newEvent.advanced = data["advanced"]
    newEvent.timestamp = data["timestamp"]
    newEvent.start_time = data["start_time"]
    newEvent.end_time = data["end_time"]
    newEvent.length = data["length"]
    newEvent.value = data["value"]
    newEvent.unit = data["unit"]
    
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
    

