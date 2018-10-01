from src.mobile import Mobile
import random


class CollectMagnetCloud:
    mobile = None

    y_min = 0
    y_max = 40
    x_min = 200
    x_max = 300

    minimumColorToExpect = 200

    collectMagnetRowY = 470
    stepSize = 50

    def __init__(self):
        self.mobile = Mobile()

    def is_mode_active(self, frame):
        cropped = frame[self.y_min:self.y_max, self.x_min:self.x_max]
        average_color = [cropped[:, :, i].mean() for i in range(cropped.shape[-1])]

        if all(i > self.minimumColorToExpect for i in average_color):
            return True

        return False

    def process_mode(self):
        self.mobile.initTouch()
        for step in range(21):
            x = (self.stepSize * step) + random.randint(0, 70)
            y = self.collectMagnetRowY + random.randint(0, 70)

            self.mobile.actionDuringTouch(x, y)
        self.mobile.clearTouch()
        pass
