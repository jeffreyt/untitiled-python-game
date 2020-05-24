import arcade
from arcade import color

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SCREEN_TITLE = "sunny day"
RADIUS = 80


def sunny_day():
    # setup window
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.set_background_color(color.SKY_BLUE)

    # rendering
    arcade.start_render()
    arcade.draw_lrtb_rectangle_filled(0, (SCREEN_WIDTH * 1.0), (SCREEN_HEIGHT * 0.3), 0, arcade.csscolor.GREEN)
    arcade.draw_circle_filled((SCREEN_WIDTH * 0.8), (SCREEN_HEIGHT * 0.8), RADIUS, color.YELLOW)
    arcade.finish_render()

    # display
    arcade.run()


sunny_day()
