import pygame

from const import Window, Colors, Gravity
from object import Object


def main():
    obj = Object(
        x=100,
        y=100,
        height=40,
        width=40,
        v_x=25,
        v_y=25,
        color=Colors.PINK,
    )
    obj2 = Object(
        x=100,
        y=500,
        height=40,
        width=40,
        v_x=-15,
        v_y=15,
        color=Colors.BLUE,
    )
    timestep = 100
    pygame.init()
    clock = pygame.time.Clock()
    surface = pygame.display.set_mode(
        Window.SIZE, pygame.RESIZABLE
    )  # Displaying on specified window size
    pygame.display.set_caption("Our game")
    run = True
    while run:
        clock.tick(timestep)
        surface.fill(Colors.GREEN)  # Window Bg

        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # To quit on clicking the X
                run = False
        obj.update(Gravity.Earth, timestep / 1000, [obj2])
        obj2.update(Gravity.Earth, timestep / 1000, [obj])
        obj.draw(surface)
        obj2.draw(surface)
        pygame.display.update()  # To update the display with newly added codes

    pygame.quit()


main()
