"""Aqara Open IOT HUB which base on MQTT."""
from __future__ import annotations
from multiprocessing import set_forkserver_preload

import time


import threading
import time
from typing import Any, Callable
from typing import Optional
from paho.mqtt import client as mqtt
from .openlogging import logger


# import sys,os
# sys.path.append(os.getcwd())
# from .device import AqaraDeviceManager
# from .openapi import  AqaraOpenAPI

# LINK_ID = f"aqara-iot-app-sdk-python.{uuid.uuid1()}"
# CONNECT_FAILED_NOT_AUTHORISED = 5



class AqaraMQConfig:
    """Aqara mqtt config."""

    def __init__(self, cfg: dict[str, str] = {}) -> None:
        """Init AqaraMQConfig."""
        #  {
        #     "password": "BG2FRrJTIGCaHTP4Ga2Mlfrr",
        #     "clientId": "omqt.9617f124-a3e3-45fb-8cc5-64c2017b99d5",
        #     "subscribeTopic": "receive_omqt.9617f124-a3e3-45fb-8cc5-64c2017b99d5",
        #     "mqttHost": "aiot-mqtt-test.aqara.cn",
        #     "userName": "9478646628902215681ddba4",
        #     "mqttPort": "1883",
        #     "publishTopic": "control_omqt.9617f124-a3e3-45fb-8cc5-64c2017b99d5"
        # }

        self.password = cfg.get("password", "")
        self.client_id = cfg.get("clientId", "")
        self.source_topic = cfg.get("publishTopic", {})
        self.host = cfg.get("mqttHost", "")
        self.port = int(cfg.get("mqttPort", 0))
        self.username = cfg.get("userName", "")
        self.subscribe_topic = cfg.get("subscribeTopic", {})
        self.expire_time = cfg.get("expireTime", 7200)


