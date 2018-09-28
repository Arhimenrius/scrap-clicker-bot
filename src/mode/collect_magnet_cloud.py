class CollectMagnetCloud:
    def is_mode_active(self, frame):
        cropped = frame[0:40, 200:300]
        average_color = [cropped[:, :, i].mean() for i in range(cropped.shape[-1])]

        if all(i > 235 for i in average_color):
            return True

        return False

    def process_mode(self):
        print('Collect Magnet Cloud')
        pass
