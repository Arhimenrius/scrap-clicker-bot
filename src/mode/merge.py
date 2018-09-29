from src.mobile import Mobile
from src.barrels_detector import BarrelsDetector


class Merge:
    mobile = None
    barrels_detector = None

    def __init__(self):
        self.mobile = Mobile()
        self.barrels_detector = BarrelsDetector()

    def process_mode(self, frame):
        barrel_per_position = self.barrels_detector.detect_types_per_position(frame)
        # print(barrel_per_position)
        pass
