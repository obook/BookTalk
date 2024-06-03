# -*- coding: utf-8 -*-
"""
Created on Jun 2 2024
Projet NSI 2023-2024 Sainte-Marie Bastide/Bordeaux
@author: obook
"""

import tkinter, tkinter.ttk
from PIL import Image, ImageTk
from ip import get_interfaces
from settings import GetFriendIp, GetOutputId, GetInputId

ips = get_interfaces()
FriendIp = GetFriendIp()

Fenetre = tkinter.Tk() #création de la fenêtre, avec un nom de votre choix Fenetre
Fenetre.title('BookTalk ' +ips[0]['ip']) #Titre de la fenêtre
Fenetre.geometry("400x120")
Fenetre.resizable(False, False)

ico = Image.open('booktalk.png')
photo = ImageTk.PhotoImage(ico)
Fenetre.wm_iconphoto(False, photo)

# configure the grid
Fenetre.columnconfigure(0, weight=1)
Fenetre.columnconfigure(1, weight=3)

OuputDevice_Label= tkinter.Label(Fenetre, text = 'Écouteurs :').grid(row=1, column=1)
OutputDeviceCombo = tkinter.ttk.Combobox(Fenetre,width=50)
OutputDeviceCombo.grid(row=1, column=2)

InputDevice_Label= tkinter.Label(Fenetre, text = 'Microphone :').grid(row=2, column=1) #Un label pour afficher du texte
InputDeviceCombo = tkinter.ttk.Combobox(Fenetre,width=50)
InputDeviceCombo.grid(row=2, column=2)

FriendIP_Label=tkinter.Label(Fenetre, text = 'IP Ami :').grid(row=3, column=1)
FriendIP = tkinter.StringVar()
FriendIP.set(FriendIp)
FriendIPEntry = tkinter.Entry(Fenetre,textvariable = FriendIP)
FriendIPEntry.grid(row=3, column=2)

Button_Start = tkinter.Button(Fenetre, text ='Démarrer', width=10)
Button_Start.grid(row=4, column=1)

Button_Stop = tkinter.Button(Fenetre, text ='Arrêter', width=10, state="disabled")
Button_Stop.grid(row=4, column=2)

Button_Speak = tkinter.Button(Fenetre, name="buttonSpeak", text ='Parler', width=10, activebackground="red", state="disabled")
Button_Speak.grid(row=5, column=1)

Button_Quit = tkinter.Button(Fenetre, text ='Quitter', width=10)
Button_Quit.grid(row=5, column=2)

def MakeInterface(StartFunc, StopFunc, QuitFunc, OutputDevicesList, InputDevicesList):

    OutputDevices=[]
    for OutputDevice in OutputDevicesList:
        OutputDevices.append(OutputDevice["name"])
    OutputDeviceCombo['values'] = OutputDevices
    try:
        OutputDeviceCombo.current(GetOutputId()) # Crash if id do not exist
    except:
       pass
     
    InputDevices=[]
    for InputDevice in InputDevicesList:
        InputDevices.append(InputDevice["name"])
    InputDeviceCombo['values'] = InputDevices
    try:
        InputDeviceCombo.current(GetInputId()) # Crash if id do not exist
    except:
       pass
    
    Button_Start['command'] = StartFunc
    Button_Stop['command'] = StopFunc
    Button_Quit['command'] = QuitFunc
    
    return Fenetre

def GetOutputCombo():
    return OutputDeviceCombo.current()

def GetInputCombo():
    return InputDeviceCombo.current()

def GetInputIp():
    return FriendIP.get()

def SetStartOn():
    #Button_Start["bg"] = 'green'
    #Button_Start["fg"] = 'black'
    Button_Start["text"] = 'Démarré'
    Button_Start.config(state="disabled")
    Button_Stop.config(state="normal")
    Button_Speak.config(state="normal")
    OutputDeviceCombo.config(state="disabled")
    FriendIPEntry.config(state="disabled")

def SetStartOff():
    Button_Start.config(bg = 'SystemButtonFace')
    Button_Start.config(state="normal")
    Button_Start["text"] = 'Démarrer'
    Button_Stop.config(state="disabled")
    Button_Speak.config(state="disabled")
    OutputDeviceCombo.config(state="normal")
    FriendIPEntry.config(state="normal")
    
def SetSpeakDisabled():
    Button_Speak.config(state="disabled")
    
def SetSpeakEnable():
    Button_Speak.config(state="normal")
    