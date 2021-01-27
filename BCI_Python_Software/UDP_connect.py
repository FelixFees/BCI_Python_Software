# This python script listens on UDP port 3333
# for messages from the ESP32 board and prints them
import socket
import sys
import numpy as np


def collect_data():

    time = []
    channel_1 = []
    channel_2 = []
    channel_3 = []
    channel_4 = []
    channel_5 = []
    channel_6 = []

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    except socket.error as msg:
        print('Failed to create socket. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
        sys.exit()

    try:
        s.bind(('', 3333))
    except socket.error as msg:
        print('Bind failed. Error: ' + str(msg[0]) + ': ' + msg[1])
        sys.exit()

    print('Server listening')
    for x in range(7):
        converted_data = []

        d = s.recvfrom(1024)
        data = d[0]
        data = data.decode("utf-8")
        data = data.split("\r\n")

        for i in range(len(data)-1):
            data_converter = float(data[i])
            converted_data.append(data_converter)

        if converted_data[0] == 0.0:
            time = converted_data
            time = time[1:]

        elif converted_data[0] == 1.0:
            channel_1 = converted_data
            channel_1 = channel_1[1:]

        elif converted_data[0] == 2.0:
            channel_2 = converted_data
            channel_2 = channel_2[1:]

        elif converted_data[0] == 3.0:
            channel_3 = converted_data
            channel_3 = channel_3[1:]

        elif converted_data[0] == 4.0:
            channel_4 = converted_data
            channel_4 = channel_4[1:]

        elif converted_data[0] == 5.0:
            channel_5 = converted_data
            channel_5 = channel_5[1:]

        elif converted_data[0] == 6.0:
            channel_6 = converted_data
            channel_6 = channel_6[1:]

        if not data:
            break

    s.close()
    return np.vstack((time, channel_1, channel_2, channel_3, channel_4, channel_5, channel_6))

