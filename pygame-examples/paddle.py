from const import Colors
from typing import Tuple

import pygame


class Paddle:
    def __init__(
        self,
        x: float,
        y: float,
        v_x: float,
        v_y: float,
        color: Tuple[int, int, int],
        friction: float,
        key_up: int = pygame.K_UP,
        key_down: int = pygame.K_DOWN,
        points: int = 0
    ):
        self.x = x
        self.y = y
        self.v_x = v_x
        self.v_y = v_y
        window_width, window_height = pygame.display.get_surface().get_size()
        self.width = window_width // 40
        self.height = window_height // 5
        self.color = color
        assert 0 <= friction <= 1
        self.friction = friction
        self.up = key_up
        self.down = key_down
        self.points = points

    def update(self, timestep: float, *args, **kwargs):
        boundary_y, boundary_x = pygame.display.get_surface().get_size()
        if pygame.key.get_pressed()[self.up]:
            self.v_x -= 2
        elif pygame.key.get_pressed()[self.down]:
            self.v_x += 2
        self.x += self.v_x * timestep
        self.y += self.v_y * timestep
        if self.x + self.height / 2 >= boundary_x or self.x - self.height / 2 <= 0:
            self.v_x = -self.v_x
        if self.y + self.width / 2 >= boundary_y or self.y - self.width / 2 <= 0:
            self.v_y = -self.v_y
        self.v_x = (1 - self.friction) * self.v_x
        self.v_y = (1 - self.friction) * self.v_y

    def draw(self, surface, font):
        max_x, max_y = pygame.display.get_surface().get_size()
        rect = pygame.Rect(
            self.y - self.width / 2, self.x - self.height / 2, self.width, self.height
        )
        pygame.draw.rect(surface, self.color, rect)
        text = font.render(str(self.points), True, Colors.WHITE)
        surface.blit(text, (self.y - 0.5*text.get_width(), self.x - 0.5* text.get_width() ))


