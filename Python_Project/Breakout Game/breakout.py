"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 10         # 100 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    graphics = BreakoutGraphics()
    lives = NUM_LIVES
    # Add the animation loop here!
    while True:
        if lives == 0 or graphics.brick_num == 0:
            break
        pause(FRAME_RATE)
        if graphics.start:
            dx = graphics.get_dx()
            dy = graphics.get_dy()
            while True:
                # pause
                pause(FRAME_RATE)

                # update
                graphics.ball.move(dx, dy)

                # check whether the ball exceeds the bottom boundary
                if graphics.ball.y + graphics.ball.height >= graphics.window.height:
                    graphics.start = False  # stop ball from moving
                    lives -= 1
                    graphics.reset_ball()
                    break

                # check whether the ball hits the items
                collision = False  # a switch for checking whether the collision happens
                for i in range(2):
                    if collision:
                        break
                    for j in range(2):
                        obj = graphics.window.get_object_at(graphics.ball.x + graphics.ball.width*i,
                                                            graphics.ball.y + graphics.ball.height*j)
                        if obj is not None:
                            if obj == graphics.paddle:  # when ball hits the paddle
                                dy = -dy  # make ball rebound
                            else:   # when ball hits the brick
                                graphics.window.remove(obj)  # remove the brick
                                graphics.brick_num -= 1
                                if graphics.brick_num == 0:
                                    lives = 0
                                dy = -dy
                            collision = True
                            break

                # check whether the ball hits the boundaries other than bottom
                if graphics.ball.x <= 0 or graphics.ball.x + graphics.ball.width >= graphics.window.width:
                    dx = -dx
                if graphics.ball.y <= 0:
                    dy = -dy


if __name__ == '__main__':
    main()
