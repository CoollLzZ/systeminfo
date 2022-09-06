import datetime
import os

# Todo: Getting Current date
today = datetime.date.today()

# Todo: Collecting the serial number of system
cmd = 'wmic bios get serialnumber'
SR_number = os.popen(cmd).read()
SR_number = SR_number.split("\n")[2]

# Todo: Collecting the system's information
cmd = 'systeminfo'
systemInfo = os.popen(cmd).read()

# Todo: Collecting Installed Software list
cmd = "wmic product get Name, Version"
Installed_Software = os.popen(cmd).read()

with open(mode='w', file=f'{today}_{SR_number[0:7]}.txt') as info:
    info.write(f'\nThis file is registered with Serial Number: {SR_number}\n\n')
    info.write("---------------------------------------------------------------------------------------------\n")
    info.write("--------------------------------------Detailed System Info-----------------------------------\n")
    info.write("---------------------------------------------------------------------------------------------\n")
    info.write(systemInfo)
    info.write("\n\n\n")
    info.write("---------------------------------------------------------------------------------------------\n")
    info.write("--------------------------------------Installed Software's-----------------------------------\n")
    info.write("---------------------------------------------------------------------------------------------\n\n")
    info.write(Installed_Software)

# Todo: Pushing info file to public repository
GIT_URL= 'https://github.com/CoollLzZ/systeminfo.git'
cmd = 'git add .'
os.popen(cmd)
