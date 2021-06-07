import curses,time,os
import random as r

cursor=[1,1]
u_color=("0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f")
color=u_color[0]
px=[color]*800
isdarkpalette=True

def border():
	if cursor[0]<1:cursor[0]+=1
	if cursor[0]>40:cursor[0]-=1
	if cursor[1]<1:cursor[1]+=1
	if cursor[1]>20:cursor[1]-=1

def update():
	for y in range(20):
		for x in range(40):
			if px[x+y*40]=="0":
				mainscreen.addstr(2+y,1+x," ",curses.color_pair(60))
			elif px[x+y*40]=="1":
				mainscreen.addstr(2+y,1+x," ",curses.color_pair(61))
			elif px[x+y*40]=="2":
				mainscreen.addstr(2+y,1+x," ",curses.color_pair(62))
			elif px[x+y*40]=="3":
				mainscreen.addstr(2+y,1+x," ",curses.color_pair(63))
			elif px[x+y*40]=="4":
				mainscreen.addstr(2+y,1+x," ",curses.color_pair(64))
			elif px[x+y*40]=="5":
				mainscreen.addstr(2+y,1+x," ",curses.color_pair(65))
			elif px[x+y*40]=="6":
				mainscreen.addstr(2+y,1+x," ",curses.color_pair(66))
			elif px[x+y*40]=="7":
				mainscreen.addstr(2+y,1+x," ",curses.color_pair(67))
			elif px[x+y*40]=="8":
				mainscreen.addstr(2+y,1+x," ",curses.color_pair(70))
			elif px[x+y*40]=="9":
				mainscreen.addstr(2+y,1+x," ",curses.color_pair(71))
			elif px[x+y*40]=="a":
				mainscreen.addstr(2+y,1+x," ",curses.color_pair(72))
			elif px[x+y*40]=="b":
				mainscreen.addstr(2+y,1+x," ",curses.color_pair(73))
			elif px[x+y*40]=="c":
				mainscreen.addstr(2+y,1+x," ",curses.color_pair(74))
			elif px[x+y*40]=="d":
				mainscreen.addstr(2+y,1+x," ",curses.color_pair(75))
			elif px[x+y*40]=="e":
				mainscreen.addstr(2+y,1+x," ",curses.color_pair(76))
			elif px[x+y*40]=="f":
				mainscreen.addstr(2+y,1+x," ",curses.color_pair(77))

def printPaletteType():
	if isdarkpalette:
		mainscreen.addstr(22,42,"Dark palette ",curses.color_pair(2))
	else:
		mainscreen.addstr(22,42,"Light palette",curses.color_pair(2))

splash=[
	"This program sucks!",
	"Why not?",
	"Stupid machine, you make me look bad",
	"This program is dedicated to Meggy Spletzer",
	"Ultra Efficient",
	"DYUWAH!",
	"2.0 Update: Finally removed Ultraman Belial",
	"OICU812",
	"You're 20000 milliseconds too early to catch me!",
	"Access Code GRIDMAN",
	"oppai",
	"OwO",
	"Callie was here, but this time with Marie ^w^",
	"ASSSSSSSSSSSSSSS! - AVGN",
	"Ich bitte Sie, meinen Namen zu singen!",
	"You are beautiful",
	"Tlqkffjaemfdk",
	"Shuwatch!",
	"BRAVE LOVE TIGA",
	"Why cannibalism? Isn't there anything else to eat?",
	"Goodbye, dear...my friend!",
	"Until the dying day!!!",
	"I ask that you chant my name!",
	"You're already a star, Marina. We're an unstoppable duo!",
	"Tachibana-san! Why are you just standing? Have you really betrayed us?",
	"Once you take hold of me, what will you do?",
	"Now, count up your sins!",
	"Rushia is boing boing",
	"Horny Senchou",
	"Yubi yubi! Give me your fingers!",
]
prginstString=[
	"INSTRUCTIONS",
	"WASD - Move the cursor",
	"L - Plot pixel",
	"1 -> 8 - Choose color",
	"9 - Change to light/dark palette",
	"SHIFT + 1 -> 8 - Fill",
	"[ - Save",
	"] - Load",
	"+ - Exit",
	"1 - BLACK",
	"2 - BLUE",
	"3 - GREEN",
	"4 - CYAN",
	"5 - RED",
	"6 - MAGENTA",
	"7 - YELLOW",
	"8 - WHITE",
]

