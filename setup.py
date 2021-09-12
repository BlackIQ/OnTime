import os

os.system("sudo rm -rf /bin/ontime ~/.ontime")
os.system("gcc ontime/execute.c")
os.system("mkdir exe")
os.system("cp -r a.out exe")
os.system("mv exe/a.out exe/ontime")
os.system("sudo cp -r exe/ontime /bin")
os.system("mkdir ~/.ontime")
os.system("cp -r ontime/ontime.py ~/.ontime")
os.system("rm -rf exe a.out")
os.system("pip3 install notify-py")

print("\nInstallation done.")
