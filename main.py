import datetime
import os
import subprocess

GIT_URL = "https://github.com/CoollLzZ/systeminfo.git"


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
        info.write(Installed_Software)  # I used variable names directly here but before calling function
        # #need to be declared
        info.write("---------------------------------------------------------------------------------------------\n")
        info.write("--------------------------------------Windows Activation-----------------------------------\n")
        info.write("---------------------------------------------------------------------------------------------\n\n")
        info.write(out + "\n")
        if "This machine is permanently activated." in out:
            info.write("Windows is activated")
        else:
            info.write("Windows is not activated.")


# Todo: Creating function for pushing data-file into Public repo
def git_push(date, sr):
    """This function needs some args: date=today's date and sr=serial number"""
    # command = "echo %cd%"
    # pwd = os.popen(command).read()

    command = f"git config --global --add safe.directory '*'"
    subprocess.run(command, shell=True)

    command = "git add ."
    subprocess.run(command, shell=True)

    command = f'git commit -m "Pushing info on {date} for serial number:{sr}"'
    subprocess.run(command, shell=True)

    # command = f"git remote add origin '{GIT_URL}'"
    # subprocess.run(command, shell=True)
    command = f"git push"
    subprocess.run(command, shell=True)


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

# Todo: Checking for the windows is activated or not.
cmd = 'cscript slmgr.vbs -xpr | findstr -i activate'
output = subprocess.Popen(cmd, shell=True, cwd="C:\Windows\System32", stdout=subprocess.PIPE)
out, err = output.communicate()
out = str(out[3:-1])
out = out[3:-3]

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

# Todo: Pushing the data file on remote repository.
git_push(date=today, sr=SR_number)
print(f"Push Successful for sr:{SR_number}")
