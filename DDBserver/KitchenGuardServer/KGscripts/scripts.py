from ..models import Event, Sensor, Patient
import datetime
import json

def getCookingEvents(cookingEvents):
    cooking = False
    curr_event = Event()
    events = []
    
    for event in cookingEvents:
       
        desc = json.loads(event.description.replace("'", "\""))
        if not 'power' in desc:
            continue
                
        
        # If resident isn't cooking but have turned the stove on. Power > 3 is equal to 'state': 'ON'
        if not cooking and desc["power"] > 3:
            cooking = True
            curr_event = event
            curr_event.start_time = event.timestamp
            continue
        
        # If resident IS cooking and stove is turned off. Power < 3 is equal to 'state': 'OFF'
        if cooking and desc["power"] < 3:
            cooking = False
            curr_event.end_time = event.timestamp
            curr_event.length = curr_event.end_time - curr_event.start_time
            events.append(curr_event)        
        
    return events

def getTrackingEvents(trackingEvents):
    rooms = {}
    curr_events = {}
    curr_event = Event()
    
    events = []
    

    for event in trackingEvents:
        
        try:
            cleanedDesc = event.description.replace("'", '"').replace("False", "false").replace("True", "true")
            desc = json.loads(cleanedDesc)
        except json.JSONDecodeError:
            print("Invalid JSON in description:", event.description)
        
        
        
        
        if not rooms.get(event.sensor.sensor_location) and desc["occupancy"]:
            rooms[event.sensor.sensor_location] = True           
            curr_events[event.sensor.sensor_location] = event
            curr_events[event.sensor.sensor_location].start_time = event.timestamp          
            continue
        
        if rooms.get(event.sensor.sensor_location) and not desc["occupancy"]:
            rooms[event.sensor.sensor_location] = False
            if event.sensor.sensor_location in curr_events:
                curr_event = curr_events[event.sensor.sensor_location]
                curr_event.end_time = event.timestamp
                curr_event.length = curr_event.end_time - curr_event.start_time
                events.append(curr_event)
               
    return events
    
def epochToDateTime(epoch_timestamp):
    if epoch_timestamp == -1:
        return -1
    dt_object = datetime.datetime.fromtimestamp(epoch_timestamp)
    # Convert datetime object to a formatted string
    return str(dt_object.strftime('%Y-%m-%d %H:%M:%S'))

def getOverlapingEvents(cookingEvents, trackingEvents):
    overlappingEvents = []
    for cEvent in cookingEvents:
        for tEvent in trackingEvents:
            if eventsOverlaps(cEvent, tEvent):
                    overlappingEvents.append(tEvent)
    
    
    
    return overlappingEvents

def forcedshut(event, events):
    val = ""
    for tEvent in events:
        if eventsOverlaps(event, tEvent) and event.event_type_enum == 82136 and tEvent.event_type_enum == 82099:
            if (event.end_time - tEvent.end_time >= 60 and tEvent.sensor.sensor_location == "kitchen"):
                val = "true"
                return val
            else: val = "false"
    return val
    
                
def eventsOverlaps(cEvent, tEvent):
    return ((cEvent.start_time < tEvent.start_time and cEvent.end_time > tEvent.start_time) or
            (cEvent.start_time > tEvent.start_time and cEvent.start_time < tEvent.end_time))

def serializeData(events):
    arr = [{'patient': event.patient.patient_id,
            'sensor': event.sensor.sensor_id,
            'location': event.sensor.sensor_location,
            'event_type': event.event_type,
            'timestamp': epochToDateTime(event.timestamp),
            'start_time': epochToDateTime(event.start_time),
            'end_time': epochToDateTime(event.end_time),
            'length': round(event.length / 60, 2), # second / 60 seconds pr minute = minutes
            'forced_shutdown': str(forcedshut(event, events)),
            'event_id': event.event_id, 
            } for event in events]
    
    return arr
    
