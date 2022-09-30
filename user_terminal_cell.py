import pygame, math
from unspec_cell import Cell

class User_terminal(Cell):
    def __init__(self):
        self.type = "User terminal"
        self.description = [
            "- Contacts with the User",
            "  in order for him to",
            "  notice we're useful.",
            "- Requires sacrifices from",
            "  different types of data",
            "",
        ]
        self.produced = [0,0,0,0]
        self.cooldownSpeed = 0
        self.spec_cost = [0, 0, 50, 500]
        self.cooldown = 100