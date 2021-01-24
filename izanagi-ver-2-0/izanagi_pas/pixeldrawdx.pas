program PixelDrawDX;
uses crt,keyboard;
type attrPixel=array[1..40,1..20] of char;
var
	x,y{pixel coordinate},cx,cy{cursor coordinate}:integer;
	color:char;
	canvasUpdatePermission,PaletteStatus:boolean;
	fileName:string[32];
	pxdx_directory:string;
	pixel:attrPixel;
	savedFile:text;
	fileLoad:file of char;
	menuKey,actionKey:tKeyEvent;
label
	cvRefresh,setCursor,inputKey,checkCoordinate,checkPalette,SaveCanvas,LoadCanvas,pxdxfileRead,done_fileRead;
// ####              #     #               #           #
// #   #             #     #               #           #     *
// #   #  ###  #   # ####  #  ###         # #   ###  ##### ###    ###  ####
// #   # #   # #   # #   # # #   #        # #  #   #   #     #   #   # #   #
// #   # #   # #   # #   # # ##### #####  ###  #       #     #   #   # #   #
// #   # #   # #   # #   # # #           #   # #   #   # #   #   #   # #   #
// ####   ###   #### ####  #  ###        #   #  ###     #  #####  ###  #   #
// WriteLn(' // Pascal Form // ');
// dedicated to Eggplant Kouhai - Mashu Kyrielight
procedure gotoPixel(x,y:byte);
begin
	gotoxy(x+1,y+1);
end;
procedure Update;
begin
	if canvasUpdatePermission=false then
		begin
			textAttr:=$9f;clrscr; {Draw the screen}
			gotoxy(1,1);write(chr(218));for x:=1 to 40 do write(chr(196));write(chr(191));
			for x:=1 to 20 do
				begin
					gotoxy(1,1+x);write(chr(179));for y:=1 to 40 do write(' ');write(chr(179));
				end;
			gotoxy(1,22);write(chr(192));for x:=1 to 40 do write(chr(196));write(chr(217));
			gotoxy(2,2);textAttr:=$00;
			for y:=1 to 20 do
				begin
					gotoxy(2,y+1);for x:=1 to 40 do write(' ');
				end;
			textAttr:=$9e;gotoxy(43,1); {Write the instructions}
			write('IZANAGI / PIXELDRAW DX 2.1');
			gotoxy(43,2);write('Arrow keys / WASD - Move');
			gotoxy(43,3);write('SPACE / L - Draw');
			gotoxy(43,4);write('1 --> 8 - Choose color');
			gotoxy(43,5);write('SHIFT + 1 --> 8 - Fill canvas');
			gotoxy(43,6);write('TAB - Toggle palette');
			gotoxy(43,7);write('F1 - Save / F2 - Load');
			gotoxy(43,8);write('F3 - Exit');
			textAttr:=$9f;
			gotoxy(43,9);write('1: BLACK - DGRAY');
			gotoxy(43,10);write('2: DBLUE - BLUE');
			gotoxy(43,11);write('3: DGREEN - GREEN');
			gotoxy(43,12);write('4: DCYAN - CYAN');
			gotoxy(43,13);write('5: DRED - RED');
			gotoxy(43,14);write('6: PURPLE - PINK');
			gotoxy(43,15);write('7: BROWN - YELLOW');
			gotoxy(43,16);write('8: GRAY - WHITE');
			textAttr:=$9e;
			gotoxy(43,22);write('Palette: DARK')
		end
		else
			begin
				for y:=1 to 20 do
					begin
						for x:=1 to 40 do
							begin
								if pixel[x,y]='0' then
									begin
										gotoPixel(x,y);textAttr:=$00;write(chr(219));
									end;
								if pixel[x,y]='1' then
									begin
										gotoPixel(x,y);textAttr:=$01;write(chr(219));
									end;
								if pixel[x,y]='2' then
									begin
										gotoPixel(x,y);textAttr:=$02;write(chr(219));
									end;
								if pixel[x,y]='3' then
									begin
										gotoPixel(x,y);textAttr:=$03;write(chr(219));
									end;
								if pixel[x,y]='4' then
									begin
										gotoPixel(x,y);textAttr:=$04;write(chr(219));
									end;
								if pixel[x,y]='5' then
									begin
										gotoPixel(x,y);textAttr:=$05;write(chr(219));
									end;
								if pixel[x,y]='6' then
									begin
										gotoPixel(x,y);textAttr:=$06;write(chr(219));
									end;
								if pixel[x,y]='7' then
									begin
										gotoPixel(x,y);textAttr:=$07;write(chr(219));
									end;
								if pixel[x,y]='8' then
									begin
										gotoPixel(x,y);textAttr:=$08;write(chr(219));
									end;
								if pixel[x,y]='9' then
									begin
										gotoPixel(x,y);textAttr:=$09;write(chr(219));
									end;
								if pixel[x,y]='a' then
									begin
										gotoPixel(x,y);textAttr:=$0a;write(chr(219));
									end;
								if pixel[x,y]='b' then
									begin
										gotoPixel(x,y);textAttr:=$0b;write(chr(219));
									end;
								if pixel[x,y]='c' then
									begin
										gotoPixel(x,y);textAttr:=$0c;write(chr(219));
									end;
								if pixel[x,y]='d' then
									begin
										gotoPixel(x,y);textAttr:=$0d;write(chr(219));
									end;
								if pixel[x,y]='e' then
									begin
										gotoPixel(x,y);textAttr:=$0e;write(chr(219));
									end;
								if pixel[x,y]='f' then
									begin
										gotoPixel(x,y);textAttr:=$0f;write(chr(219));
									end;

							end;
					end;
			end;
