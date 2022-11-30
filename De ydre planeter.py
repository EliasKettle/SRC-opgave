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

def cirkel_linje(tid, centrum, radius, vinkelhastighed, fase=0):
    x_c, y_c = centrum
    x = x_c + radius * math.cos(vinkelhastighed * tid + fase)
    y = y_c + radius * math.sin(vinkelhastighed * tid + fase)
    return x, y



def baner(delta_tid):
    arcade.start_render()
    x, y = ellipse(baner.tid, (BREDDE / 2, HOEJDE / 2), 74.1, 81.7, 3)
    x_2, y_2 = ellipse(baner.tid, (BREDDE / 2, HOEJDE / 2), 140, 150, 1.2)
    x_3, y_3 = ellipse(baner.tid, (BREDDE / 2, HOEJDE / 2), 300.639, 273.556, 0.42)
    x_4, y_4 = ellipse(baner.tid, (BREDDE / 2, HOEJDE / 2), 453.687, 445.963, 0.21)
    #Rotation i Jupiter
    x_5, y_5 = cirkel_linje(baner.tid, (x, y), 13.982, 30925.93, 0)
    #Rotation i Saturn
    x_6, y_6 = cirkel_linje(baner.tid, (x_2, y_2), 11.646, 28049.14, 0)
    #Rotation i Uranus
    x_7, y_7 = cirkel_linje(baner.tid, (x_3, y_3), 5.724, -18136.9, 0)
    #Rotation i Neptun
    x_8, y_8 = cirkel_linje(baner.tid, (x_4, y_4), 4.9244, 19138.11)
    #Solen
    arcade.draw_circle_filled(625, 325, 27.854, arcade.color.YELLOW)
    #Saturns ringe
    arcade.draw_circle_outline(x_2, y_2, 15, arcade.color.NAVAJO_WHITE, 1.82)
    #Jupiter
    arcade.draw_circle_filled(x, y, 13.982, arcade.color.WHITE)
    #Radius i Jupiter
    arcade.draw_line(x_5, y_5, x, y, arcade.color.RED)
    #Saturn
    arcade.draw_circle_filled(x_2, y_2, 11.646, arcade.color.BURLYWOOD)
    #Radius i Saturn
    arcade.draw_line(x_6, y_6, x_2, y_2, arcade.color.RED)
    #Uranus
    arcade.draw_circle_filled(x_3, y_3, 5.724, arcade.color.LIGHT_BLUE)
    #Radius i Uranus
    arcade.draw_line(x_7, y_7, x_3+5.724, y_3-5.724, arcade.color.RED)
    #Neptune
    arcade.draw_circle_filled(x_4, y_4, 4.9244, arcade.color.DODGER_BLUE)
    #Radius i Neptune
    arcade.draw_line(x_8, y_8, x_4, y_4, arcade.color.RED)


    if len(baner.spor) > SPORLAENGDE:
        baner.spor.pop(0)

    if len(baner.spor2) > SPORLAENGDE:
        baner.spor2.pop(0)

    if len(baner.spor3) > SPORLAENGDE:
        baner.spor3.pop(0)

    if len(baner.spor4) > SPORLAENGDE:
        baner.spor4.pop(0)

    for punkt in baner.spor:
        arcade.draw_circle_filled(*punkt, 2, arcade.color.WHITE)
    for punkt in baner.spor2:
        arcade.draw_circle_filled(*punkt, 2, arcade.color.BURLYWOOD)
    for punkt in baner.spor3:
        arcade.draw_circle_filled(*punkt, 2, arcade.color.LIGHT_BLUE)
    for punkt in baner.spor4:
        arcade.draw_circle_filled(*punkt, 2, arcade.color.DODGER_BLUE)
    baner.tid += delta_tid
    baner.spor.append((x, y))
    baner.spor2.append((x_2, y_2))
    baner.spor3.append((x_3, y_3))
    baner.spor4.append((x_4, y_4))
def main():
    arcade.open_window(BREDDE, HOEJDE, "De ydre planeter")
    arcade.set_background_color(arcade.csscolor.BLACK)

    baner.tid = 0.0
    baner.spor = list()
    baner.spor2 = list()
    baner.spor3 = list()
    baner.spor4 = list()
    arcade.schedule(baner, 1 / 60)

    arcade.run()

main()