def initTerm():
	global mainscreen
	mainscreen=curses.initscr()
	curses.noecho()
	curses.start_color()
	curses.curs_set(0)
	curses.init_pair(1,curses.COLOR_BLUE,curses.COLOR_BLUE)
	curses.init_pair(2,curses.COLOR_GREEN,curses.COLOR_BLUE)
	curses.init_pair(3,curses.COLOR_WHITE,curses.COLOR_BLUE)
	curses.init_pair(4,curses.COLOR_WHITE,curses.COLOR_RED)
	curses.init_pair(60,0,0)
	curses.init_pair(61,0,1)
	curses.init_pair(62,0,2)
	curses.init_pair(63,0,3)
	curses.init_pair(64,0,4)
	curses.init_pair(65,0,5)
	curses.init_pair(66,0,6)
	curses.init_pair(67,0,7)
	curses.init_pair(70,0,8)
	curses.init_pair(71,0,9)
	curses.init_pair(72,0,10)
	curses.init_pair(73,0,11)
	curses.init_pair(74,0,12)
	curses.init_pair(75,0,13)
	curses.init_pair(76,0,14)
	curses.init_pair(77,0,15)

initTerm()
for y in range(24):
	for x in range(80):
		mainscreen.addstr(y,x," ",curses.color_pair(1))
mainscreen.addstr(0,0,"IZANAGI Ver 2.1 - (C)2021 Katsumi Kougen. All rights reserved.",curses.color_pair(3))
mainscreen.addstr(1,0,chr(201),curses.color_pair(3))
for x in range(1,41):mainscreen.addstr(1,x,chr(205),curses.color_pair(3))
mainscreen.addstr(1,41,chr(187),curses.color_pair(3))
for y in range(2,22):
	mainscreen.addstr(y,0,chr(186),curses.color_pair(3))
	for x in range(1,41):mainscreen.addstr(y,x," ",curses.color_pair(60))
	mainscreen.addstr(y,41,chr(186),curses.color_pair(3))
mainscreen.addstr(22,0,chr(200),curses.color_pair(3))
for x in range(1,41):mainscreen.addstr(22,x,chr(205),curses.color_pair(3))
mainscreen.addstr(22,41,chr(188),curses.color_pair(3))
mainscreen.addstr(23,0,splash[r.randrange(len(splash))],curses.color_pair(2))
for indx,string in enumerate(prginstString):mainscreen.addstr(indx+1,42,string,curses.color_pair(2))
printPaletteType()
update()
mainscreen.addstr(1+cursor[1],cursor[0],chr(190),curses.color_pair(4))
mainscreen.refresh()

