from typing import Tuple, List

import pygame


def check_if_overlaps(first, second):
    return check_if_overlaps_x(first, second) and check_if_overlaps_y(first, second)


def check_if_overlaps_x(first, second):
    if first.x < second.x:
        return first.x + first.height / 2 > second.x - second.height / 2
    else:
        return first.x - first.height / 2 < second.x + second.height / 2


def check_if_overlaps_y(first, second):
    if first.y < second.y:
        return first.y + first.width / 2 > second.y - second.width / 2
    else:
        return first.y - first.width / 2 < second.y + second.width / 2


class RectangularObject:
    def __init__(
        self,
        x: float,
        y: float,
        height: float,
        width: float,
        v_x: float,
        v_y: float,
        color: Tuple[int, int, int],
    ):
        self.x = x
        self.y = y
        self.v_x = v_x
        self.v_y = v_y
        self.width = width
        self.height = height
        self.color = color

    def update(self, acceleration: Tuple[float, float], timestep: float, objects: List['RectangularObject']):
        boundary_y, boundary_x = pygame.display.get_surface().get_size()
        a_x, a_y = acceleration
        self.v_x += a_x * timestep
        self.v_y += a_y * timestep
        self.x += self.v_x * timestep
        self.y += self.v_y * timestep
        if self.x + self.height / 2 >= boundary_x or self.x - self.height / 2 <= 0:
            self.v_x = -self.v_x
        if self.y + self.width / 2 >= boundary_y or self.y - self.width / 2 <= 0:
            self.v_y = -self.v_y
        for other in objects:
            if other is self:
                continue
            if check_if_overlaps(self, other):
                self.v_x = -self.v_x
                self.v_y = -self.v_y
                other.v_x = -other.v_x
                other.v_y = -other.v_y

    def draw(self, surface):
        rect = pygame.Rect(
            self.y - self.width / 2, self.x - self.height / 2, self.width, self.height
        )
        pygame.draw.rect(surface, self.color, rect)


class RoundObject:
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

    def update(self, acceleration: Tuple[float, float], timestep: float, objects: List['RoundObject']):
        boundary_x, boundary_y = pygame.display.get_surface().get_size()
        a_x, a_y = acceleration
        self.v_x += a_x * timestep
        self.v_y += a_y * timestep
        self.x += self.v_x * timestep
        self.y += self.v_y * timestep
        if self.x + self.radius >= boundary_x or self.x - self.radius <= 0:
            self.v_x = -self.v_x
        if self.y + self.radius >= boundary_y or self.y - self.radius <= 0:
            self.v_y = -self.v_y
        for other in objects:
            if other is self:
                continue
            if (self.x - other.x)**2 + (self.y - other.y)**2 <= (self.radius + other.radius)**2:
                other.v_x = - other.v_x
                other.v_y = - other.v_y
                self.v_x = - self.v_x
                self.v_y = - self.v_y

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.radius)

