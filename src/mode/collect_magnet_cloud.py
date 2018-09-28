class CollectMagnetCloud:
    yMin = 0
    yMax = 40
    xMin = 200
    xMax = 300

    minimumColorToExpect = 220

    def is_mode_active(self, frame):
        cropped = frame[self.yMin:self.yMax, self.xMin:self.xMax]
        average_color = [cropped[:, :, i].mean() for i in range(cropped.shape[-1])]

        if all(i > self.minimumColorToExpect for i in average_color):
            return True

        return False

    def process_mode(self):
        pass
