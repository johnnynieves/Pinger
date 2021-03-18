#!/usr/bin/env python3

from icmplib import ping, multiping, traceroute
from time import sleep, time, ctime
from csv import reader, writer
from colorama import Fore, Style
from os import error, system


def newscreen():
    system('clear')


def start():
    for year in range(0, 365 + 1):
        with open(f'Standard_Log_{ctime()}.csv', 'a+') as log:
            print(f'Starting log for {ctime()}\n')
            log.write(f'Monitoring Log for {ctime()}\n')
            log.write('')
            log.write(f'DEVICE     ,NETWORK IP     ,STATUS     ,LOG_TIME\n')
            for minutes in range(0, 1440):
                ping_devices(log)
                sleep(5)
                system('clear')


def ping_devices(log):
    # check1 = 'blank'
    # check2 = 'blank2'
    with open('devices.csv', 'r') as device:
        devices = reader(device)
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
                log.write(f'{object[0]},{object[1]},Down,{ctime()}\n')
            # alert(check1, object[1])
                # check2 = object[1]
                # if check1 == check2:
                #     print(
                #         f"This is your alert {check2} has been {Fore.LIGHTRED_EX} Down{Style.RESET_ALL} for atleast 2 minutes!!")
                # check2 = check1


def alert(check1, check2):
    if check1 == check2:
        print(
            f"This is your alert {check2} has been {Fore.LIGHTRED_EX} Down{Style.RESET_ALL} for aleast 2 minutes!!")


if '__main__' == __name__:
    # try:
    newscreen()
    start()
    # except:
    #     KeyboardInterrupt
    #     print('\nYou decided to quit the Pinger?!\nGood Bye!!')
    #     exit(1)
