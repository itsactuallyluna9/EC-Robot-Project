from typing import Literal
import pygame
from pygame.locals import *
from time import sleep


class Controller:
    __current_mode = "tank"
    __remote_stop_engaged = False

    def __init__(self):
        pygame.init()
        pygame.joystick.init()

    def connect(self):
        while True:
            if pygame.joystick.get_count() == 0:
                sleep(1)
            else:
                break

        self.joystick = pygame.joystick.Joystick(0)
        self.joystick.init()

    @property
    def controller_name(self):
        if self.joystick:
            return self.joystick.name

    @property
    def left_tank_thread(self):
        if self.__remote_stop_engaged:
            return 0

        if self.__current_mode == "tank":
            return self.joystick.get_axis(1)  # left stick y-axis
        return 0

    @property
    def right_tank_thread(self):
        if self.__remote_stop_engaged:
            return 0

        if self.current_mode == "tank":
            return self.joystick.get_axis(3)  # right stick y-axis

        return 0

    @property
    def arm_position(self):
        if self.__remote_stop_engaged:
            return 0
        
        return 0

    @property
    def hand_position(self):
        if self.__remote_stop_engaged:
            return 0
        
        return 0

    @property
    def remote_stop_engaged(self):
        return self.__remote_stop_engaged

    @property
    def current_mode(self) -> Literal["tank", "car"]:
        return self.__current_mode

    @property
    def should_shutdown(self):
        return False
