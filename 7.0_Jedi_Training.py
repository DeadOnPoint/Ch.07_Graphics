#Sign your name:Will Jacobson

'''
Recreate, exactly the Test Picture from the website. The arcade colors used in this picture in no particular order are:
BLACK, ALMOND, PHLOX, BLUSH, RED, BLUE, WISTERIA, AMBER, BRICK_RED and YELLOW.
The picture is 500px wide and 400px tall. Look up ARC in the documentation to do the PAC-MAN.
'''

import arcade

SW = 500
SH = 400

arcade.open_window(SW,SH, "Ch. 7 Jedi Training")
arcade.set_background_color(arcade.color.ALMOND)
arcade.start_render()
for x in range(0,SW+1,20): #horizontal lines
    arcade.draw_line(0,x,SW,x,arcade.color.BLACK,2)
for y in range(0,SW+1,20): #vertical lines
    arcade.draw_line(y,0,y,SH,arcade.color.BLACK,2)
arcade.draw_rectangle_filled(50,SH-30,60,20,arcade.color.PHLOX) #upper left rectangle
arcade.draw_line(80,20,120,60,arcade.color.BLUE) #line
arcade.draw_rectangle_filled(200,260,40,20,arcade.color.BLUSH,-45) #tilted rectangle
arcade.draw_circle_filled(250,200,40,arcade.color.WISTERIA) #circle
arcade.draw_ellipse_filled(100,100,120,40,arcade.color.AMBER) #ellipse
arcade.draw_text("I love you. I know.",20,155,arcade.color.BRICK_RED,20) #I love you text
arcade.draw_point(SW-40,10,arcade.color.RED,5) #dot
arcade.draw_arc_filled(400,320,120,120,arcade.color.YELLOW,30,330) #pacman
arcade.finish_render()
arcade.run()