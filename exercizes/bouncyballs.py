import arcade
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
NUMBER_OF_BALLS = 30
SCREEN_TITLE = "bounce, see?"


class BouncyBall:

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

        if self.pos_x < (0 + self.radius) or self.pos_x > (SCREEN_WIDTH - self.radius):
            self.delta_x *= -1

        if self.pos_y < (0 + self.radius) or self.pos_y > (SCREEN_HEIGHT - self.radius):
            self.delta_y *= -1


class BouncyBallPit(arcade.Window):

    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.WHITE)

        self.balls = []
        for x in range(NUMBER_OF_BALLS):
            self.balls.append(BouncyBall(*ball_randomizer()))

    def on_draw(self):
        arcade.start_render()
        for ball in self.balls:
            ball.draw()

    def update(self, delta_time):
        for ball in self.balls:
            ball.update()


def ball_randomizer():

    radius = random.randrange(5, 20)
    pos_x = random.randrange(radius, SCREEN_WIDTH - radius)
    pos_y = random.randrange(radius, SCREEN_HEIGHT - radius)
    delta_x = random.randrange(2, 5) * random.choice([-1, 1])
    delta_y = random.randrange(2, 5) * random.choice([-1, 1])
    color = (random.randrange(0, 256), random.randrange(0, 256), random.randrange(0, 256))

    return [pos_x, pos_y, delta_x, delta_y, radius, color]


def main():
    # setup window
    window = BouncyBallPit(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

    # display
    arcade.run()


if __name__ == "__main__":
    main()
