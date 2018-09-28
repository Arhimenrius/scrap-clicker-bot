import cv2


class CollectSteel:
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

    def is_mode_active(self, frame):
        cropped = frame[self.yMin:self.yMax, self.xMin:self.xMax]

        average_color = [cropped[:, :, i].mean() for i in range(cropped.shape[-1])]

        if self.minBlue < average_color[0] < self.maxBlue \
                and self.minGreen < average_color[1] < self.maxGreen \
                and self.minRed < average_color[2] < self.maxRed:
            return True
        return False

    def process_mode(self):
        pass
