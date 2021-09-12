import notifypy
import time
# import sys

notification = notifypy.Notify()

# usertime = sys.argv[1]
usertime = input("Enter when you want to set: ")

def done(usert):
	notification.title = f"Time is {usert}"
	notification.message = f"You set the alarm for {usert}"
	notification.audio = "files/alarm.wav"
	notification.icon = "files/icon.png"

	notification.send()

while True:
	now = time.strftime("%H:%M:%S", time.localtime())
	
	if now == usertime:
		break
	else:
		time.sleep(1)
		pass
		
while True:
	done(usertime)
	time.sleep(10)