keycmd=mainscreen.getch()
while keycmd!=0:
	if keycmd in (ord('w'),ord('W')):
		cursor[1]-=1
		border()
		update()
		mainscreen.addstr(1+cursor[1],cursor[0],chr(190),curses.color_pair(4))
	elif keycmd in (ord('s'),ord('S')):
		cursor[1]+=1
		border()
		update()
		mainscreen.addstr(1+cursor[1],cursor[0],chr(190),curses.color_pair(4))
	elif keycmd in (ord('a'),ord('A')):
		cursor[0]-=1
		border()
		update()
		mainscreen.addstr(1+cursor[1],cursor[0],chr(190),curses.color_pair(4))
	elif keycmd in (ord('d'),ord('D')):
		cursor[0]+=1
		border()
		update()
		mainscreen.addstr(1+cursor[1],cursor[0],chr(190),curses.color_pair(4))
	elif keycmd in (ord('l'),ord('L')):
		px[(cursor[0]-1)+(cursor[1]-1)*40]=color
		update()
		mainscreen.addstr(1+cursor[1],cursor[0],chr(190),curses.color_pair(4))
	elif keycmd==ord('1'):
		if isdarkpalette:color=u_color[0]
		else:color=u_color[8]
	elif keycmd==ord('2'):
		if isdarkpalette:color=u_color[1]
		else:color=u_color[9]
	elif keycmd==ord('3'):
		if isdarkpalette:color=u_color[2]
		else:color=u_color[10]
	elif keycmd==ord('4'):
		if isdarkpalette:color=u_color[3]
		else:color=u_color[11]
	elif keycmd==ord('5'):
		if isdarkpalette:color=u_color[4]
		else:color=u_color[12]
	elif keycmd==ord('6'):
		if isdarkpalette:color=u_color[5]
		else:color=u_color[13]
	elif keycmd==ord('7'):
		if isdarkpalette:color=u_color[6]
		else:color=u_color[14]
	elif keycmd==ord('8'):
		if isdarkpalette:color=u_color[7]
		else:color=u_color[15]
	elif keycmd==ord('9'):
		if isdarkpalette:
			isdarkpalette=False
			printPaletteType()
		else:
			isdarkpalette=True
			printPaletteType()
	elif keycmd==ord('!'):
		if isdarkpalette:
			for i in range(800):
				px[i]=u_color[0]
		else:
			for i in range(800):
				px[i]=u_color[8]
		update()
		mainscreen.addstr(1+cursor[1],cursor[0],chr(190),curses.color_pair(4))
	elif keycmd==ord('@'):
		if isdarkpalette:
			for i in range(800):
				px[i]=u_color[1]
		else:
			for i in range(800):
				px[i]=u_color[9]
		update()
		mainscreen.addstr(1+cursor[1],cursor[0],chr(190),curses.color_pair(4))
	elif keycmd==ord('#'):
		if isdarkpalette:
			for i in range(800):
				px[i]=u_color[2]
		else:
			for i in range(800):
				px[i]=u_color[10]
		update()
		mainscreen.addstr(1+cursor[1],cursor[0],chr(190),curses.color_pair(4))
	elif keycmd==ord('$'):
		if isdarkpalette:
			for i in range(800):
				px[i]=u_color[3]
		else:
			for i in range(800):
				px[i]=u_color[11]
		update()
		mainscreen.addstr(1+cursor[1],cursor[0],chr(190),curses.color_pair(4))
	elif keycmd==ord('%'):
		if isdarkpalette:
			for i in range(800):
				px[i]=u_color[4]
		else:
			for i in range(800):
				px[i]=u_color[12]
		update()
		mainscreen.addstr(1+cursor[1],cursor[0],chr(190),curses.color_pair(4))
	elif keycmd==ord('^'):
		if isdarkpalette:
			for i in range(800):
				px[i]=u_color[5]
		else:
			for i in range(800):
				px[i]=u_color[13]
		update()
		mainscreen.addstr(1+cursor[1],cursor[0],chr(190),curses.color_pair(4))
	elif keycmd==ord('&'):
		if isdarkpalette:
			for i in range(800):
				px[i]=u_color[6]
		else:
			for i in range(800):
				px[i]=u_color[14]
		update()
		mainscreen.addstr(1+cursor[1],cursor[0],chr(190),curses.color_pair(4))
	elif keycmd==ord('*'):
		if isdarkpalette:
			for i in range(800):
				px[i]=u_color[7]
		else:
			for i in range(800):
				px[i]=u_color[15]
		update()
		mainscreen.addstr(1+cursor[1],cursor[0],chr(190),curses.color_pair(4))
	elif keycmd==ord('['):
		curses.endwin()
		print("IZANAGI - Ver 2.1\nSAVE AS...")
		try:
			filename=input("File name: ")
			with open(f"{filename}.pxpy","w") as f:f.write("".join(px));time.sleep(0.8)
			print("File successfully saved!\nPress ENTER to go back to the main screen.")
		except OSError:
			print("ERROR - ILLEGAL FILE NAME")
		input()
		curses.initscr()
		update()
		mainscreen.refresh()
	elif keycmd==ord(']'):
		curses.endwin()
		print("IZANAGI - Ver 2.1\nLOAD...")
		try:
			filename=input("File name: ")
			with open(f"{filename}.pxpy","r") as f:
				for i,j in enumerate(f.read()):
					px[i]=j;time.sleep(0.008)
			print("File successfully loaded!\nPress ENTER to go back to the main screen.")
		except FileNotFoundError:
			print("ERROR - NO FILE FOUND")
		except OSError:
			print("ERROR - ILLEGAL FILE NAME")
		input()
		curses.initscr()
		update()
		mainscreen.refresh()
	elif keycmd==ord('+'):
		break
	mainscreen.refresh()
	keycmd=mainscreen.getch()

curses.endwin()
print("Exiting IZANAGI...\n\n\n\n\n\n(C)2021 Katsumi Kougen. All rights reserved.")
time.sleep(2)
