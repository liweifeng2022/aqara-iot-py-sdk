import logging

import sys,os
sys.path.append(os.getcwd())
# ENDPOINT = "https://open-cn.aqara.com"

# from env import ENDPOINT

from aqara_iot import (
    AqaraOpenAPI,
    # AuthType,
    # AqaraOpenMQ,
    AqaraDeviceManager,
    AqaraHomeManager,
    AqaraDeviceListener,    
    # AqaraTokenInfo,
    AqaraDevice,
    AQARA_LOGGER
)




AQARA_LOGGER.setLevel(logging.DEBUG)
# Init
# openapi = AqaraOpenAPI(ENDPOINT, ACCESS_ID, ACCESS_KEY, AuthType.CUSTOM)
openapi = AqaraOpenAPI("86")
openapi.get_auth("13723489545", "Faj19880718","")


# Update device status
deviceManager = AqaraDeviceManager(openapi)



# openmq = AqaraOpenMQ()
# openmq.set_get_config(deviceManager.config_mqtt_add)
# openmq.add_message_listener(deviceManager.on_message)
# openmq.start()

homeManager = AqaraHomeManager(openapi, deviceManager)
homeManager.update_device_cache()
# homeManager.update_location_info()
# homeManager.query_location()
# homeManager.query_scenes()



# # deviceManager.updateDeviceCaches(devIds)
# device = deviceManager.deviceMap.get(DEVICE_ID)


class aqaraDeviceListener(AqaraDeviceListener):
    def update_device(self, device: AqaraDevice):
        print("_update-->", device)

    def add_device(self, device: AqaraDevice):
        print("_add-->", device)

    def remove_device(self, device_id: str):
        pass


# deviceManager.add_device_listener(aqaraDeviceListener())

