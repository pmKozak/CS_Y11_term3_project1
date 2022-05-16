import pygame
from const import Colors, Window, Gravity
from object import Object


def control_object(obj):
    if pygame.key.get_pressed()[pygame.K_UP]:
        obj.v_x -= 10
    if pygame.key.get_pressed()[pygame.K_DOWN]:
        obj.v_x += 10
    if pygame.key.get_pressed()[pygame.K_RIGHT]:
        obj.v_y += 10
    if pygame.key.get_pressed()[pygame.K_LEFT]:
        obj.v_y -= 10
    if pygame.key.get_pressed()[pygame.K_SPACE]:
        obj.v_x = 0
        obj.v_y = 0


def main():
    obj = Object(
        x=100,
        y=100,
        height=40,
        width=40,
        v_x=0,
        v_y=0,
        color=Colors.PINK,
    )
    timestep = 100
    pygame.init()
    clock = pygame.time.Clock()
    surface = pygame.display.set_mode(Window.SIZE)  # Displaying on specified window size
    pygame.display.set_caption("Our game")
    run = True
    while run:
        clock.tick(timestep)
        surface.fill(Colors.GREEN)  # Window Bg

        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # To quit on clicking the X
                run = False
        control_object(obj)
        obj.update(Gravity.No, timestep / 1000)
        obj.draw(surface)
        pygame.display.update()  # To update the display with newly added codes

    pygame.quit()


main()