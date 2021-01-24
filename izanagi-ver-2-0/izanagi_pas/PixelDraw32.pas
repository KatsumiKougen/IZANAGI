program PixelDraw32;
uses crt,keyboard;
type varPixel2 = array[1..32,1..16] of boolean;
var i,e,x,y: integer;
    CX,CY: byte;
    pixel2: varPixel2;
	menukeyInput,OnScreenKey,OnScreenKey1,OnScreenKey2,OnScreenKey3: tKeyEvent;
label Monochrome,
	  {Labels for monochrome mode}
      setCanvas_P2,CanvasRefresh_P2,CanvasRefresh2_P2,DefaultCoordinate_P2,setCursor_P2,inputKeyCmd_P2,checkCoordinate_P2;
procedure gotoPixel(x,y: byte);
begin
 gotoxy(x+1,y+1);
end;
begin
 textbackground(0);clrscr;randomize;
 gotoxy(2,1);textcolor(10);write('Loading...');
 gotoxy(2,2);textcolor(7);
 write(chr(218));for i:=1 to 76 do write(chr(196));write(chr(191));
 gotoxy(2,3);write(chr(179));for i:=1 to 76 do write(' ');write(chr(179));
 gotoxy(2,4);write(chr(192));for i:=1 to 76 do write(chr(196));write(chr(217));
 gotoxy(3,3);textcolor(2);for i:=1 to 76 do write('|');gotoxy(2,5);
 textcolor(15);write('Copyright 2020 QTware Productions. All rights reserved.');
 textbackground(10);textcolor(10);gotoxy(3,3);
 for i:=1 to 76 do
  begin
   delay(random(501));write(chr(4));
  end;
 gotoxy(2,6);textbackground(0);textcolor(15);write('Complete. Press any key to continue');readkey;
 Monochrome:
 textbackground(9);clrscr; {Draw the screen}
 gotoxy(1,1);textcolor(15);write(chr(218));for i:=1 to 32 do write(chr(196));write(chr(191));
 for i:=1 to 16 do
  begin
   gotoxy(1,1+i);write(chr(179));for e:=1 to 32 do write(' ');write(chr(179));
  end;
 gotoxy(1,18);write(chr(192));for i:=1 to 32 do write(chr(196));write(chr(217));
 gotoxy(2,2);textbackground(0);
 for i:=1 to 16 do
  begin
   gotoxy(2,i+1);for e:=1 to 32 do write(' ');
  end;
 textbackground(9);gotoxy(35,1); {Write the instructions}
 textcolor(14);write('INSTRUCTIONS');
 gotoxy(35,2);write('Arrow keys / WASD - Move');
 gotoxy(35,3);write('SPACE, BKSP / K, L - Draw, delete');
 gotoxy(35,4);write('F1 - Invert');
 gotoxy(35,5);write('F2 - Clear canvas');
 gotoxy(35,6);write('F3 - Exit the program');
 goto CanvasRefresh_P2;
 setCanvas_P2:
 for y:=1 to 16 do
  begin
   for x:=1 to 32 do pixel2[x,y]:=false; {Set all registers to 0}
  end;
 goto Monochrome;
 CanvasRefresh_P2: {Check all registers of the pixels on-screen.}
 for y:=1 to 16 do
  begin
   for x:=1 to 32 do
    begin
	 if pixel2[x,y]=false then
	  begin 
	   gotoPixel(x,y);textcolor(0);write(chr(219)); {If there's a 0 in this pixel, draw a black block}
	  end;
	 if pixel2[x,y]=true then
	  begin
	   gotoPixel(x,y);textcolor(15);write(chr(219)); {If there's a 1 in this pixel, draw a white block}
	  end;
	end;
  end;
 goto DefaultCoordinate_P2;
 CanvasRefresh2_P2:
 for y:=1 to 16 do
  begin
   for x:=1 to 32 do
    begin
	 if pixel2[x,y]=false then
	  begin 
	   gotoPixel(x,y);textcolor(0);write(chr(219)); {If there's a 0 in this pixel, draw a black block}
	  end;
	 if pixel2[x,y]=true then
	  begin
	   gotoPixel(x,y);textcolor(15);write(chr(219)); {If there's a 1 in this pixel, draw a white block}
	  end;
	end;
  end;
 goto setCursor_P2;
 DefaultCoordinate_P2: {Set the default coordinate of the cursor: X=1, Y=1}
 CX:=1;CY:=1;
 goto setCursor_P2;
 setCursor_P2:
 textbackground(12);textcolor(15);
 gotoPixel(CX,CY);write(chr(245));goto inputKeyCmd_P2;
 inputKeyCmd_P2:initKeyboard;
 OnScreenKey:=GetKeyEvent;OnScreenKey:=TranslateKeyEvent(OnScreenKey);
 case tKeyRecord(OnScreenKey).keycode of
  65315,7777: begin
               CX:=CX-1;goto checkCoordinate_P2;
              end;
  65317,8292: begin
               CX:=CX+1;goto checkCoordinate_P2;
              end;
  65313,4471: begin
               CY:=CY-1;goto checkCoordinate_P2;
              end;
  65319,8051: begin
               CY:=CY+1;goto checkCoordinate_P2;
              end;
  14624,9579: begin
               pixel2[CX,CY]:=true; goto CanvasRefresh2_P2;
              end;
  3592,9836: begin
               pixel2[CX,CY]:=false; goto CanvasRefresh2_P2;
              end;
  65281: begin
          for y:=1 to 16 do
		   begin
		    for x:=1 to 32 do
			 if pixel2[x,y]=false then pixel2[x,y]:=true {Change the register of each pixel. For example: 0 -> 1 and vice-versa}
			 else pixel2[x,y]:=false;
		   end;
		  goto CanvasRefresh2_P2;
         end;
  65282: begin
          for y:=1 to 16 do
		   begin
		    for x:=1 to 32 do pixel2[x,y]:=false;
		   end;
		  goto CanvasRefresh2_P2;
         end;
  65283: halt(0)
  else goto inputKeyCmd_P2;
 end;
 doneKeyboard;
 checkCoordinate_P2:
 if CX<1 then
  begin
   CX:=CX+1;goto inputKeyCmd_P2;
  end;
 if CX>32 then
  begin
   CX:=CX-1;goto inputKeyCmd_P2;
  end;
 if CY<1 then
  begin
   CY:=CY+1;goto inputKeyCmd_P2;
  end;
 if CY>16 then
  begin
   CY:=CY-1;goto inputKeyCmd_P2;
  end;
 goto CanvasRefresh2_P2;
end.