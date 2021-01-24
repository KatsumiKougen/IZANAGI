import curses,time,os
import random as ran

def border():
	if cursor[0]<1:
		cursor[0]+=1
	if cursor[0]>40:
		cursor[0]-=1
	if cursor[1]<1:
		cursor[1]+=1
	if cursor[1]>20:
		cursor[1]-=1

def update():
	for y in range(20):
		for x in range(40):
			if px[x+y*40]=="0":
				mainscreen.addstr(2+y,1+x," ",curses.color_pair(60))
			if px[x+y*40]=="1":
				mainscreen.addstr(2+y,1+x," ",curses.color_pair(61))
			if px[x+y*40]=="2":
				mainscreen.addstr(2+y,1+x," ",curses.color_pair(62))
			if px[x+y*40]=="3":
				mainscreen.addstr(2+y,1+x," ",curses.color_pair(63))
			if px[x+y*40]=="4":
				mainscreen.addstr(2+y,1+x," ",curses.color_pair(64))
			if px[x+y*40]=="5":
				mainscreen.addstr(2+y,1+x," ",curses.color_pair(65))
			if px[x+y*40]=="6":
				mainscreen.addstr(2+y,1+x," ",curses.color_pair(66))
			if px[x+y*40]=="7":
				mainscreen.addstr(2+y,1+x," ",curses.color_pair(67))
			if px[x+y*40]=="8":
				mainscreen.addstr(2+y,1+x," ",curses.color_pair(70))
			if px[x+y*40]=="9":
				mainscreen.addstr(2+y,1+x," ",curses.color_pair(71))
			if px[x+y*40]=="a":
				mainscreen.addstr(2+y,1+x," ",curses.color_pair(72))
			if px[x+y*40]=="b":
				mainscreen.addstr(2+y,1+x," ",curses.color_pair(73))
			if px[x+y*40]=="c":
				mainscreen.addstr(2+y,1+x," ",curses.color_pair(74))
			if px[x+y*40]=="d":
				mainscreen.addstr(2+y,1+x," ",curses.color_pair(75))
			if px[x+y*40]=="e":
				mainscreen.addstr(2+y,1+x," ",curses.color_pair(76))
			if px[x+y*40]=="f":
				mainscreen.addstr(2+y,1+x," ",curses.color_pair(77))

def palstt():
	if isdarkpalette==True:
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
"Now, count up your sins!"
]
program_inst=["INSTRUCTIONS",
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
"8 - WHITE",]
cursor=[1,1] #[x,y] - max x: 40, max y: 20
u_color=("0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f") #0-f
px=[]
color=u_color[0]
isdarkpalette=True
for i in range(800):
	px.append(color)

print("------- ATTENTION -------\n   Starting from Version 2.0, PIXELDRAW Project will forever be known as\nKatsumi's IZANAGI Project. Thank you for using PIXELDRAW.")
print("\n   What is new on Version 2.0?\n   I've added 16-colour support, so now it is possible to create artworks with\nfull 16 CGA colours. The program is backward compatible with 8-colour artworks.")
print("\n   That is all for now.\n        Best regards,\n                ~Katsumi Kogen~")
input("\n"*10+"PRESS [ENTER] TO CONTINUE.")
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

for y in range(24):
	for x in range(80):
		mainscreen.addstr(y,x," ",curses.color_pair(1))
mainscreen.addstr(0,0,"IZANAGI Ver 2.0 - (C)2021 Katsumi Kogen. All rights reserved.",curses.color_pair(3))
mainscreen.refresh()
curses.napms(10)
#draw canvas
mainscreen.addstr(1,0,chr(201),curses.color_pair(3))
for x in range(1,41):
	mainscreen.addstr(1,x,chr(205),curses.color_pair(3))
mainscreen.addstr(1,41,chr(187),curses.color_pair(3))
for y in range(2,22):
	mainscreen.addstr(y,0,chr(186),curses.color_pair(3))
	for x in range(1,41):
		mainscreen.addstr(y,x," ",curses.color_pair(60))
	mainscreen.addstr(y,41,chr(186),curses.color_pair(3))
mainscreen.addstr(22,0,chr(200),curses.color_pair(3))
for x in range(1,41):
	mainscreen.addstr(22,x,chr(205),curses.color_pair(3))
mainscreen.addstr(22,41,chr(188),curses.color_pair(3))
mainscreen.addstr(23,0,splash[ran.randrange(len(splash))],curses.color_pair(2))
for strindx in program_inst:
	mainscreen.addstr(program_inst.index(strindx)+1,42,strindx,curses.color_pair(2))
palstt()
mainscreen.refresh()
#update then set cursor
update()
mainscreen.addstr(1+cursor[1],cursor[0],chr(190),curses.color_pair(4))
mainscreen.refresh()

