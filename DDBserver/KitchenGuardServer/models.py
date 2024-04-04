from django.db import models

# This is the sensor information
class Sensor(models.Model):
    def __str__(self):
        return self.sensor_id + ", " + self.sensor_type
    sensor_id = models.CharField(max_length=200)
    sensor_type = models.CharField(max_length=200)
    sensor_location = models.CharField(max_length=200) # Room
    device_model = models.CharField(max_length=200)
    device_vendor = models.CharField(max_length=200)
    accuracy = models.IntegerField(default=-1) # self reported accuracy
    sensor_blind_duration = models.IntegerField(default=-1) # Måske skal den fjernes?

class Patient(models.Model):
    def __str__(self):
        return self.patient_id + ", " + self.location
    patient_id = models.CharField(max_length=200)
    caregiver_id = models.IntegerField(default=-1)
    monitor_id = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    street_address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    postal_code = models.CharField(max_length=200)
    site = models.CharField(max_length=200)    

class Event(models.Model):
    def __str__(self):
        return self.event_id + "," + self.description
    event_id = models.CharField(max_length=200)
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    event_type = models.CharField(max_length=200)
    event_type_enum = models.IntegerField(default=-1)
    description = models.CharField(max_length=200)
    advanced = models.CharField(max_length=200)
    timestamp = models.IntegerField(default=-1)
    start_time = models.IntegerField(default=-1)
    end_time = models.IntegerField(default=-1)
    length = models.IntegerField(default=-1)

    value = models.CharField(max_length=200)
    unit = models.CharField(max_length=200)
    # Eventuel tilføj flere values