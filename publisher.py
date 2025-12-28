# Home Assistant MQTT Live Publisher
# Student: Karthika Ramasamy Senthilkumar

import paho.mqtt.client as mqtt
import time
import random
import json
import logging 


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


student_name = "Karthika Ramasamy Senthilkumar" 
unique_id = "42130220" 
topic = "home/karthika-2025/sensor" 



broker = "192.168.29.188"
port = 1883
username = "final_fix_user"
password = "mqtt1111"


client = mqtt.Client()
client.username_pw_set(username, password)

try:
   
    client.connect(broker, port) 
    
    logging.info(f"Connected to {broker}:{port} and publishing live sensor data...")

    soil_moisture = 400

    while True:
        # Simulate sensor readings
        temperature = 25 + random.uniform(-1, 1)
        humidity = 60 + random.uniform(-2, 2)
        soil_moisture += random.randint(-5, 5)
        soil_moisture = max(300, min(700, soil_moisture))

        # Prepare payload as JSON.
        payload = {
            "temperature": round(temperature, 1),
            "humidity": round(humidity, 1),
            "soil_moisture": soil_moisture # Your extra sensor
        }

        # Publish to MQTT with RETAIN=True
        client.publish(topic, json.dumps(payload), retain=True)
        logging.info("Published: %s", payload) 

        time.sleep(5)

# --- Exception Handling ---
except ConnectionRefusedError:
   
    logging.error(f"Could not connect to MQTT broker at {broker}:{port}. Check if Mosquitto is running or firewall is blocking the connection.")
except Exception as e:
   
    logging.error(f"An unexpected error occurred: {e}")
except KeyboardInterrupt:
    client.disconnect()
   
    logging.info("Disconnected from MQTT broker.")
