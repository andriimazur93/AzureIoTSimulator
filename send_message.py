import asyncio
import json
import os
import uuid
from datetime import datetime
from random import randint

from azure.iot.device.aio import IoTHubDeviceClient


def build_message():
    message = {
        # unique id
        'id': str(uuid.uuid4()),
        # current timestamp
        'timestamp': datetime.now().strftime('%Y-%m-%dT%H:%M:%S'),
        # random temperature
        'temperature': randint(-40, 40),
        # random humidity
        'humidity': randint(1, 99)
    }
    return message


async def main():
    # Fetch the connection string from an env variable
    conn_str = os.environ['AZURE_CONN_STRING']

    # Fetch the sleep interval from env variable
    sleep_interval = int(os.environ['SLEEP_INTERVAL_SECONDS'])

    message_count = int(os.environ['MESSAGE_COUNT'])

    # Create instance of the device client using the connection string
    device_client = IoTHubDeviceClient.create_from_connection_string(conn_str)

    await device_client.connect()

    for i in range(message_count):

        message = build_message()

        # Send a single message
        print(f"{message['timestamp']}: sending message {message['id']}")
        await device_client.send_message(json.dumps(message))

        await asyncio.sleep(sleep_interval)

    # Finally, shut down the client
    await device_client.shutdown()


if __name__ == "__main__":
    asyncio.run(main())
