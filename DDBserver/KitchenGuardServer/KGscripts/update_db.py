from ..models import Event, Sensor, Patient


def updatedb(data):
        
    # Checks for an event already existing
    if Event.objects.filter(event_id=data["id"]).exists():
        print("Event already exists in database")
        return
    
    # Checks if patient already exists    
    if Patient.objects.filter(patient_id=data["patientId"]).exists():
        print("Patient already exists")
        patient = Patient.objects.get(patient_id=data["patientId"]) # Creates an instance of a patient matching the given id. 
    else:
        # Creates a new instance of the patient
        patient = Patient(patient_id = data["patientId"],
                          caregiver_id = data["caregiverId"],
                          monitor_id = data["monitorId"],
                          location = data["location"],
                          street_address = data["streetAdress"],
                          city = data["city"],
                          postal_code = data["postalCode"],
                          site = data["site"])  
        patient.save()

    
    # Checks if sensor already exists
    if Sensor.objects.filter(sensor_id=data["sensorId"]):
        print("Sensor already exists")
        sensor = Sensor.objects.get(sensor_id=data["sensorId"]) # Creates an instance of the sensor matching the id
    else:
        # The sensor is new and a new instance of the sensor is registered.
        sensor = Sensor(sensor_id = data["sensorId"],
                        sensor_type = data["sensorType"],
                        sensor_location = data["sensorLocation"],
                        device_model = data["deviceModel"],
                        device_vendor = data["deviceVendor"],
                        accuracy = data["accuracy"],
                        sensor_blind_duration = data["sensorBlindDuration"])
        sensor.save()
        
    # Creates the new event and logs it
    newEvent = Event(event_id = data["id"],
                     sensor = sensor,
                     patient = patient,
                     event_type = data["eventType"],
                     event_type_enum = data["eventTypeEnum"],
                     description = data["description"],
                     advanced = data["advanced"],
                     timestamp = data["timestamp"],
                     start_time = data["startTime"],
                     end_time = data["endTime"],
                     length = data["length"],
                     value = data["value"],
                     unit = data["unit"])
    newEvent.save()
    

