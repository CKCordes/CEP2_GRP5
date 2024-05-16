# Kitchen Guard Project

**Introduction:**

Kitchen Guard is a distributed system aimed at enhancing kitchen safety, particularly for individuals facing cognitive challenges. The project addresses the problem of unattended stoves, which can pose significant risks in households. By designing, implementing, and testing a distributed kitchen guard system, we aim to create a safer kitchen environment.

**Key Objectives:**

1. Detect when a user leaves the stove unattended for more than 20 minutes and automatically cut power, with reminders provided to the user.
2. Cancel alerts immediately upon the user's return to the kitchen.
3. Support user presence detection in multiple rooms, with localized reminders available in those areas.
4. Report all events, including cooking operations and user absences, to a distributed monitoring server and database.
5. Develop a distributed user interface server and client for accessing monitoring data via PC, tablet, web, or smartphone.
6. Utilize movement sensors (PIR) and power plug control units for detection and reminders, with support provided for Zigbee-based sensors and Python code for Raspberry Pi.
7. Implement support for MQTT protocol with JSON encoding, following HEUCOD recommendations.

**Platform and Technologies:**

- Sensors: Zigbee-based sensors
- Controller: Python application to run on Raspberry Pi
- Server: Python Django
- Communication Protocol
  - Sensors <--> Controller : MQTT with JSON encoding.
  - Controller <--> Server : HTTP
