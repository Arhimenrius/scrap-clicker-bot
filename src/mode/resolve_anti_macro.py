from src.mobile import Mobile
from src.digit_detector import detect_digit
import random
import threading
from time import sleep
import cv2

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

mobile = Mobile()


class DetectAntiMacro:
    def is_mode_active(self, frame):
        cropped = crop_original_frame(frame)
        buttons_to_click = cropped[
                           buttons_y_min:buttons_y_max,
                           buttons_x_min:buttons_x_max
                           ]
        average_color_of_cropped = [cropped[:, :, i].mean() for i in range(cropped.shape[-1])]
        average_color_of_buttons_to_click = [buttons_to_click[:, :, i].mean() for i in range(cropped.shape[-1])]
        if cropped_min_blue < average_color_of_cropped[0] < cropped_max_blue \
                and cropped_min_green < average_color_of_cropped[1] < cropped_max_green \
                and cropped_min_red < average_color_of_cropped[2] < cropped_max_red \
                and buttons_min_blue < average_color_of_buttons_to_click[0] < buttons_max_blue \
                and buttons_min_green < average_color_of_buttons_to_click[1] < buttons_max_green \
                and buttons_min_red < average_color_of_buttons_to_click[2] < buttons_max_red:
            return True
        return False


class ResolveAntiMacro(threading.Thread):
    frame = None

    def __init__(self, frame):
        self.frame = frame
        threading.Thread.__init__(self)

    def run(self):
        cropped = crop_original_frame(self.frame)

        expected_number_image = cropped[
                                expected_number_y_min:expected_number_y_max,
                                expected_number_x_min:expected_number_x_max
                                ]
        try:
            expected_number = int(detect_digit(expected_number_image)[0])
            numbers_to_click = cropped[
                               buttons_y_min:buttons_y_max,
                               buttons_x_min:buttons_x_max
                               ]

            for row in range(0, number_of_buttons_y):
                for column in range(0, number_of_buttons_x):
                    button = numbers_to_click[
                             (button_height * row) + (button_offset_y * row):
                             (button_height * (row + 1)) + (button_offset_y * row),
                             (button_width * column) + (button_offset_x * column):
                             (button_width * (column + 1)) + (button_offset_x * column),
                             ]
                    number = int(detect_digit(button)[0])

                    if number == expected_number:
                        pass
                        x = buttons_position_on_mobile[row][column][0]
                        y = buttons_position_on_mobile[row][column][1]
                        mobile.initTouch()
                        mobile.actionDuringTouch(
                            x + random.randint(20, 40),
                            y + random.randint(20, 40),
                        )
                        mobile.clearTouch()
            sleep(0.5)
            mobile.initTouch()
            mobile.actionDuringTouch(
                confirm_button[0] + random.randint(20, 40),
                confirm_button[1] + random.randint(20, 40),
            )
            mobile.clearTouch()
        except ValueError:
            pass
        except IndexError:
            pass


def crop_original_frame(frame):
    return frame[y_min:y_max, x_min:x_max]