end;
begin
	textAttr:=$0a;clrscr;randomize;
	gotoxy(2,1);write('Loading...');
	gotoxy(2,2);textAttr:=$07;
	write(chr(218));for x:=1 to 76 do write(chr(196));write(chr(191));
	gotoxy(2,3);write(chr(179));for x:=1 to 76 do write(' ');write(chr(179));
	gotoxy(2,4);write(chr(192));for x:=1 to 76 do write(chr(196));write(chr(217));
	gotoxy(3,3);textAttr:=$02;for x:=1 to 76 do write('|');gotoxy(2,5);
	textAttr:=$0f;writeln('Copyright 2020-2021 Katsumi Kogen. All rights reserved.');write(' https://github.com/KatsumiKougen');
	textAttr:=$ec;gotoxy(3,3);
	for x:=1 to 76 do
 	begin
		delay(random(101));write(chr(4));
  	end;
	gotoxy(2,7);textAttr:=$0f;write('Complete. Press any key to continue');readkey;
	canvasUpdatePermission:=false;cx:=1;cy:=1;PaletteStatus:=false;Update;
	for y:=1 to 20 do
		begin
			for x:=1 to 40 do pixel[x,y]:='0';
		end;
	canvasUpdatePermission:=true;Update;
	checkPalette:
	textAttr:=$9e;
	if PaletteStatus=false then
		begin
			gotoxy(43,22);write('                ');
			gotoxy(43,22);write('Palette: DARK');
		end
	else
		begin
			gotoxy(43,22);write('                 ');
			gotoxy(43,22);write('Palette: LIGHT');
		end;
	goto setCursor;
	setCursor:
	textAttr:=$7f;gotoPixel(cx,cy);write(chr(230));goto inputKey;
	inputKey:
	initKeyboard;
	actionKey:=getKeyEvent;actionKey:=translateKeyEvent(actionKey);
	case tKeyRecord(actionKey).keycode of
	//WASD - Arrow keys
		65315,7777:
			begin
				cx:=cx-1;goto checkCoordinate;
			end;
		65317,8292:
			begin
				cx:=cx+1;goto checkCoordinate;
			end;
		65313,4471:
			begin
				cy:=cy-1;goto checkCoordinate;
			end;
		65319,8051:
			begin
				cy:=cy+1;goto checkCoordinate;
			end;
	//Draw command
		14624,9836:
			begin
				pixel[cx,cy]:=color;Update;goto setCursor;
			end;
	//Toggle palette
		3849:
			begin
				if PaletteStatus=false then PaletteStatus:=true else PaletteStatus:=false;
				goto checkPalette;
			end;
	//Choose color
		561:
			begin
				if PaletteStatus=false then color:='0';
				if PaletteStatus=true then color:='8';
				goto inputKey;
			end;
		818:
			begin
				if PaletteStatus=false then color:='1';
				if PaletteStatus=true then color:='9';
				goto inputKey;
			end;
		1075:
			begin
				if PaletteStatus=false then color:='2';
				if PaletteStatus=true then color:='a';
				goto inputKey;
			end;
		1332:
			begin
				if PaletteStatus=false then color:='3';
				if PaletteStatus=true then color:='b';
				goto inputKey;
			end;
		1589:
			begin
				if PaletteStatus=false then color:='4';
				if PaletteStatus=true then color:='c';
				goto inputKey;
			end;
		1846:
			begin
				if PaletteStatus=false then color:='5';
				if PaletteStatus=true then color:='d';
				goto inputKey;
			end;
		2103:
			begin
				if PaletteStatus=false then color:='6';
				if PaletteStatus=true then color:='e';
				goto inputKey;
			end;
		2360:
			begin
				if PaletteStatus=false then color:='7';
				if PaletteStatus=true then color:='f';
				goto inputKey;
			end;
	//Fill procedure
		545:
			begin
				if PaletteStatus=false then color:='0' else color:='8';
				for y:=1 to 20 do
					begin
						for x:=1 to 40 do pixel[x,y]:=color;
					end;
				Update;goto inputKey;
			end;
		832:
			begin
				if PaletteStatus=false then color:='1' else color:='9';
				for y:=1 to 20 do
					begin
						for x:=1 to 40 do pixel[x,y]:=color;
					end;
				Update;goto inputKey;
			end;
		1059:
			begin
				if PaletteStatus=false then color:='2' else color:='a';
				for y:=1 to 20 do
					begin
						for x:=1 to 40 do pixel[x,y]:=color;
					end;
				Update;goto inputKey;
			end;
		1316:
			begin
				if PaletteStatus=false then color:='3' else color:='b';
				for y:=1 to 20 do
					begin
						for x:=1 to 40 do pixel[x,y]:=color;
					end;
				Update;goto inputKey;
			end;
		1573:
			begin
				if PaletteStatus=false then color:='4' else color:='c';
				for y:=1 to 20 do
					begin
						for x:=1 to 40 do pixel[x,y]:=color;
					end;
				Update;goto inputKey;
			end;
		1886:
			begin
				if PaletteStatus=false then color:='5' else color:='d';
				for y:=1 to 20 do
					begin
						for x:=1 to 40 do pixel[x,y]:=color;
					end;
				Update;goto inputKey;
			end;
		2086:
			begin
				if PaletteStatus=false then color:='6' else color:='e';
				for y:=1 to 20 do
					begin
						for x:=1 to 40 do pixel[x,y]:=color;
					end;
				Update;goto inputKey;
			end;
		2346:
			begin
				if PaletteStatus=false then color:='7' else color:='f';
				for y:=1 to 20 do
					begin
						for x:=1 to 40 do pixel[x,y]:=color;
					end;
				Update;goto inputKey;
			end;
		65281: goto SaveCanvas;
		65282: goto LoadCanvas;
		65283: halt(0)
		else goto inputKey;
	end;
	checkCoordinate:
	if cx<1 then
		begin
			cx:=cx+1;goto inputKey;
		end;
	if cx>40 then
		begin
			cx:=cx-1;goto inputKey;
		end;
	if cy<1 then
		begin
			cy:=cy+1;goto inputKey;
		end;
	if cy>20 then
		begin
			cy:=cy-1;goto inputKey;
		end;
	Update;goto setCursor;
