# Kitchen Guard Server side

## Prerequisite
This project has multiple external dependencies, which are needed for the system to run. Most are installed by default. 
Below are the ones not installed by default. 
- Django Framework

## Run server locally 
By default the server will run on port 8000 on 127.0.0.1
The server can be started by navigating to the directory containing the `manage.py` file. 
In this repository that is `/DDBserver/`.
From here run the following command:
```
python manage.py runserver
```
When the server is running it can be accessed on `127.0.0.1/8000`.

## Directory structure
The directory structure is mainly based on how Django structures its directories. The directory consists of "DDBserver" which is the project directory, "frontend" which handles the frontend template files, and "KitchenGuardServer" which is responsible for handling the database. 
```
DDBserver/
├── DDBserver/
│   ├── ..
│   └── ..
├── frontend/
│   ├── templates/
│   │   ├── login.html
│   │   └── index.html
│   └── ..
└── KitchenGuardServer/
    ├── KGscripts/
    |       |
    │       └── .. 
    └── ..
```

## Database structure
The database is a .sqlite file as this is default for a Django project. 
The database mainly consists of three tables, Event, Sensor, and Patient. 
Each event is coupled to one sensor and one patient through the sensor_id and patient_id. 

```
  Event Table
+-----------+-----------+------------+-----+
| event_id  | sensor_id | patient_id | ... |
+-----------+-----------+------------+-----+
|           |           |            |     |
|           |           |            |     |
+-----------+-----------+------------+-----+

  Sensor Table
+-----------+-----+
| sensor_id | ... |
+-----------+-----+
|           |     |
|           |     |
+-----------+-----+

  Patient Table
+------------+-----+
| patient_id | ... |
+------------+-----+
|            |     |
|            |     |
|            |     |
+------------+-----+

```