class AqaraOpenMQ(threading.Thread):
    """Aqara open iot mqtt client.

    eg:
    aqara_mq = AqaraOpenMQ()
    aqara_mq.set_get_config(device_manager.config_mqtt_add)
    aqara_mq.add_message_listener(device_manager.on_message)
    aqara_mq.start()
      
    """
    def __init__(self, is_debug = False) -> None:
        """Init AqaraOpenMQ."""
        threading.Thread.__init__(self)
        self._stop_event = threading.Event()
        self.client = None
        self.need_reconnect = True
        self.mq_config = None
        self.message_listeners = set()
        self.get_config = None
        self.is_debug = is_debug

    def set_get_config(self, get_config: Callable[[str], None]):
        """set the callback func which will be used to get mqtt config"""
        self.get_config = get_config

    def _get_mqtt_config(self) -> Optional[AqaraMQConfig]:       
        if self.get_config is None:
            return None

        if self.is_debug:
            cfg = { #debug cfg
                'password':'kKHsf4qA3sasN2OrDJDJR2lH',
                'clientId':'omqt.dcd32f47-8116-4ef6-a8b4-36b46a7f7238',
                'subscribeTopic':'receive_omqt.dcd32f47-8116-4ef6-a8b4-36b46a7f7238',
                'mqttHost':'aiot-mqtt-test.aqara.cn',
                'userName':'948959825666478080da1ead',
                'mqttPort':'1883',
                'publishTopic':'control_omqt.dcd32f47-8116-4ef6-a8b4-36b46a7f7238',
            }
            return AqaraMQConfig(cfg)
        
        cfg = AqaraMQConfig(self.get_config())

        if len(cfg) == 0 or cfg.host == "":
            return None
        else :
            return cfg

    def _decode_mq_message(self, b64msg: str, password: str, t: str) -> dict[str, Any]:
        print(b64msg)
        # key = password[8:24]
        # cipher = AES.new(key.encode("utf8"), AES.MODE_ECB)
        # msg = cipher.decrypt(base64.b64decode(b64msg))
        # padding_bytes = msg[-1]
        # msg = msg[:-padding_bytes]
        # return json.loads(msg)
  

    def _on_disconnect(self, client, userdata, rc):
    # def _on_disconnect(self, client, userdata):        
        if self.client is not None and self.need_reconnect:
            # 每次断开都会更改 client 和 use name password，重连需要重新设置
            mq_config = self._get_mqtt_config()
            self.client._client_id = mq_config.client_id
            self.client.username_pw_set(mq_config.username, mq_config.password)
            self.client.user_data_set({"mqConfig": mq_config})

        logger.debug("disconnect")

    def _on_connect(self, mqttc: mqtt.Client, user_data: Any, flags, rc):
        logger.debug(f"connect flags->{flags}, rc->{rc}")
        if rc == 0:
            mqttc.subscribe(user_data["mqConfig"].subscribe_topic)   

    def _on_message(self, mqttc: mqtt.Client, user_data: Any, msg: mqtt.MQTTMessage):
        logger.debug(f"payload-> {msg.payload}")

        # {
        #     "data":[
        #             {   "resourceId":"14.7.111",
        #                 "time":"1646303154714",
        #              "triggerSource":{"time":"1646303154","type":4},
        #              "value":"1",
        #              "subjectId":"virtual.93083750786711",
        #              "statusCode":0}
        #              ],
                    
        #  "msgId":"AC10C8A4001E18B4AAC20E41363B00371",
        #  "msgType":"resource_report",
        #  "openId":"853851328861948953623941439489",
        #  "time":"1646303154747"
        #  }

        data = msg.payload.decode("utf8")
        #decode data

        for listener in self.message_listeners:
            listener(data)

    def _on_subscribe(self, mqttc: mqtt.Client, user_data: Any, mid, granted_qos):
        logger.debug(f"_on_subscribe: {mid}")

    def _on_log(self, mqttc: mqtt.Client, user_data: Any, level, string):
        logger.debug(f"_on_log: {string}")

    def run(self):
        """Method representing the thread's activity which should not be used directly."""
        while not self._stop_event.is_set():
            self.__run_mqtt()

            # reconnect every 2 hours required.
            if self.mq_config is not None:
                time.sleep(self.mq_config.expire_time - 60)
            else :
                time.sleep(7200)

    def __run_mqtt(self):
        mq_config = self._get_mqtt_config()
        if mq_config is None :
            logger.error("error while get mqtt config")
            time.sleep(60*5) 
            return

        self.mq_config = mq_config

        logger.debug(f"connecting {mq_config.host}")

        if self.client is not None:
            self.need_reconnect = False
            self.client.disconnect()

        mqttc = self._start(mq_config)            
        self.client = mqttc
        self.need_reconnect = True

    def _start(self, mq_config: AqaraMQConfig) -> mqtt.Client:
        mqttc = mqtt.Client(mq_config.client_id)
        mqttc.username_pw_set(mq_config.username, mq_config.password)
        mqttc.user_data_set({"mqConfig": mq_config})
        mqttc.on_connect = self._on_connect
        mqttc.on_message = self._on_message
        mqttc.on_subscribe = self._on_subscribe
        # mqttc.on_log = self._on_log
        mqttc.on_disconnect = self._on_disconnect

        # url = urlsplit(mq_config.url)
        # if url.scheme == "ssl":
        #     mqttc.tls_set()

        # mqttc.tls_set()

        mqttc.connect(mq_config.host, mq_config.port)

        mqttc.loop_start()
        return mqttc

    def start(self):
        """Start mqtt.

        Start mqtt thread
        """
        logger.debug("start")
        super().start()

    def stop(self):
        """Stop mqtt.

        Stop mqtt thread
        """
        logger.debug("stop")
        self.need_reconnect = False
        self.message_listeners = set()
        if self.client is not None:
            self.client.disconnect()
            self.client = None
        self._stop_event.set()

    def add_message_listener(self, listener: Callable[[str], None]):
        """Add mqtt message listener."""
        self.message_listeners.add(listener)

    def remove_message_listener(self, listener: Callable[[str], None]):
        """Remvoe mqtt message listener."""
        self.message_listeners.discard(listener)





