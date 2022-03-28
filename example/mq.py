import logging
from pydoc import cli
import time

import sys,os
sys.path.append(os.getcwd())

from aqara_iot import AqaraOpenAPI, AqaraOpenMQ, AQARA_LOGGER

from env import ENDPOINT
#, ACCESS_ID, ACCESS_KEY, USERNAME, PASSWORD


# AQARA_LOGGER.setLevel(logging.DEBUG)

# # Init
# openapi = AqaraOpenAPI(ENDPOINT, ACCESS_ID, ACCESS_KEY)
# openapi.connect(USERNAME, PASSWORD, "86", 'aqaraSmart')

# # Receive device message
# def on_message(msg):
#     print("on_message: %s" % msg)

# openapi.token_info.expire_time = 0

def config_mqtt_add():
    return
openmq = AqaraOpenMQ()
openmq.set_get_config(config_mqtt_add)
# openmq.run()
openmq.start()
time.sleep(8)
openmq.stop()
# time.sleep(3)
# openmq.start()



# openmq.add_message_listener(on_message)



# from paho.mqtt import client as mqtt_client
# import time
# import random

# broker = 'broker.emqx.io'
# port = 1883
# topic = "/python/mqtt"
# client_id = f'python-mqtt-{random.randint(0, 1000)}'



# def on_connect(client, userdata, flags, rc):
#     if rc == 0:
#         print("Connected to MQTT Broker!")
#     else:
#         print("Failed to connect, return code %d\n", rc)

# def conn():
#     # Set Connecting Client ID
#     client = mqtt_client.Client("omqt.dcd32f47-8116-4ef6-a8b4-36b46a7f7238")
#     client.on_connect = on_connect
#     client.username_pw_set("948959825666478080da1ead", "kKHsf4qA3sasN2OrDJDJR2lH")
#     ret = client.connect("aiot-mqtt-test.aqara.cn", 1883)

#     # ret = client.connect(broker, 1883)
#     print(ret)
#     return client


# cli = conn()
# cli.loop_start()

# time.sleep(600)
# print("end")



# import random
# import time

# from paho.mqtt import client as mqtt_client


# broker = 'broker.emqx.io'
# # broker = "aiot-mqtt-test.aqara.cn"
# port = 1883
# # topic = "/python/mqtt"
# # generate client ID with pub prefix randomly
# # client_id = f'python-mqtt-{random.randint(0, 100)}'

# client_id = "omqt.dcd32f47-8116-4ef6-a8b4-36b46a7f7238"




# # def on_disconnect(self, client, userdata, rc): #, rc
# def on_disconnect(self, client, userdata): #, rc
#     # if rc != 0:
#     #     print(f"Unexpected disconnection.{rc}")
#     # else:
    
#     print("disconnect")


# def on_connect(client, userdata, flags, rc):
#     if rc == 0:
#         print("Connected to MQTT Broker!")
#     else:
#         print("Failed to connect, return code %d\n", rc)

# def connect_mqtt() -> mqtt_client:




#     client = mqtt_client.Client(client_id)
#     client.username_pw_set("948959825666478080da1ead", "kKHsf4qA3sasN2OrDJDJR2lH")
#     client.on_connect = on_connect
#     client.on_disconnect = on_disconnect
#     client.connect(broker, port)
#     return client


# def subscribe(client: mqtt_client, topic: str):
#     def on_message(client, userdata, msg):
#         print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")

#     ret = client.subscribe(topic)
#     print(ret)
#     client.on_message = on_message


# # def run():



# client = connect_mqtt()

# time.sleep(1)
# subscribe(client, "receive_omqt.dcd32f47-8116-4ef6-a8b4-36b46a7f7238")

# # subscribe(client, "#")
# # client.loop_forever()
# client.loop_start()



# time.sleep(600)


# run()


# Received 
# `{"data":[{"resourceId":"14.7.111","time":"1646303154714","triggerSource":{"time":"1646303154","type":4},"value":"1","subjectId":"virtual.93083750786711","statusCode":0}],"msgId":"AC10C8A4001E18B4AAC20E41363B00371","msgType":"resource_report","openId":"853851328861948953623941439489","time":"1646303154747"}` 
# from `receive_omqt.dcd32f47-8116-4ef6-a8b4-36b46a7f7238` topic







