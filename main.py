import arcade
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "moving around"
MOVEMENT_SPEED = 3


class Ball:

    def __init__(self, pos_x, pos_y, delta_x, delta_y, radius, init_color):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.delta_x = delta_x
        self.delta_y = delta_y
        self.radius = radius
        self.color = init_color

    def draw(self):
        arcade.draw_circle_filled(self.pos_x, self.pos_y, self.radius, self.color)

    def update(self):
        self.pos_x += self.delta_x
        self.pos_y += self.delta_y


class MyGame(arcade.Window):

    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.set_mouse_visible(False)
        arcade.set_background_color(arcade.color.WHITE)

        self.ball = Ball(*ball_randomizer(stationary=True))

    def on_draw(self):
        arcade.start_render()
        self.ball.draw()

    def update(self, delta_time):
        self.ball.update()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.ball.delta_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.ball.delta_x = MOVEMENT_SPEED
        elif key == arcade.key.UP:
            self.ball.delta_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.ball.delta_y = -MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.ball.delta_x = 0
        elif key == arcade.key.UP or key == arcade.key.DOWN:
            self.ball.delta_y = 0

    # def on_mouse_motion(self, x, y, dx, dy):
    #     self.ball.pos_x = x
    #     self.ball.pos_y = y


def ball_randomizer(stationary=False):

    radius = random.randrange(5, 20)
    pos_x = random.randrange(radius, SCREEN_WIDTH - radius)
    pos_y = random.randrange(radius, SCREEN_HEIGHT - radius)
    delta_x = 0 if stationary else random.randrange(2, 5) * random.choice([-1, 1])
    delta_y = 0 if stationary else random.randrange(2, 5) * random.choice([-1, 1])
    color = (random.randrange(0, 256), random.randrange(0, 256), random.randrange(0, 256))

    return [pos_x, pos_y, delta_x, delta_y, radius, color]


def main():
    # setup window
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

    # display
    arcade.run()


if __name__ == "__main__":
    main()
