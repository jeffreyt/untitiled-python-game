import arcade
from arcade import color

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SCREEN_TITLE = "hotdog"
RADIUS = 150


def main():
    # setup window
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.set_background_color(color.WHITE)

    # rendering
    arcade.start_render()
    arcade.draw_circle_filled(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, RADIUS, color.BLUE)
    arcade.finish_render()

    # display
    arcade.run()


if __name__ == "__main__":
    main()
