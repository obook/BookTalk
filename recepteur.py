# -*- coding: utf-8 -*-
"""
Created on Jun 2 2024
Projet NSI 2023-2024 Sainte-Marie Bastide/Bordeaux
@author: obook
Source originale : https://github.com/richardos/audio-stream
"""

import socket
import sys

import pyaudio
import utils

# default configuration parameters
DEFAULT_SERVER_PORT = 9999
STREAM_FORMAT = pyaudio.paInt16
BUFFER_SIZE = 65536

def run_socket_connection(port, audio_stream, states):
    
    print("run_socket_connection")

    try:
        serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        serversocket.bind(('', int(port)))
        serversocket.listen(5)

        print('Waiting for client connection...')
        transmitter, addr = serversocket.accept() # bloquant !!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        print('Client connected.')

        data = transmitter.recv(BUFFER_SIZE)
        while len(data):
            data = transmitter.recv(BUFFER_SIZE)
            audio_stream.write(data)
            
    except (ConnectionResetError, ConnectionAbortedError) as e:
        print(str(e))
    finally:
        print('Client disconnected.')
        serversocket.close()
            
    print('run_socket_connection finished.')

def ServerStart(states,deviceid):

    audio = pyaudio.PyAudio()

    # get all output devices
    output_devices = utils.get_output_devices(audio)
    if len(output_devices) == 0:
        print('No output device found')
        sys.exit()
        
    selected_device_id = deviceid # 4 # Google Buds
    selected_device_info = output_devices[selected_device_id]
   
    # print('You have selected:', selected_device_info)

    channels = max(selected_device_info["maxInputChannels"],
                   selected_device_info["maxOutputChannels"])

    try:
        stream = audio.open(format=STREAM_FORMAT,
                            channels=channels,
                            rate=int(selected_device_info["defaultSampleRate"]),
                            output=True,
                            frames_per_buffer=BUFFER_SIZE,
                            output_device_index=selected_device_id)

        while states['recepteur'] == True :
            run_socket_connection(DEFAULT_SERVER_PORT, stream, states)

    finally:
        print('ServerStart:Shutting down')
        stream.close()
        audio.terminate()


def ServerStartTest(states):
    
    print("ServerStart:Thread Start")
    
    while states['recepteur'] == True:
        #if stopping_event.is_set() and id==1 :
        #    break
        pass
    
    print("ServerStart:Thread finished")
    