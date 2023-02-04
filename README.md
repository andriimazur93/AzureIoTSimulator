IoT sensor emulator

## Overview

This project is a minimalistic emulator if an IoT devile, simulating stream of data sent to Azure IoT Hub. It's useful when testing streaming jobs. Based on the Azure Raspberry Pi IoT Simulator [Online Simulator](https://azure-samples.github.io/raspberry-pi-web-simulator/#GetStarted).

## Prerequisites

- Docker

## Usage
### Set the environment variables
- SLEEP_INTERVAL_SECONDS: This environment variable specifies the number of seconds the application should wait before sending the next message.

- MESSAGE_COUNT: This environment variable specifies the total number of messages that the application should send.

- AZURE_CONN_STRING: This environment variable is the connection string that the application uses to connect to Azure IoT Hub. The connection string should be set to the values for your IoT hub.

### Building the Docker Image
Run the following command to build the Docker image:
```
docker build -t azure-iot-smart-home .
```
### Running the Application
Run the following command to start the application
```
docker run azure-iot-smart-home
```

## Message format
The messages sent by this program have the following format:
```
{
  "id": "unique-id",
  "timestamp": "YYYY-MM-DDTHH:MM:SS",
  "temperature": temperature-value,
  "humidity": humidity-value
}
```
where:
- id: A unique identifier for the message.
- timestamp: The current date and time in the format YYYY-MM-DDTHH:MM:SS.
- temperature: A random value between -40 and 40.
- humidity: A random value between 1 and 99.

## Check received messages in Azure Portal
In order to see your messages in Azure portal, open Azure CLI and run following commands

1. Add the Azure IoT extension to the Azure CLI. The Azure IoT extension provides a set of commands for managing Azure IoT Hubs, devices, and solutions.
```
az extension add --name azure-iot`
```

2. Monitor events on an Azure IoT Hub with the specified name.
```
az iot hub monitor-events --hub-name <youriothubname>
```