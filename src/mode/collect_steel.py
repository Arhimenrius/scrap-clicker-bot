from src.mobile import Mobile
import random


class CollectSteel:
    mobile = None

    minBlue = 140
    maxBlue = 155
    minGreen = 180
    maxGreen = 190
    minRed = 140
    maxRed = 160

    yMin = 155
    yMax = 175
    xMin = 60
    xMax = 420

    collectSteelFirstRowY = 550
    collectSteelSecondRowY = 650
    stepSize = 75

    def __init__(self):
        self.mobile = Mobile()

    def is_mode_active(self, frame):
        cropped = frame[self.yMin:self.yMax, self.xMin:self.xMax]

        average_color = [cropped[:, :, i].mean() for i in range(cropped.shape[-1])]

        if self.minBlue < average_color[0] < self.maxBlue \
                and self.minGreen < average_color[1] < self.maxGreen \
                and self.minRed < average_color[2] < self.maxRed:
            return True
        return False

    def process_mode(self):
        self.mobile.initTouch()
        for step in range(14):
            x = (self.stepSize * step) + random.randint(0, 10)
            y = self.collectSteelFirstRowY + random.randint(0, 10)

            self.mobile.actionDuringTouch(x, y)

        for step in range(14):
            x = (self.stepSize * step) + random.randint(0, 10)
            y = self.collectSteelSecondRowY + random.randint(0, 10)

            self.mobile.actionDuringTouch(x, y)
        self.mobile.clearTouch()
