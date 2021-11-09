'''
FLAG PROJECT
---------------
Make your flag 260 pixels tall
Use the scaling image on the website to determine other dimensions
The hexadecimal colors for the official flag are red:#BF0A30 and blue:#002868
Title the window, "The Stars and Stripes"
I used a draw_text command and used 20 pt. asterisks for the stars.
We will have a competition to see who can make this flag in the least lines of code.
The record is 16! You will have to use some loops to achieve this.
'''

import arcade
import math

FH = 260
FW = FH*1.9

arcade.open_window(FW,FH,"Flag of 'Merica")
arcade.set_background_color(arcade.color.WHITE)
arcade.start_render()
for y in range(10,int(FW+1),int(FH/13*2)): #red stripes
    arcade.draw_rectangle_filled(FW/2,y,FW,FH/13,(191,10,48))
arcade.draw_lrtb_rectangle_filled(0,FH*0.76,FW,FH*(6/13),(0,40,104)) #blue union
for i in range(50):
    if i <= 5:
        FY = FH - FH * .054
        FX = FH * .063 + i * (2 * FH * .063)
    elif i > 5 and i <= 10:
        FY = FH - 2 * FH * .054
        FX = 2 * FH * .063 + (i - 6) * (2 * FH * .063)
    elif i > 10 and i <= 16:
        FY = FH - 3 * FH * .054
        FX = FH * .063 + (i - 11) * (2 * FH * .063)
    elif i > 16 and i <= 21:
        FY = FH - 4 * FH * .054
        FX = 2 * FH * .063 + (i - 17) * (2 * FH * .063)
    elif i > 21 and i <= 27:
        FY = FH - 5 * FH * .054
        FX = FH * .063 + (i - 22) * (2 * FH * .063)
    elif i > 27 and i <= 32:
        FY = FH - 6 * FH * .054
        FX = 2 * FH * .063 + (i - 28) * (2 * FH * .063)
    elif i > 32 and i <= 38:
        FY = FH - 7 * FH * .054
        FX = FH * .063 + (i - 33) * (2 * FH * .063)
    elif i > 38 and i <= 43:
        FY = FH - 8 * FH * .054
        FX = 2 * FH * .063 + (i - 39) * (2 * FH * .063)
    else:
        FY = FH - 9 * FH * .054
        FX = FH * .063 + (i - 44) * (2 * FH * .063)
    arcade.draw_polygon_filled([
        [(FH * .0616) / 6 * math.cos(math.radians(54)) + FX, (FH * .0616) / 6 * math.sin(math.radians(54)) + FY],
        [FH * .0616 / 2 * math.cos(math.radians(90)) + FX, FH * .0616 / 2 * math.sin(math.radians(90)) + FY],
        [(FH * .0616) / 6 * math.cos(math.radians(126)) + FX, (FH * .0616) / 6 * math.sin(math.radians(126)) + FY],
        [FH * .0616 / 2 * math.cos(math.radians(162)) + FX, FH * .0616 / 2 * math.sin(math.radians(162)) + FY],
        [(FH * .0616) / 6 * math.cos(math.radians(198)) + FX, (FH * .0616) / 6 * math.sin(math.radians(198)) + FY],
        [FH * .0616 / 2 * math.cos(math.radians(234)) + FX, FH * .0616 / 2 * math.sin(math.radians(234)) + FY],
        [(FH * .0616) / 6 * math.cos(math.radians(270)) + FX, (FH * .0616) / 6 * math.sin(math.radians(270)) + FY],
        [FH * .0616 / 2 * math.cos(math.radians(306)) + FX, FH * .0616 / 2 * math.sin(math.radians(306)) + FY],
        [(FH * .0616) / 6 * math.cos(math.radians(342)) + FX, (FH * .0616) / 6 * math.sin(math.radians(342)) + FY],
        [FH * .0616 / 2 * math.cos(math.radians(18)) + FX, FH * .0616 / 2 * math.sin(math.radians(18)) + FY]
    ], arcade.color.WHITE)
arcade.finish_render()
arcade.run()