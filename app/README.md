# Kitchen Guard Application

The Kitchen Guard Application, is meant to run on a Raspberry-pi and server to run as the controller for the Kitchen Guard System.

**To run the app:**

Prerequisites:

- Have Mosquitto Broker running on Raspberry pi. The app assumes that the broker is running locally on port 1883.
- Sensors connected to the broker
- For saving of event to database, have the database server running,
- System configured in __main__.py.

Be in the root directory CEP2_GRP5:
run: python -m App

That will start execution on App/__main__.py
