from tkinter import *
import sqlite3
window = Tk()

t1 = Text(window,height=5,width=20)
t1.grid(row=1,column=0,padx=20,pady=10)

def createTable():
	conn = sqlite3.connect("WebDB01.db")
	cur = conn.cursor()
	cur.execute("CREATE TABLE IF NOT EXISTS db (url TEXT)")
	conn.commit()
	conn.close()

def insertWebsite():
	conn = sqlite3.connect("WebDB01.db")
	cur = conn.cursor()
	cur.execute("INSERT INTO db VALUES (?)",(siteUrl.get(),))
	conn.commit()
	conn.close()
	t1.insert(END,siteUrl.get()+"\n")
	e1.delete(0,END)
	e2.delete(0,END)

def getWebsites():
	conn = sqlite3.connect("WebDB01.db")
	cur = conn.cursor()
	cur.execute("SELECT url FROM db")
	rows = cur.fetchall()
	conn.close()
	return rows

def showWebsites():
	rows = getWebsites()
	for web in rows:
		t1.insert(END,web[0]+"\n")

createTable()
showWebsites()

siteName = StringVar()
e1 = Entry(window,textvariable = siteName)
e1.grid(row = 0, column = 0,padx = 10, pady=10)

siteUrl = StringVar()
e2 = Entry(window,textvariable = siteUrl)
e2.grid(row = 0, column = 1,padx = 10, pady=10)

b1 = Button(window,text = "ADD",command = insertWebsite)
b1.grid(row = 1,column=1,padx = 10,pady=10)

window.mainloop()