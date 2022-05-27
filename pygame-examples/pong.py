import random

import pygame
from const import Colors, Window, Gravity
from paddle import Paddle
from ball import Ball


def restart_game(ball: Ball, min_velocity: int = 20, max_velocity: int = 50):
    assert 0 < min_velocity < max_velocity
    ball.x = Window.WIDTH // 2
    ball.y = Window.HEIGHT // 2
    v_x = 0
    v_y = 0
    while v_y < min_velocity / 2 or v_x ** 2 + v_y ** 2 < min_velocity ** 2:
        v_x = random.randint(-max_velocity, max_velocity)
        v_y = random.randint(-max_velocity, max_velocity)
    ball.v_x = v_x
    ball.v_y = v_y


def main(friction=0.02, n_balls=2):
    pygame.init()
    font = pygame.font.SysFont("verdana", 16)
    timestep = 100
    clock = pygame.time.Clock()
    surface = pygame.display.set_mode(Window.SIZE)  # Displaying on specified window size

    paddle1 = Paddle(
        x=Window.HEIGHT // 2,
        y=100,
        v_x=0,
        v_y=0,
        color=Colors.PINK,
        friction=friction,
        key_up=pygame.K_w,
        key_down=pygame.K_s,
    )
    paddle2 = Paddle(
        x=Window.HEIGHT // 2,
        y=Window.WIDTH - 100,
        v_x=0,
        v_y=0,
        color=Colors.BLUE,
        friction=friction,
    )
    balls = []
    for _ in range(n_balls):
        balls.append(Ball(
            x=Window.WIDTH // 2,
            y=Window.HEIGHT // 2,
            v_x=0,
            v_y=0,
            radius=15,
            color=Colors.WHITE
        ))
    objects = [
        paddle1,
        paddle2,
        *balls
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
            for ball in balls:
                restart_game(ball)
        for obj in objects:
            ret = obj.update(timestep=timestep / 1000, objects=[paddle1, paddle2])
            obj.draw(surface, font)
            if ret is None:
                continue
            elif ret == 1:
                paddle1.points += 1
                for ball in balls:
                    restart_game(ball)
            elif ret == 2:
                paddle2.points += 1
                for ball in balls:
                    restart_game(ball)
            else:
                raise RuntimeError("Unknown response from Ball:", ret)
        pygame.display.update()  # To update the display with newly added codes

    pygame.quit()


main()