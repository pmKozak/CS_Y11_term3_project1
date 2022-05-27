from typing import Tuple, List, Union

import pygame
from paddle import Paddle


class Ball:
    def __init__(
        self,
        x: float,
        y: float,
        radius: float,
        v_x: float,
        v_y: float,
        color: Tuple[int, int, int],
    ):
        self.x = x
        self.y = y
        self.v_x = v_x
        self.v_y = v_y
        self.radius = radius
        self.color = color

    def update(self, timestep: float, objects: List[Union[Paddle, 'Ball']]):
        ret = None
        boundary_x, boundary_y = pygame.display.get_surface().get_size()
        self.x += self.v_x * timestep
        self.y += self.v_y * timestep
        if self.y + self.radius >= boundary_y or self.y - self.radius <= 0:
            self.v_y = -self.v_y
        if self.x - self.radius <= 0:
            ret = 2
        if self.x + self.radius >= boundary_x:
            ret = 1

        for other in objects:
            if other is self:
                continue
            if (
                abs(self.y - other.x) <= other.height // 2 + self.radius
            ) and (
                abs(self.x - other.y) <= other.width // 2 + self.radius
            ):
                other.v_y = - other.v_y
                self.v_x = - self.v_x
        return ret

    def draw(self, surface, *args, **kwargs):
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.radius)