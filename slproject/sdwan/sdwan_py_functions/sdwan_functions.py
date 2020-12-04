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
#    for device in devices:
#        if device['deviceType']=='vmanage':
#            print('success - we have a vmanage')
#        print(f"Device controller => {device['deviceType']} with System IP address {device['deviceIP']}")


device_list = get_devicecontrollers()

for device in device_list:
    if device['deviceType'] == 'vmanage':
        print('The name of the device is: ',device['host-name'])


#print(vmanage)

if __name__ == "__main__":
   response = get_devicecontrollers()