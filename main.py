import arcade
#import math

BREDDE = 1200
HOEJDE = 650


arcade.open_window(BREDDE, HOEJDE, "her")
arcade.set_background_color(arcade.csscolor.BLACK)

arcade.start_render()
arcade.draw_circle_filled(42, 325, 50, arcade.color.YELLOW)
arcade.finish_render()
arcade.run()

