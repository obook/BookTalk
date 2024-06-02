# -*- coding: utf-8 -*-
"""
Created on Jun 2 2024
Projet NSI 2023-2024 Sainte-Marie Bastide/Bordeaux
@author: obook
"""

import json

config = {"friendip": "127.0.01", "OutputDeviceId": 0, "InputDeviceId": 0}

def SaveConfig():
    global config
    
    with open('booktalk.json', 'w') as f:
        json.dump(config, f)

def LoadConfig():
    global config

    with open('config.json', 'r') as f:
        config = json.load(f)
    
def GetFriendIp():
    global config
    
    LoadConfig()
    return config['friendip']

def SetFriendIp(ip):
    global config
    
    config['friendip'] = ip
    SaveConfig()
    