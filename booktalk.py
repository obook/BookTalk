# -*- coding: utf-8 -*-
"""
Created on Fri May 31 20:38:33 2024
Projet NSI 2023-2024 Sainte-Marie Bastide/Bordeaux
@author: obook
"""

from tkinter import *
from threading import Thread

from recepteur import ServerStart
from emetteur import ClientSpeak
from interface import *
from devices import InputDevices, OutputDevices

states = {"recepteur":True,"emetteur":False} # False=off True=on

#╣ Default devices

OutputDevicesList = []
InputDevicesList = []

def StartListen():
    itemid = GetOutputCombo()
    deviceid = OutputDevicesList[itemid]['id']
    devicename = OutputDevicesList[itemid]['name']
    print(f"Start Listen on {devicename} ({deviceid})")
    
    server_thread = Thread(target=ServerStart, args=(states,deviceid))
    server_thread.start()
    SetStartOn()
    SetSpeakEnable()

def StopListen():
    print("StopListen...")
    states['recepteur'] = False
    SetStartOff()
    
def StartSpeak(event):   

    if str(event.widget).split(".")[-1] == 'buttonSpeak':
        itemid = GetInputCombo()
        deviceid = InputDevicesList[itemid]['id']
        devicename = InputDevicesList[itemid]['name']
        friendip = GetInputIp()
        print(f"Start Speak to {friendip} on {devicename} ({deviceid})")

        if str(event.widget).split(".")[-1] == 'buttonSpeak':
            client_thread = Thread(target=ClientSpeak, args=(states,deviceid,friendip))
            states['emetteur'] = True
            client_thread.start()

def StopSpeak(event):
    if str(event.widget).split(".")[-1] == 'buttonSpeak':
        states['emetteur'] = False

        
def Quit():
    print("Quitter")
    states['emetteur'] = False
    states['recepteur'] = False
    Fenetre.destroy()
    

OutputDevicesList = OutputDevices()
InputDevicesList = InputDevices()

Fenetre = MakeInterface(StartListen,StopListen,Quit, OutputDevicesList, InputDevicesList) # MakeInterface(StartFunc, StopFunc, QuitFunc):

# Détection du clic souris gauche
Fenetre.bind("<ButtonPress-1>", StartSpeak) # Appuyé
Fenetre.bind("<ButtonRelease-1>", StopSpeak) # Relaché

SetSpeakDisabled()

Fenetre.mainloop() # lance la boucle principale


print("FINI !")
