from ..models import Event, Sensor, Patient
import datetime

def getCookingEvents(cookingEvents):
    cooking = False
    curr_event = Event()
    events = []
    for event in cookingEvents:
        # If resident isn't cooking but have turned the stove on
        if not cooking and event.description == "{state:ON}":
            cooking = True
            curr_event = event
            continue
        
        # If resident IS cooking and stove is turned off. 
        if cooking and event.description == "{state:OFF}":
            cooking = False
            curr_event.end_time = event.start_time
            curr_event.length = curr_event.end_time - curr_event.start_time

            events.append(curr_event)        
        
    return events

def getTrackingEvents(trackingEvents):
    rooms = {}
    curr_events = {}
    curr_event = Event()
    
    events = []
    
    for event in trackingEvents:
        if not rooms.get(event.sensor.sensor_location) and event.description == "{Occupied:True}":
            rooms[event.sensor.sensor_location] = True           
            curr_events[event.sensor.sensor_location] = event
            continue
        
        if rooms.get(event.sensor.sensor_location) and event.description == "{Occupied:False}":
            rooms[event.sensor.sensor_location] = False
            if event.sensor.sensor_location in curr_events:
                curr_event = curr_events[event.sensor.sensor_location]
                curr_event.end_time = event.start_time
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

def eventsOverlaps(cEvent, tEvent):
    return ((cEvent.start_time < tEvent.start_time and cEvent.end_time > tEvent.start_time) or
            (cEvent.start_time > tEvent.start_time and cEvent.start_time < tEvent.end_time))
        

def serializeData(events):
    arr = [{'event_id': event.event_id, 
            'sensor': event.sensor.sensor_id,
            'patient': event.patient.patient_id,
            'event_type': event.event_type,
            'timestamp': epochToDateTime(event.timestamp),
            'start_time': epochToDateTime(event.start_time),
            'end_time': epochToDateTime(event.end_time),
            'length':event.length / 3600, # second / 3600 seconds pr hour = hours
            } for event in events]
    return arr
    
    