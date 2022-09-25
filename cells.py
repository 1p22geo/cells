# ************************
# Special class defining file for cell types
# - Contains C  E  L  L  S
# You know, just in case
# *********************

import pygame, math
from unspec_cell import Cell

class DataCollector(Cell):
    def __init__(self):
        super().__init__()
        self.type = "Data collector cell"
        self.spec_cost = [10, 0, 0, 0]
        self.produced = [0.2, 0, 0, 0]
        self.description = [
            "- Produces Data",
            "- Can't be divided",
            "- Can be re-specialised",
            "  into a Mass",
            "  Data collector",
            "",
        ]
        self.specBpossible = True
        self.cooldownSpeed = 0

class MassCollector(Cell):
    def __init__(self):
        super().__init__()
        self.type = "Mass data collector"
        self.spec_cost = [100, 0, 0, 0]
        self.produced = [-0.4, 0.05, 0, 0]
        self.description = [
            "- Produces Mass data",
            "- Can't be divided",
            "- Can be re-specialised",
            "  into a prime number",
            "  collector",
            "",
        ]
        self.specBpossible = False
        self.cooldownSpeed = 0

class PrimeCollector(Cell):
    def __init__(self):
        super().__init__()
        self.type = "Prime number collector"
        self.spec_cost = [0, 200, 0, 0]
        self.produced = [-0.2, -0.15, 0.01, 0]
        self.description = [
            "- Finds prime numbers",
            "  using a simple method",
            "- uses mass data",
            "- Opens new possibilities",
            "- Has two possible respecs",
            "",
        ]
        self.specBpossible = True
        self.cooldownSpeed = 0

class PiCollector(Cell):
    def __init__(self):
        super().__init__()
        self.type = "Pi decimals calculator"
        self.produced = [-0.4, 0, -0.005, 15]
        self.description = [
            "- Calculates the decimal",
            "  places of the pi constant",
            "- They can be used",
            "  for decreasing visibility",
            "- Unlocks new possibilities",
            "",
        ]
        self.specBpossible = False
        self.cooldownSpeed = 0
        self.spec_cost = [0, 0, 100, 0]
        self.cooldown = 100

class EffPrime(Cell):
    def __init__(self):
        super().__init__()
        self.type = "Eff-prime cell"
        self.produced = [-0.2, -0.05, 0.005, -3]
        self.description = [
            "- Calculates prime numbers",
            "  more efficiently using",
            "  less input data.",
            "- Produces less prime numbers",
            "  than the original",
            "",
        ]
        self.specBpossible = False
        self.cooldownSpeed = 0
        self.spec_cost = [0, 0, 100, 1000]
        self.cooldown = 100