# Dockerized MQTT to FastAPI Bridge

## Overview

This Docker application provides a simple bridge between MQTT (Message Queuing Telemetry Transport) and FastAPI. It allows you to receive MQTT messages and present them through a FastAPI web interface.

## Prerequisites

Before using this application, you should have the following prerequisites installed:

- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)

## Installation and Usage

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/copycat1024/mqtt-fastapi-1.git
   cd mqtt-fastapi-1
   ```

2. Build and run the Docker container:

   ```bash
   docker compose up
   ```

   This command will build the Docker image and start the containers. The MQTT to FastAPI bridge should now be running.

3. Access the FastAPI web interface in your browser:

   - [http://localhost/v1/messages](http://localhost/v1/messages)

   You should see the FastAPI interface where you can view incoming messages.

   - [http://localhost/docs](http://localhost/v1/messages)

   You can also see all available endpoint in the documentation.

## MQTT Messages

When the application is running, it will subscribe to the topic "charger/+/connector/+/session/+". There is also one application that publish a random message to the topic every 10 seconds.
