import arcade
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
NUMBER_OF_BALLS = 10
MOVEMENT_SPEED = 3
SCREEN_TITLE = "me hungry"


class Pakumon:
    def __init__(self, pos_x, pos_y, mouth_speed, radius):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.delta_x = 0
        self.delta_y = 0
        self.mouth = 0
        self.delta_mouth = mouth_speed
        self.radius = radius
        self.orientation = 0

    def draw(self):
        # arcade.draw_circle_filled(self.x, self.y, 50, arcade.color.BANANA_YELLOW)
        mouth_top = self.orientation + 30 - self.mouth
        mouth_bottom = self.orientation + 330 + self.mouth
        arcade.draw_arc_filled(self.pos_x, self.pos_y, self.radius, self.radius, arcade.color.BANANA_YELLOW, mouth_top, mouth_bottom)
        # arcade.draw_arc_outline(self.x, self.y, 50, 50, arcade.color.BLACK, mouth_top, mouth_bottom)

    def update(self):
        self.mouth += self.delta_mouth
        if self.mouth > 30 or self.mouth < 0:
            self.delta_mouth *= -1

        self.pos_x = clamp(self.pos_x + self.delta_x, 0 + self.radius, SCREEN_WIDTH - self.radius)
        self.pos_y = clamp(self.pos_y + self.delta_y, 0 + self.radius, SCREEN_HEIGHT - self.radius)


class BouncyBall:

    def __init__(self, pos_x, pos_y, delta_x, delta_y, radius, init_color, is_eaten=False):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.delta_x = delta_x
        self.delta_y = delta_y
        self.radius = radius
        self.color = init_color
        self.is_eaten = is_eaten

    def draw(self):
        if not self.is_eaten:
            arcade.draw_circle_filled(self.pos_x, self.pos_y, self.radius, self.color)
            # arcade.draw_circle_outline(self.pos_x, self.pos_y, self.radius, arcade.color.CYBER_YELLOW)

    def update(self):
        self.pos_x += self.delta_x
        self.pos_y += self.delta_y

        if self.pos_x < (0 + self.radius) or self.pos_x > (SCREEN_WIDTH - self.radius):
            self.delta_x *= -1

        if self.pos_y < (0 + self.radius) or self.pos_y > (SCREEN_HEIGHT - self.radius):
            self.delta_y *= -1

    def die(self):
        self.is_eaten = True


class HungryCircleGuy(arcade.Window):

    def __init__(self, width, height, title):
        # setup window
        super().__init__(width, height, title)
        self.set_mouse_visible(False)
        arcade.set_background_color(arcade.color.COOL_GREY)

        # construct
        self.balls = []
        self.score = 0
        self.p1 = Pakumon(SCREEN_WIDTH*0.5, SCREEN_HEIGHT*0.5, 1, 50)
        for x in range(NUMBER_OF_BALLS):
            self.balls.append(BouncyBall(*ball_randomizer(radius=10, color=arcade.color.GHOST_WHITE)))

    def on_draw(self):
        arcade.start_render()
        self.p1.draw()
        for ball in self.balls:
            ball.draw()

        # text hud
        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.RED, 18)

    def update(self, delta_time):
        self.p1.update()
        for ball in self.balls:
            ball.update()
            if detect_collision(self.p1, ball):
                ball.die()
                self.balls.remove(ball)
                self.score += 1

    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.p1.orientation = 180
            self.p1.delta_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.p1.orientation = 0
            self.p1.delta_x = MOVEMENT_SPEED
        elif key == arcade.key.UP:
            self.p1.orientation = 90
            self.p1.delta_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.p1.orientation = 270
            self.p1.delta_y = -MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.p1.delta_x = 0
        elif key == arcade.key.UP or key == arcade.key.DOWN:
            self.p1.delta_y = 0


def ball_randomizer(radius=None, color=None):

    radius = radius if radius else random.randrange(5, 20)
    pos_x = random.randrange(radius, SCREEN_WIDTH - radius)
    pos_y = random.randrange(radius, SCREEN_HEIGHT - radius)
    delta_x = random.randrange(2, 5) * random.choice([-1, 1])
    delta_y = random.randrange(2, 5) * random.choice([-1, 1])
    color = color if color else (random.randrange(0, 256), random.randrange(0, 256), random.randrange(0, 256))

    return [pos_x, pos_y, delta_x, delta_y, radius, color]


def clamp(value, minval, maxval):
    if value < minval:
        return minval
    elif value > maxval:
        return maxval
    else:
        return value


def detect_collision(p1, ball):

    return False


def main():
    """ main """
    # setup window
    window = HungryCircleGuy(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

    # display
    arcade.run()


if __name__ == "__main__":
    main()
