# Kitchen Guard Server side

## Prerequisite
This project has multiple external dependencies, which are needed for the system to run. 
- Django Framework
- datetime library
- json library

## Run server locally 
By default the server will run on port 8000 on 127.0.0.1
The server can be started by navigating to the directory containing the `manage.py file`. 


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


## Run the server locally 
