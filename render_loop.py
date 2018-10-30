import pygame
from consts import *


def display_update(DISPLAY_SURFACE, FPS_CLOCK, game_state_list):
    """
    Update the screen to display any changes.

    :param DISPLAY_SURFACE:         Surface to be drawn onto
    :param FPS_CLOCK:               Clock object to track FPS
    :param game_state_list:         List of states to be updated
                                    on screen.
    :return:                        Nothing.
    """
    DISPLAY_SURFACE.blit(pygame.image.load("Assets/Art/screen.png"), (0, 0))
    object_to_blit = game_state_list[0]
    DISPLAY_SURFACE.blit(object_to_blit.sprites[0], (object_to_blit.x, object_to_blit.y))
    pygame.display.flip()
    FPS_CLOCK.tick(FPS)