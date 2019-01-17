#!/usr/bin/python3
# wifi hotspot enabler

import os
os.system('cls')
print('\n\n\n\n\n')
print('Green Hackers WiFi Hotspot Enabler')
print('(c) 2019 Green Hackers Group. All right reserved.')
print()
ssid = 'AungWinHtut'
password = 'asdfqwer'
cmd = '0'
while cmd != '3':
    print('1-Start Hotspot')
    print('2-Stop Hotspot')
    print('3- exit')
    cmd = input('Please Enter Your Choice (1,2,3): ')
    if cmd == '1':
        print('Starting Wifi hotspot....')
        ssid = input('Please Enter SSID: ')
        password = input('Please Enter Password: ')
        command = "netsh wlan set hostednetwork mode=allow ssid=" + ssid + " key=" + password
        os.system(command)
        os.system('netsh wlan start hostednetwork')
    elif cmd == '2':
        print('Stopping Wifi hotspot....')
        os.system('netsh wlan stop hostednetwork')
    elif cmd == '3':
        print('Exiting Program....')
        quit()
    else:
        print("Bad input! Please try again (Only 1,2,3)")
        os.system('pause')


