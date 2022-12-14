import arcade
import math

BREDDE = 1250
HOEJDE = 650
SPORLAENGDE = 50



def ellipse(tid, centrum, a, b, vinkelhastighed, fase=0):
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
    #Baner om solen bliver udregnet
    x, y = ellipse(baner.tid, (BREDDE / 2, HOEJDE / 2), 97.854, 74.854, 2)
    x_2, y_2 = ellipse(baner.tid, (BREDDE / 2, HOEJDE / 2), 135.854, 134.854, 0.78)
    x_3, y_3 = ellipse(baner.tid, (BREDDE / 2, HOEJDE / 2), 179.954, 174.954, 0.48)
    x_4, y_4 = ellipse(baner.tid, (BREDDE / 2, HOEJDE / 2), 276.854, 233.854, 0.24)
    #Rotation i Merkur
    x_5, y_5 = cirkel_linje(baner.tid, (x, y), 4.878, 3, 0)
    #Rotation i Venus
    x_6, y_6 = cirkel_linje(baner.tid, (x_2, y_2), 12.104, -0.72, 0)
    #Rotaion i Jorden
    x_7, y_7 = cirkel_linje(baner.tid, (x_3, y_3), 12.742, 175.2, 0)
    #Rotation i Mars
    x_8, y_8 = cirkel_linje(baner.tid, (x_4, y_4), 6.787, 109.92, 0)
    #Solen
    arcade.draw_circle_filled(625, 325, 27.854, arcade.color.YELLOW)
    #Merkur
    arcade.draw_circle_filled(x, y, 4.878, arcade.color.GRAY)
    #Radius i Merkur
    arcade.draw_line(x_5, y_5, x, y, arcade.color.RED)
    #Venus
    arcade.draw_circle_filled(x_2, y_2, 12.104, arcade.color.ORANGE)
    #Radius i Venus
    arcade.draw_line(x_6, y_6, x_2, y_2, arcade.color.RED)
    #Jorden
    arcade.draw_circle_filled(x_3, y_3, 12.742, arcade.color.BLUE)
    #Radius i Jorden
    arcade.draw_line(x_7, y_7, x_3, y_3, arcade.color.RED)
    #Mars
    arcade.draw_circle_filled(x_4, y_4, 6.787, arcade.color.RED)
    #Radius i Mars
    arcade.draw_line(x_8, y_8, x_4, y_4, arcade.color.WHITE)

    #Tjekker om sporet er for langt
    if len(baner.spor) > SPORLAENGDE:
        baner.spor.pop(0)

    if len(baner.spor2) > SPORLAENGDE:
        baner.spor2.pop(0)

    if len(baner.spor3) > SPORLAENGDE:
        baner.spor3.pop(0)

    if len(baner.spor4) > SPORLAENGDE:
        baner.spor4.pop(0)

    #Tegner punkterne i sporerne
    for punkt in baner.spor:
        arcade.draw_circle_filled(*punkt, 2, arcade.color.GRAY)
    for punkt in baner.spor2:
        arcade.draw_circle_filled(*punkt, 2, arcade.color.ORANGE)
    for punkt in baner.spor3:
        arcade.draw_circle_filled(*punkt, 2, arcade.color.BLUE)
    for punkt in baner.spor4:
        arcade.draw_circle_filled(*punkt, 2, arcade.color.RED)
    #Opdateres over tid
    baner.tid += delta_tid
    #Tilf??jer nyt punkt i listen efter det sidste bliver fjernet
    baner.spor.append((x, y))
    baner.spor2.append((x_2, y_2))
    baner.spor3.append((x_3, y_3))
    baner.spor4.append((x_4, y_4))
def main():
    arcade.open_window(BREDDE, HOEJDE, "De indre planeter")
    arcade.set_background_color(arcade.csscolor.BLACK)
    #Planeterne starter med tiden 0.0
    baner.tid = 0.0
    #Listerner over sporet bliver genereret
    baner.spor = list()
    baner.spor2 = list()
    baner.spor3 = list()
    baner.spor4 = list()
    #Skal opdatere hvert 1/60 sekund
    arcade.schedule(baner, 1 / 60)

    arcade.run()

main()
