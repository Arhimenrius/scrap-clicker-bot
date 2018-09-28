import cv2


class CollectSteel:
    def is_mode_active(self, frame):
        cropped = frame[155:180, 60:420]
        cv2.imshow("cropped", cropped)

        average_color = [cropped[:, :, i].mean() for i in range(cropped.shape[-1])]

        print(average_color)
        if 140 < average_color[0] < 155 and 180 < average_color[1] < 190 and 140 < average_color[2] < 160:
            return True
        return False

    def process_mode(self):
        print('Collect steel')
        pass
