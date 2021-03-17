#!/usr/bin/env python3

from icmplib import ping, multiping, traceroute
from time import sleep, time, ctime
from csv import reader, writer
from colorama import Fore, Style
from os import error, system


def mport():
    # do a check on the system to see if modules already exist if they do move on to start()
    system('sudo -H pip3 install icmplib colorama')


def start():
    for year in range(0, 365 + 1):
        with open('Standard_Log.csv', 'a+') as log:
            print(f'Starting log for {ctime()}\n')
            log.write(f'Starting log for {ctime()}\n')
            log.write('')
            log.write(f'DEVICE     ,NETWORK IP     ,STATUS     ,LOG_TIME\n')
        for minutes in range(0, 1440):
            ping_devices()
            sleep(60)
            system('clear')


def ping_devices():
    with open('devices.csv', 'r') as device:
        devices = reader(device)
        with open('Standard_Log.csv', 'a+') as log:
            for object in devices:
                response = ping(object[1], count=1)
                if response.is_alive:
                    entre = f'{object[0]} {object[1]} | is{Fore.GREEN} Up{Style.RESET_ALL} | Log {ctime()}'
                    print(entre)
                    log.write(
                        f'{object[0]},{object[1]},Up,{ctime()}\n')
                else:
                    dead = f'{object[0]} {object[1]} | is{Fore.LIGHTRED_EX} Down{Style.RESET_ALL} | Log {ctime()}'
                    print(dead)
                    log.write(
                        f'{object[0]},{object[1]},Down,{ctime()}\n')
                    # add a counter: if down twice alert people


if '__main__' == __name__:
    try:
        mport()
        start()
    except:
        KeyboardInterrupt
        print('\nYou decided to quit the Pinger?!\nGood Bye!!')
        exit(1)
