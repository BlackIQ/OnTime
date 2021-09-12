import notifypy
import getpass
import time
# import sys

notification = notifypy.Notify()

user = getpass.getuser()

# usertime = sys.argv[1]
usertime = input("Enter when you want to set: ")

def done(user, usert):
	notification.title = f"Time is {usert}"
	notification.message = f"You set the alarm for {usert}"
	notification.audio = f"/home/{user}/.ontime/files/alarm.wav"
	notification.icon = f"/home/{user}/.ontime/files/icon.png"
	
	notification.send()

while True:
	now = time.strftime("%H:%M:%S", time.localtime())
	
	if now == usertime:
		break
	else:
		time.sleep(1)
		pass
		
while True:
	done(user, usertime)
	time.sleep(10)
