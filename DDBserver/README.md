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
When the server is running it can be accessed on `127.0.0.1:8000`.

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

## Create a superuser
To get a correct set of credentials you'll have to create a Django `superuser`. This is needed as the login checks for a match in the Django superusers when a user tries to login. Alternatively, due to the current low prioritization of security measures, you can bypass the login process by navigating to `127.0.0.1:8000/index`.
### To create a new superuser:
Navigate to the directory containing the `manage.py` file. 
In this repository that is `/DDBserver/`.
From here run the following command:
```
python manage.py createsuperuser
```
Enter your desired username and press enter.
You will then be prompted for your desired email address. This can be ignored by pressing enter. 
The final step is to enter your password. You will be asked to enter your password twice, the second time as a confirmation of the first.

You should now be able to login using your newly created superuser. 




