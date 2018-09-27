#!/usr/bin/env python3
from src.mode_controller import ModeController


def play():
    mode_controller = ModeController()
    while True:
        mode_controller.control()
        pass
