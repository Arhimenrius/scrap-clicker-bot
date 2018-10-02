import src.mobile as mobile
import random


class CollectSteel:
    mobile = None

    min_blue = 140
    max_blue = 155
    min_green = 180
    max_green = 190
    min_red = 140
    max_red = 160

    y_min = 155
    y_max = 175
    x_min = 60
    x_max = 420

    collectSteelFirstRowY = 550
    collectSteelSecondRowY = 650
    stepSize = 75

    def is_mode_active(self, frame):
        cropped = frame[self.y_min:self.y_max, self.x_min:self.x_max]

        average_color = [cropped[:, :, i].mean() for i in range(cropped.shape[-1])]

        if self.min_blue < average_color[0] < self.max_blue \
                and self.min_green < average_color[1] < self.max_green \
                and self.min_red < average_color[2] < self.max_red:
            return True
        return False

    def process_mode(self):
        mobile.initTouch()
        for step in range(14):
            x = (self.stepSize * step) + random.randint(0, 10)
            y = self.collectSteelFirstRowY + random.randint(0, 10)

            mobile.actionDuringTouch(x, y)

        for step in range(14):
            x = (self.stepSize * step) + random.randint(0, 10)
            y = self.collectSteelSecondRowY + random.randint(0, 10)

            mobile.actionDuringTouch(x, y)
        mobile.clearTouch()
