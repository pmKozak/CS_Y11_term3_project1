import random

import pygame
from const import Colors, Window, Gravity
from paddle import Paddle
from ball import Ball


def restart_game(ball: Ball):
    ball.x = Window.WIDTH // 2
    ball.y = Window.HEIGHT // 2
    ball.v_x = random.randint(-20, 20)
    ball.v_y = random.randint(-20, 20)


def main(friction=0.02):
    pygame.init()
    font = pygame.font.SysFont("verdana", 16)
    timestep = 100
    clock = pygame.time.Clock()
    surface = pygame.display.set_mode(Window.SIZE)  # Displaying on specified window size

    paddle1 = Paddle(
        x=100,
        y=100,
        v_x=0,
        v_y=0,
        color=Colors.PINK,
        friction=friction,
        key_up=pygame.K_q,
        key_down=pygame.K_a,
    )
    paddle2 = Paddle(
        x=100,
        y=Window.WIDTH - 100,
        v_x=0,
        v_y=0,
        color=Colors.BLUE,
        friction=friction,
    )
    ball = Ball(
        x=Window.WIDTH // 2,
        y=Window.HEIGHT // 2,
        v_x=0,
        v_y=0,
        radius=15,
        color=Colors.WHITE
    )
    objects = [
        paddle1,
        paddle2,
        ball
    ]
    pygame.display.set_caption("Pong game")
    run = True
    while run:
        clock.tick(timestep)
        surface.fill(Colors.GREEN)  # Window Bg
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # To quit on clicking the X
                run = False
        if pygame.key.get_pressed()[pygame.K_SPACE]:
            restart_game(ball)
        for obj in objects:
            ret = obj.update(timestep=timestep / 1000, objects=objects)
            obj.draw(surface, font)
            if ret is None:
                continue
            elif ret == 1:
                paddle1.points += 1
                restart_game(ball)
            elif ret == 2:
                paddle2.points += 1
                restart_game(ball)
            else:
                raise RuntimeError("Unknown response from Ball:", ret)
        pygame.display.update()  # To update the display with newly added codes

    pygame.quit()


main()