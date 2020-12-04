#SDWAN functions inside SDWAN folder

import requests
import json
from slproject.sdwan.sdwan_py_functions.auth import login

def get_devicecontrollers():
    session = login()
    baseurl = "https://10.100.99.28:8443"
    controller_endpoint = "/dataservice/system/device/controllers"
    url = f"{baseurl}{controller_endpoint}"
    #print('Exectuing following URL:\n',url ,'\n')
    response_controller = session.get(url, verify=False)
    devices = response_controller.json()['data']
    return devices

if __name__ == "__main__":
   response = get_devicecontrollers()