import logging
import sys,os

sys.path.append(os.getcwd())

from aqara_iot.openlogging import filter_logger, logger
from aqara_iot import AqaraOpenAPI
from env import *



# aqara_logger.setLevel(logging.DEBUG)
logger.setLevel(logging.DEBUG)



# Init
openapi = AqaraOpenAPI("86")
# openapi.connect("13723489545", "Faj19880718","CHINA","")
openapi.get_auth("13723489545", "Faj19880718","")

DISCOVERY_INTEGRATIONS = ("dhcp", "ssdp", "usb", "zeroconf")

print(*DISCOVERY_INTEGRATIONS)
