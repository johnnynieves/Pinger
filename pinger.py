#!/usr/bin/env python3

from icmplib import ping, multiping, traceroute
from time import sleep, time, ctime
from csv import reader, writer
from colorama import Fore, Style
from os import error, system
from email.message import EmailMessage
import smtplib


def newscreen():
    system('clear')


def start():
    for year in range(0, 365 + 1):
        with open(f'Standard_Log_{ctime()}.csv', 'a+') as log:
            print(f'Starting log for {ctime()}\n')
            log.write(f'Monitoring Log for {ctime()}\n')
            log.write('')
            log.write(f'DEVICE     ,NETWORK IP     ,STATUS     ,LOG_TIME\n')
            for minutes in range(0, 1440+1):
                ping_devices(log)
                sleep(300)
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
                # alert(dead):


def alert(dead):
    msg = EmailMessage()
    msg['Subject'] = 'Device Down!!'
    msg['From'] = 'from_me@gmail.com'
    # Can add a list for more individuals
    msg['To'] = 'To@gmail.com'
    msg.set_content(f'Check {dead}')

    with open(directory, 'rb') as f:
        file_data = f.read()
        # file_type = 'image' only use for sending an image |
        file_type = 'octet-stream'
        file_name = directory.split('/')[4]  # gets the name of file only

    # attachments = ['this will be a search in the directory']
    msg.add_attachment(
        file_data,
        maintype='application',
        subtype=file_type,
        filename=file_name
    )
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(email, password)
        smtp.send_message(msg)
    print('Email Sent')


if '__main__' == __name__:
    try:
        newscreen()
        start()
    except:
        KeyboardInterrupt
        print('\nYou decided to quit the Pinger?!\nGood Bye!!!')
        exit(1)
