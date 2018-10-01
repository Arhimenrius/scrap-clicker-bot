from src.mobile import Mobile
from src.digit_detector import detect_digit
import random
import cv2


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

    number_of_buttons_x = 3
    number_of_buttons_y = 3

    button_height = 69
    button_width = 69
    button_offset_x = 9
    button_offset_y = 8

    cropped_min_red = 120
    cropped_max_red = 160
    cropped_min_green = 130
    cropped_max_green = 160
    cropped_min_blue = 130
    cropped_max_blue = 160

    buttons_min_red = 70
    buttons_max_red = 120
    buttons_min_green = 70
    buttons_max_green = 125
    buttons_min_blue = 70
    buttons_max_blue = 120

    # X/Y per row
    buttons_position_on_mobile = [
        # ROW 1
        [[315, 650], [540, 650], [780, 650]],
        # ROW 2
        [[315, 875], [540, 875], [780, 875]],
        # ROW 3
        [[315, 1100], [540, 1100], [780, 1100]],
    ]

    confirm_button = [530, 1350]

    ap = None

    def __init__(self):
        self.mobile = Mobile()

    def is_mode_active(self, frame):
        cropped = self.crop_original_frame(frame)
        buttons_to_click = cropped[
                           self.buttons_y_min:self.buttons_y_max,
                           self.buttons_x_min:self.buttons_x_max
                           ]
        average_color_of_cropped = [cropped[:, :, i].mean() for i in range(cropped.shape[-1])]
        average_color_of_buttons_to_click = [buttons_to_click[:, :, i].mean() for i in range(cropped.shape[-1])]
        if self.cropped_min_blue < average_color_of_cropped[0] < self.cropped_max_blue \
                and self.cropped_min_green < average_color_of_cropped[1] < self.cropped_max_green \
                and self.cropped_min_red < average_color_of_cropped[2] < self.cropped_max_red \
                and self.buttons_min_blue < average_color_of_buttons_to_click[0] < self.buttons_max_blue \
                and self.buttons_min_green < average_color_of_buttons_to_click[1] < self.buttons_max_green \
                and self.buttons_min_red < average_color_of_buttons_to_click[2] < self.buttons_max_red:
            return True
        return False

    def process_mode(self, frame):
        cropped = self.crop_original_frame(frame)

        expected_number_image = cropped[
                                self.expected_number_y_min:self.expected_number_y_max,
                                self.expected_number_x_min:self.expected_number_x_max
                                ]
        try:
            expected_number = int(detect_digit(expected_number_image)[0])
            numbers_to_click = cropped[
                               self.buttons_y_min:self.buttons_y_max,
                               self.buttons_x_min:self.buttons_x_max
                               ]

            for row in range(0, self.number_of_buttons_y):
                for column in range(0, self.number_of_buttons_x):
                    button = numbers_to_click[
                             (self.button_height * row) + (self.button_offset_y * row):
                             (self.button_height * (row + 1)) + (self.button_offset_y * row),
                             (self.button_width * column) + (self.button_offset_x * column):
                             (self.button_width * (column + 1)) + (self.button_offset_x * column),
                             ]
                    number = int(detect_digit(button)[0])

                    if number == expected_number:
                        pass
                        x = self.buttons_position_on_mobile[row][column][0]
                        y = self.buttons_position_on_mobile[row][column][1]
                        self.mobile.initTouch()
                        self.mobile.actionDuringTouch(
                            x + random.randint(20, 40),
                            y + random.randint(20, 40),
                        )
                        self.mobile.clearTouch()

            self.mobile.initTouch()
            self.mobile.actionDuringTouch(
                self.confirm_button[0] + random.randint(20, 40),
                self.confirm_button[1] + random.randint(20, 40),
            )
            self.mobile.clearTouch()
        except ValueError:
            pass
        except IndexError:
            pass

    def crop_original_frame(self, frame):
        return frame[self.y_min:self.y_max, self.x_min:self.x_max]
