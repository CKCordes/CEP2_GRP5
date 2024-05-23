# Kitchen Guard Application

The Kitchen Guard Application, is meant to run on a Raspberry-Pi and serve to run as the controller for the Kitchen Guard System.

The application consists of a HomeHelper Library, which is a library that provides the necessary abstractions for the application to interact with the Zigbee2Mosquitto Interface, the Mosquitto Broker, and the Database Server.

The application also consists of a KitchenGuardApp, which is the main application that runs the Kitchen Guard System.

See the __main__.py file in the App directory for the entry point of the application, and to see how the application is configured.

## Run the app

Prerequisites:

- Have Mosquitto Broker running on Raspberry pi. The app assumes that the broker is running locally on port 1883.
- Have Zigbee2Mosquitto antenna live and have sensors and actuators connected to the Zigbee2Mosquitto Interface
- For saving of event to database, have the database server running. Have the endpoint for the database server configured in the WebClient.
- Have your system configured in "\__main__.py", with correct friendly names for the sensors and actuators, and the correct topics for the sensors and actuators.

Be in the root directory CEP2_GRP5:

To start the application, run:

```shell
> python -m App
```

That will start execution on App/\__main__.py