SaveCanvas:
	doneKeyboard;
	textAttr:=$9e;clrscr;
	gotoxy(1,1);writeln('Enter the file name, then press ENTER.');
	textAttr:=$0f;readln(fileName);
	textAttr:=$9e;writeln('Hold on...');delay(random(1001));
	assign(savedFile,fileName+'.pec');
	rewrite(savedFile);
	for y:=1 to 20 do
		begin
			for x:=1 to 40 do write(savedFile,pixel[x,y]);
		end;
	close(savedFile);
	textAttr:=$be;writeln('Saving file "',fileName,'"...');
	writeln('Complete. Press any key...');readkey;fileName:='';canvasUpdatePermission:=false;cx:=1;cy:=1;PaletteStatus:=false;
	Update;goto inputKey;
LoadCanvas:
	doneKeyboard;cx:=1;cy:=1;PaletteStatus:=false;
	textAttr:=$9e;
	gotoxy(1,23);write('Enter the file name, then press ENTER.');
	textAttr:=$0f;read(fileName);
	gotoxy(1,23);textAttr:=$9e;for x:=1 to 60 do write(' ');
	textAttr:=$9e;gotoxy(1,23);writeln('Hold on...');delay(random(5001));textAttr:=$9e;gotoxy(1,23);for x:=1 to 60 do write(' ');delay(500);
	assign(fileLoad,fileName+'.pec');
	reset(fileLoad);
	repeat
		for y:=1 to 20 do
			begin
				for x:=1 to 40 do read(fileLoad,pixel[x,y]);
			end;
	until eof(fileLoad);
	close(fileLoad);
	fileName:='';
	Update;goto setCursor;
end.
