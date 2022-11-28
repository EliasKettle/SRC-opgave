import arcade
import math

BREDDE = 1250
HOEJDE = 650
SPORLAENGDE = 250




def ellipse(tid, centrum, radius, vinkelhastighed, fase=0):
    x_c, y_c = centrum
    x = x_c + radius * math.cos(vinkelhastighed * tid + fase+500)
    y = y_c + radius * math.sin(vinkelhastighed * tid + fase)
    return x, y

def tegn_baner(delta_tid):
    arcade.start_render()
    x, y = ellipse(tegn_baner.tid, (BREDDE / 2, HOEJDE / 2), 100, 1, 0)
    arcade.draw_circle_filled(625, 325, 50, arcade.color.YELLOW)
    arcade.draw_circle_filled(x, y, 5, arcade.color.BLUE)
    if len(tegn_baner.spor) > SPORLAENGDE:
        tegn_baner.spor.pop(0)
    for punkt in tegn_baner.spor:
        arcade.draw_circle_filled(*punkt, 2, arcade.csscolor.RED)
    tegn_baner.tid += delta_tid
    tegn_baner.spor.append((x, y))

def main():
    arcade.open_window(BREDDE, HOEJDE, "her")
    arcade.set_background_color(arcade.csscolor.BLACK)

    tegn_baner.tid = 0.0
    tegn_baner.spor = list()
    arcade.schedule(tegn_baner, 1 / 60)

    arcade.run()

main()
