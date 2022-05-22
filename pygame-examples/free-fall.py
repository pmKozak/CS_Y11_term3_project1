import pygame

from const import Window, Colors, Gravity
from object import RectangularObject, RoundObject


def main():
    obj = RectangularObject(
        x=100,
        y=100,
        width=40,
        height=40,
        v_x=0,
        v_y=0,
        color=Colors.PINK,
    )
    obj2 = RectangularObject(
        x=100,
        y=200,
        width=40,
        height=40,
        v_x=15,
        v_y=35,
        color=Colors.PINK,
    )
    # obj = RoundObject(
    #     x=100,
    #     y=100,
    #     radius=10,
    #     v_x=0,
    #     v_y=0,
    #     color=Colors.PINK,
    # )
    # obj2 = RoundObject(
    #     x=100,
    #     y=500,
    #     radius=40,
    #     v_x=-15,
    #     v_y=15,
    #     color=Colors.BLUE,
    # )
    timestep = 100
    pygame.init()
    clock = pygame.time.Clock()
    surface = pygame.display.set_mode(
        Window.SIZE, pygame.RESIZABLE
    )  # Displaying on specified window size
    print(pygame.display.get_surface().get_size())
    print(Window.SIZE)
    pygame.display.set_caption("Our game")
    run = True
    while run:
        clock.tick(timestep)
        surface.fill(Colors.GREEN)  # Window Bg

        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # To quit on clicking the X
                run = False
        obj.update(Gravity.Earth, timestep / 1000, [])
        obj2.update(Gravity.Earth, timestep / 1000, [obj])
        obj.draw(surface)
        obj2.draw(surface)
        pygame.display.update()  # To update the display with newly added codes

    pygame.quit()


main()
