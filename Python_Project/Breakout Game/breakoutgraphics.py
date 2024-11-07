"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Width of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10        # Number of rows of bricks
BRICK_COLS = 10        # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height, x=(window_width-paddle_width)/2
                            , y=window_height-paddle_offset-paddle_height)
        self.paddle.filled = True
        self.window.add(self.paddle)

        # Center a filled ball
        self.ball = GOval(ball_radius, ball_radius)
        self.ball.filled = True

        # Default initial position for the ball
        self.reset_ball()

        # Default initial velocity for the ball
        self.__dx = 0
        self.__dy = 0

        # Draw bricks
        for i in range(brick_cols):
            for j in range(brick_rows):
                self.brick = GRect(brick_width, brick_height, x=(brick_width+brick_spacing)*i
                                   , y=(brick_offset-brick_height)+(brick_height+brick_spacing)*j)
                self.brick.filled = True
                if j < 2:
                    self.brick.fill_color = "red"
                elif 2 <= j < 4:
                    self.brick.fill_color = "orange"
                elif 4 <= j < 6:
                    self.brick.fill_color = "yellow"
                elif 6 <= j < 8:
                    self.brick.fill_color = "green"
                else:
                    self.brick.fill_color = "blue"
                self.window.add(self.brick)
        self.brick_num = brick_cols*brick_rows  # record the number of bricks

        # Initialize our mouse listeners
        self.start = False  # a switch for controlling the ball move
        onmouseclicked(self.set_ball_velocity)
        onmousemoved(self.paddle_move)

    def reset_ball(self):
        """
        Set the position of the ball.
        """
        self.ball.x = (self.window.width - self.ball.width) / 2
        self.ball.y = (self.window.height - self.ball.height) / 2
        self.__dx = 0
        self.__dy = 0
        self.window.add(self.ball)

    def set_ball_velocity(self, _):
        """
        Set the velocity of the ball when clicking the mouse.
        """
        self.start = True
        self.__dx = random.randint(1, MAX_X_SPEED)
        self.__dy = INITIAL_Y_SPEED
        if random.random() > 0.5:
            self.__dx = -self.__dx

    def paddle_move(self, mouse):
        """
        Set the paddle move everytime when the mouse moves.
        """
        if mouse.x < 0:
            self.paddle.x = 0
        elif mouse.x > self.window.width:
            self.paddle.x = self.window.width-self.paddle.width
        else:
            self.paddle.x = mouse.x - self.paddle.width / 2

    def get_dx(self):
        """
        :return: self.__dx: provide the value of private dx to user
        """
        return self.__dx

    def get_dy(self):
        """
        :return: self.__dy: provide the value of private dx to user
        """
        return self.__dy