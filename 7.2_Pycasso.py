'''
PYCASSO PROJECT
---------------
Your job is to make a cool picture.
You must use multiple colors.
You must have a coherent picture. No abstract art with random shapes.
You must use multiple types of graphic functions (e.g. circles, rectangles, lines, etc.)
Somewhere you must include a WHILE or FOR loop to create a repeating pattern.
Do not just redraw the same thing in the same location 10 times. 
You can contain multiple drawing commands in a loop, so you can draw multiple train cars for example.
Please use comments and blank lines to make it easy to follow your program. 
If you have 5 lines that draw a robot, group them together with blank lines above and below. 
Then add a comment at the top telling the reader what you are drawing.
IN THE WINDOW TITLE PLEASE PUT YOUR NAME.
When you are finished Pull Request your file to your instructor.
'''

import arcade

SW = 500
SH = 500

arcade.open_window(SW,SH,"Will Jacobson's Pycasso")
arcade.set_background_color(arcade.color.WHITE)
arcade.start_render()
#outter circle border
arcade.draw_circle_filled(SW/2,SH/2,200,(252, 181, 20))
arcade.draw_circle_filled(SW/2,SH/2,190,arcade.color.BLACK)
arcade.draw_circle_filled(SW/2,SH/2,160,arcade.color.WHITE)
#inner spokes
tilt = 0
for i in range(4):
    arcade.draw_rectangle_filled(SH/2,SH/2,320,40,arcade.color.BLACK,tilt)
    arcade.draw_rectangle_filled(SH/2,SH/2,320,20,(252, 181, 20),tilt)
    tilt = tilt + 45
#the B
#big B
arcade.draw_polygon_filled([[SW * 0.30 + 20,SH * 0.70],[SW * 0.30 + 20,(SH * 0.70) - 35],[SW * 0.40,SH * 0.58],[SW * 0.40,SH * 0.42],[SW * 0.3 + 20,SH * 0.30 + 30],[SW * 0.3 + 20,SH * 0.3],
                            [SW * 0.6,SH * 0.3],[SW * 0.7,(SH * 0.3) + 30],[SW * 0.7,SH * 0.46],[SW * 0.6,SH * 0.5],[SW * 0.7, SH * 0.54],[SW * 0.70,(SH * 0.70) - 30],[SW * 0.60,SH * 0.70]],arcade.color.BLACK)
#med B
arcade.draw_polygon_filled([[SW * 0.30 + 25,SH * 0.70 - 5],[SW * 0.30 + 25,(SH * 0.70) - 33],[SW * 0.40 + 7,SH * 0.58],[SW * 0.40 + 5,SH * 0.42],[SW * 0.3 + 25,SH * 0.30 + 30],[SW * 0.3 + 25,SH * 0.3 + 5],
                            [SW * 0.6 - 5,SH * 0.3 + 5],[SW * 0.7 - 7,(SH * 0.3) + 30],[SW * 0.7 - 7,SH * 0.46 - 5],[SW * 0.6 - 5,SH * 0.5],[SW * 0.7 - 7, SH * 0.54],[SW * 0.70 - 7,(SH * 0.70) - 30],[SW * 0.60,SH * 0.70 - 5]],(252, 181, 20))
#small B
arcade.draw_polygon_filled([[SW * 0.30 + 30,SH * 0.70 - 10],[SW * 0.30 + 30,(SH * 0.70) - 31],[SW * 0.40 + 14,SH * 0.58],[SW * 0.40 + 10,SH * 0.42],[SW * 0.3 + 30,SH * 0.30 + 30],[SW * 0.3 + 30,SH * 0.3 + 10],
                            [SW * 0.6 - 10,SH * 0.3 + 10],[SW * 0.7 - 14,(SH * 0.3) + 30],[SW * 0.7 - 14,SH * 0.46 - 10],[SW * 0.6 - 10,SH * 0.5],[SW * 0.7 - 14, SH * 0.54],[SW * 0.70 - 14,(SH * 0.70) - 30],[SW * 0.60,SH * 0.70 - 10]],arcade.color.BLACK)
arcade.finish_render()
arcade.run()