#
keycmd=mainscreen.getch()
while keycmd!=0:
	if keycmd==ord('w') or keycmd==ord('W'):#up
		cursor[1]-=1
		border()
		update()
		mainscreen.addstr(1+cursor[1],cursor[0],chr(190),curses.color_pair(4))
		mainscreen.refresh()
	elif keycmd==ord('s') or keycmd==ord('S'):#down
		cursor[1]+=1
		border()
		update()
		mainscreen.addstr(1+cursor[1],cursor[0],chr(190),curses.color_pair(4))
		mainscreen.refresh()
	elif keycmd==ord('a') or keycmd==ord('A'):#left
		cursor[0]-=1
		border()
		update()
		mainscreen.addstr(1+cursor[1],cursor[0],chr(190),curses.color_pair(4))
		mainscreen.refresh()
	elif keycmd==ord('d') or keycmd==ord('D'):#right
		cursor[0]+=1
		border()
		update()
		mainscreen.addstr(1+cursor[1],cursor[0],chr(190),curses.color_pair(4))
		mainscreen.refresh()
	elif keycmd==ord('l') or keycmd==ord('L'):#draw
		px[(cursor[0]-1)+(cursor[1]-1)*40]=color
		update()
		mainscreen.addstr(1+cursor[1],cursor[0],chr(190),curses.color_pair(4))
		mainscreen.refresh()
	elif keycmd==ord('1'):
		if isdarkpalette==True:
			color=u_color[0]
		else:
			color=u_color[8]
	elif keycmd==ord('2'):
		if isdarkpalette==True:
			color=u_color[1]
		else:
			color=u_color[9]
	elif keycmd==ord('3'):
		if isdarkpalette==True:
			color=u_color[2]
		else:
			color=u_color[10]
	elif keycmd==ord('4'):
		if isdarkpalette==True:
			color=u_color[3]
		else:
			color=u_color[11]
	elif keycmd==ord('5'):
		if isdarkpalette==True:
			color=u_color[4]
		else:
			color=u_color[12]
	elif keycmd==ord('6'):
		if isdarkpalette==True:
			color=u_color[5]
		else:
			color=u_color[13]
	elif keycmd==ord('7'):
		if isdarkpalette==True:
			color=u_color[6]
		else:
			color=u_color[14]
	elif keycmd==ord('8'):
		if isdarkpalette==True:
			color=u_color[7]
		else:
			color=u_color[15]
	elif keycmd==ord('9'):
		if isdarkpalette==True:
			isdarkpalette=False
			palstt()
		else:
			isdarkpalette=True
			palstt()
	elif keycmd==ord('!'):
		if isdarkpalette==True:
			for i in range(800):
				px[i]=u_color[0]
		else:
			for i in range(800):
				px[i]=u_color[8]
		update()
		mainscreen.addstr(1+cursor[1],cursor[0],chr(190),curses.color_pair(4))
		mainscreen.refresh()
	elif keycmd==ord('@'):
		if isdarkpalette==True:
			for i in range(800):
				px[i]=u_color[1]
		else:
			for i in range(800):
				px[i]=u_color[9]
		update()
		mainscreen.addstr(1+cursor[1],cursor[0],chr(190),curses.color_pair(4))
		mainscreen.refresh()
	elif keycmd==ord('#'):
		if isdarkpalette==True:
			for i in range(800):
				px[i]=u_color[2]
		else:
			for i in range(800):
				px[i]=u_color[10]
		update()
		mainscreen.addstr(1+cursor[1],cursor[0],chr(190),curses.color_pair(4))
		mainscreen.refresh()
	elif keycmd==ord('$'):
		if isdarkpalette==True:
			for i in range(800):
				px[i]=u_color[3]
		else:
			for i in range(800):
				px[i]=u_color[11]
		update()
		mainscreen.addstr(1+cursor[1],cursor[0],chr(190),curses.color_pair(4))
		mainscreen.refresh()
	elif keycmd==ord('%'):
		if isdarkpalette==True:
			for i in range(800):
				px[i]=u_color[4]
		else:
			for i in range(800):
				px[i]=u_color[12]
		update()
		mainscreen.addstr(1+cursor[1],cursor[0],chr(190),curses.color_pair(4))
		mainscreen.refresh()
	elif keycmd==ord('^'):
		if isdarkpalette==True:
			for i in range(800):
				px[i]=u_color[5]
		else:
			for i in range(800):
				px[i]=u_color[13]
		update()
		mainscreen.addstr(1+cursor[1],cursor[0],chr(190),curses.color_pair(4))
		mainscreen.refresh()
	elif keycmd==ord('&'):
		if isdarkpalette==True:
			for i in range(800):
				px[i]=u_color[6]
		else:
			for i in range(800):
				px[i]=u_color[14]
		update()
		mainscreen.addstr(1+cursor[1],cursor[0],chr(190),curses.color_pair(4))
		mainscreen.refresh()
	elif keycmd==ord('*'):
		if isdarkpalette==True:
			for i in range(800):
				px[i]=u_color[7]
		else:
			for i in range(800):
				px[i]=u_color[15]
		update()
		mainscreen.addstr(1+cursor[1],cursor[0],chr(190),curses.color_pair(4))
		mainscreen.refresh()
	elif keycmd==ord('['):
		curses.endwin()
		print("PIXELDRAW PYTHON - Ver 2.0\nSAVE AS...")
		time.sleep(0.01)
		file_name=input("File name: ")
		user_project=open(file_name+".pxpy","w")
		for i in range(800):
			user_project.write(px[i])
			time.sleep(0.001)
		user_project.close()
		print("File successfully saved!\nPress ENTER to go back to the main screen.")
		input()
		curses.initscr()
	elif keycmd==ord(']'):
		curses.endwin()
		print("PIXELDRAW PYTHON - Ver 2.0\nLOAD...")
		time.sleep(0.01)
		file_name=input("File name: ")
		try:
			user_project=open(file_name+".pxpy","r")
			px=[]
			for a in user_project.read():
				px.append(a)
				time.sleep(0.001)
			user_project.close()
			print("File successfully loaded!\nPress ENTER to go back to the main screen.")
			input()
		except FileNotFoundError:
			print("ERROR - NO FILE FOUND")
			input()
			curses.initscr()
			mainscreen.refresh()
		curses.initscr()
		update()
		mainscreen.refresh()
	elif keycmd==ord('+'):
		break
	keycmd=mainscreen.getch()

curses.endwin()
print("Exiting IZANAGI..."+"\n"*6+"(C)2021 Katsumi Kogen. All rights reserved.")
time.sleep(2)