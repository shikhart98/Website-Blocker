import time
from datetime import datetime as dt
import sqlite3

def getWebsites():
	conn = sqlite3.connect("WebDB01.db")
	cur = conn.cursor()
	cur.execute("SELECT url FROM db")
	rows = cur.fetchall()
	conn.close()
	return rows

#hosts file path [this is for windows]
hosts_temp = "hosts"
hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
#ip address
redirect = "127.0.0.1"

#list of websites you want to block
websites = []
for web in getWebsites():
	websites.append(web[0])

while True :
	if dt(dt.now().year,dt.now().month,dt.now().day,9) < dt.now() <  dt(dt.now().year,dt.now().month,dt.now().day,12) :
		print("Working hours!")
		with open(hosts_path,'r+') as file:
			content = file.read()
			for website in websites:
				if website in content:
					pass
				else :
					file.write(redirect+"	"+website+"\n")
	else :
		print("Fun hours!")
		with open(hosts_path,'r+') as file:
			content = file.readlines() # this will return me a list of strings where each element is the line of file host_temp
			file.seek(0) # moves pointer to the start of the file
			for line in content:
				if not any(website in line for website in websites):
					file.write(line)
			file.truncate() # deletes everything below where the file pointer is.
	time.sleep(10) #sleeps for 5 seconds and run the while loop after every 5 seconds.


