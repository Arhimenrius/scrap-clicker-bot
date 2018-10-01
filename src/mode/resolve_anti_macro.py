from src.mobile import Mobile
import cv2
import argparse


class ResolveAntiMacro:
    mobile = None

    y_min = 90
    y_max = 503
    x_min = 87
    x_max = 393

    expected_number_y_min = 50
    expected_number_y_max = 70
    expected_number_x_min = 248
    expected_number_x_max = 263

    buttons_y_min = 92
    buttons_y_max = 314
    buttons_x_min = 41
    buttons_x_max = 266

    min_red = 140
    max_red = 160
    min_green = 140
    max_green = 160
    min_blue = 140
    max_blue = 160

    ap = None

    processed_frame = None

    def __init__(self):
        ap = argparse.ArgumentParser()
        self.mobile = Mobile()

    def is_mode_active(self, frame):
        cropped = frame[self.y_min:self.y_max, self.x_min:self.x_max]

        average_color = [cropped[:, :, i].mean() for i in range(cropped.shape[-1])]
        if self.min_blue < average_color[0] < self.max_blue \
                and self.min_green < average_color[1] < self.max_green \
                and self.min_red < average_color[2] < self.max_red:
            self.processed_frame = cropped
            return True
        return False

    def process_mode(self):
        expected_number_image = self.processed_frame[
                                self.expected_number_y_min:self.expected_number_y_max,
                                self.expected_number_x_min:self.expected_number_x_max
                                ]
        # cv2.imshow('test5', expected_number_image)
        # detect_digit('test1', expected_number_image)
        numbers_to_click = self.processed_frame[
                           self.buttons_y_min:self.buttons_y_max,
                           self.buttons_x_min:self.buttons_x_max
                           ]
        # cv2.imshow('test6', numbers_to_click)
        # detect_digit('test2', numbers_to_click)
        pass
