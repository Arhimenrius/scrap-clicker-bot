from src.mobile import Mobile
from src.barrels_detector import BarrelsDetector
from itertools import groupby


class Merge:
    mobile = None
    barrels_detector = None
    # X/Y
    elements = [
        # ROW 1
        [200, 370],
        [430, 370],
        [650, 370],
        [875, 370],
        # ROW 2
        [200, 640],
        [430, 640],
        [650, 640],
        [875, 640],
        # ROW 3
        [200, 930],
        [430, 930],
        [650, 930],
        [875, 930],
        # ROW 4
        [200, 1220],
        [430, 1220],
        [650, 1220],
        [875, 1220],
        # ROW 5
        [200, 1500],
        [430, 1500],
        [650, 1500],
        [875, 1500],
    ]

    def __init__(self):
        self.mobile = Mobile()
        self.barrels_detector = BarrelsDetector()

    def process_mode(self, frame):
        barrel_per_position = self.barrels_detector.types_per_position(frame)
        print(barrel_per_position)
        pass
