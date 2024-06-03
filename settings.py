# -*- coding: utf-8 -*-
"""
Created on Jun 2 2024
Projet NSI 2023-2024 Sainte-Marie Bastide/Bordeaux
@author: obook
"""

import json

config = {"friendip": "127.0.0.1", "OutputDeviceId": 0, "InputDeviceId": 0}

settingsfile = 'booktalk.json'

def LoadConfig():
    global config
    
    try:
        with open(settingsfile, 'r') as f:
            config = json.load(f)
    except:
        SaveConfig()
        
    return True

def SaveConfig():
    with open(settingsfile, 'w') as f:
        json.dump(config, f)
    return True

def GetFriendIp():
    LoadConfig()
    return config['friendip']

def SaveFriendIp(ip):
    config['friendip'] = ip
    return SaveConfig()

def GetOutputId():
    LoadConfig()
    return config['OutputDeviceId']

def SaveOutputId(n):
    config['OutputDeviceId'] = n
    return SaveConfig()

def GetInputId():
    LoadConfig()
    return config['InputDeviceId']

def SaveInputId(n):
    config['InputDeviceId'] = n
    return SaveConfig()

    