# -*- coding: utf-8 -*-
"""
Projet NSI 2023-2024 Sainte-Marie Bastide/Bordeaux
@author: obook
Source originale : https://github.com/richardos/audio-stream
"""

import socket
import sys
import time

import pyaudio
import utils

# default configuration parameters
DEFAULT_SERVER_IP = '127.0.0.1'
DEFAULT_SERVER_PORT = 9999
STREAM_FORMAT = pyaudio.paInt16
BUFFER_SIZE = 16384

srvconn = 0;

def callback(in_data, frame_count, time_info, status):
    global srvconn
    srvconn.send(in_data)
    return in_data, pyaudio.paContinue


def ClientSpeak(states,deviceid,friendip):
    global srvconn
    
    srvconn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    srvconn.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    audio = pyaudio.PyAudio()

    # get all WASAPI devices
    wasapi_devices = utils.get_wasapi_devices(audio)
    if len(wasapi_devices) == 0:
        print('No WASAPI device found')
        sys.exit()

    # selected_device_id = utils.handle_device_selection(args.dev_id,wasapi_devices)
    selected_device_id = deviceid #17
    selected_device_info = wasapi_devices[selected_device_id]
    
    # print('You have selected:', selected_device_info)
    
    # input('Press enter to start streaming')

    channels = max(selected_device_info["maxInputChannels"],
                   selected_device_info["maxOutputChannels"])

    while states['emetteur'] == True:
        # Open stream
    
        stream = audio.open(format=STREAM_FORMAT,
                            channels=channels,
                            rate=int(selected_device_info["defaultSampleRate"]),
                            input=True,
                            frames_per_buffer=BUFFER_SIZE,
                            input_device_index=selected_device_info["index"],
                            stream_callback=callback) # as_loopback=True ??

        # Start stream
        try:
            print('ClientSpeak:Connecting to server...')
            srvconn.connect((friendip,DEFAULT_SERVER_PORT)) # DEFAULT_SERVER_IP
            print('ClientSpeak:Connected.')
            stream.start_stream()
            print("ClientSpeak:Stream started.")
    
            while stream.is_active() and states['emetteur'] == True:
                time.sleep(0.1)
        finally:
            # Stop stream
            stream.stop_stream()
            stream.close()
            print("ClientSpeak:Stopped.")
    
            # Cleanup
            srvconn.close()
            audio.terminate()

def ClientSpeakTest(states):
    
    print("ClientSpeak:Thread Start")

    while states['emetteur'] == True:
        #if stopping_event.is_set() and id==1 :
        #    break
        pass
    
    print("ClientSpeak:Thread finished")
    
    