import arcade
import math

BREDDE = 1250
HOEJDE = 650
SPORLAENGDE = 50



def ellipse(tid, centrum, a, b,vinkelhastighed, fase=0):
    x_c, y_c = centrum
    x = x_c + a * math.cos(vinkelhastighed * tid + fase)
    y = y_c + b * math.sin(vinkelhastighed * tid + fase)
    return x, y




def baner(delta_tid):
    arcade.start_render()
    x, y = ellipse(baner.tid, (BREDDE / 2, HOEJDE / 2), 70, 47, 2)
    x_2, y_2 = ellipse(baner.tid, (BREDDE / 2, HOEJDE / 2), 108.9, 107, 0.78)
    x_3, y_3 = ellipse(baner.tid, (BREDDE / 2, HOEJDE / 2), 152.1, 147.1, 0.48)
    x_4, y_4 = ellipse(baner.tid, (BREDDE / 2, HOEJDE / 2), 249, 206, 0.24)
    #Solen
    arcade.draw_circle_filled(625, 325, 26.927, arcade.color.YELLOW)
    #Merkur
    arcade.draw_circle_filled(x, y, 4.879, arcade.color.GRAY)
    #Venus
    arcade.draw_circle_filled(x_2, y_2, 12.104, arcade.color.ORANGE)
    #Jorden
    arcade.draw_circle_filled(x_3, y_3, 12.742, arcade.color.BLUE)
    #Mars
    arcade.draw_circle_filled(x_4, y_4, 6.787, arcade.color.RED)


    if len(baner.spor) > SPORLAENGDE:
        baner.spor.pop(0)

    if len(baner.spor2) > SPORLAENGDE:
        baner.spor2.pop(0)

    if len(baner.spor3) > SPORLAENGDE:
        baner.spor3.pop(0)

    if len(baner.spor4) > SPORLAENGDE:
        baner.spor4.pop(0)

    for punkt in baner.spor:
        arcade.draw_circle_filled(*punkt, 2, arcade.color.GRAY)
    for punkt in baner.spor2:
        arcade.draw_circle_filled(*punkt, 2, arcade.color.ORANGE)
    for punkt in baner.spor3:
        arcade.draw_circle_filled(*punkt, 2, arcade.color.BLUE)
    for punkt in baner.spor4:
        arcade.draw_circle_filled(*punkt, 2, arcade.color.RED)
    baner.tid += delta_tid
    baner.spor.append((x, y))
    baner.spor2.append((x_2, y_2))
    baner.spor3.append((x_3, y_3))
    baner.spor4.append((x_4, y_4))
def main():
    arcade.open_window(BREDDE, HOEJDE, "De indre planeter")
    arcade.set_background_color(arcade.csscolor.BLACK)

    baner.tid = 0.0
    baner.spor = list()
    baner.spor2 = list()
    baner.spor3 = list()
    baner.spor4 = list()
    arcade.schedule(baner, 1 / 60)

    arcade.run()

main()
