import datetime
import os
import subprocess


# Todo: Creating function for generating data file
def info_gen(day, sr):
    """Please Provide day=today's date and sr=serial number of the M/C"""
    with open(mode='w', file=f'Data/{sr}/{sr}_{day}') as info:
        info.write(f'\nThis file is registered with Serial Number: {sr}\n\n')
        info.write("---------------------------------------------------------------------------------------------\n")
        info.write("--------------------------------------Detailed System Info-----------------------------------\n")
        info.write("---------------------------------------------------------------------------------------------\n")
        info.write(systemInfo)
        info.write("\n\n\n")
        info.write("---------------------------------------------------------------------------------------------\n")
        info.write("--------------------------------------Installed Software's-----------------------------------\n")
        info.write("---------------------------------------------------------------------------------------------\n\n")
        info.write(Installed_Software)


# Todo: Getting Current date
today = datetime.date.today()

# Todo: Collecting the serial number of system
cmd = 'wmic bios get serialnumber'
SR_number = os.popen(cmd).read()
SR_number = SR_number.split("\n")[2]
SR_number = SR_number[0:7]

# Todo: Collecting the system's information
cmd = 'systeminfo'
systemInfo = os.popen(cmd).read()

# Todo: Collecting Installed Software list
cmd = "wmic product get Name, Version, InstallDate"
Installed_Software = os.popen(cmd).read()

# Todo: Directory confirmation of this serial number, Otherwise create a separate directory for this serial.
cmd = f"dir Data| findstr {SR_number}"
folder = subprocess.run(cmd, shell=True)

# Todo: Checking the return-code of last command.
if folder.returncode == 0:
    # That means the folder for this serial number exists
    info_gen(day=today, sr=SR_number)
else:
    # That means we have to create a folder for new serial number
    # Todo: Creating sr number folder for the new M/C
    cmd = f"mkdir Data\{SR_number}"
    folder = subprocess.run(cmd, shell=True)
    info_gen(day=today, sr=SR_number)
