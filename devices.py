# -*- coding: utf-8 -*-
"""
Projet NSI 2023-2024 Sainte-Marie Bastide/Bordeaux
@author: obook
"""

import pyaudio
from utils import get_wasapi_devices, get_output_devices, get_wasapi_devices

def OutputDevices():
    OutputDevicesList=[]
    audio = pyaudio.PyAudio()
    output_devices = get_output_devices(audio)
    for device_id in output_devices:
        dic={'id':device_id,'name':output_devices[device_id]['name']}
        OutputDevicesList.append(dic)
    return OutputDevicesList

def InputDevices():
    InputDevicesList=[]
    audio = pyaudio.PyAudio()
    input_devices = get_wasapi_devices(audio)
    for device_id in input_devices:
        dic={'id':device_id,'name':input_devices[device_id]['name']}
        InputDevicesList.append(dic)
    return InputDevicesList

    