import src.mobile as mobile
import cv2
import threading
from time import sleep
import numpy as np
import random
from skimage.measure import compare_ssim as ssim

y_min = 90
y_max = 503
x_min = 87
x_max = 393

expected_number_y_min = 38
expected_number_y_max = 86
expected_number_x_min = 251
expected_number_x_max = 286

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

event_info_min_red = 95
event_info_max_red = 105
event_info_min_green = 110
event_info_max_green = 120
event_info_min_blue = 120
event_info_max_blue = 130

confirm_button_row_min_red = 125
confirm_button_row_max_red = 140
confirm_button_row_min_green = 165
confirm_button_row_max_green = 175
confirm_button_row_min_blue = 195
confirm_button_row_max_blue = 205

tiles_coordinates = [
    # ROW 1
    [41, 92],
    [119, 92],
    [197, 92],
    # ROW 2
    [41, 168],
    [119, 168],
    [197, 168],
    # ROW 3
    [41, 245],
    [119, 245],
    [197, 245],
]

# X/Y per row
tiles_position_on_mobile = [
    # ROW 1
    [315, 650],
    [540, 650],
    [780, 650],
    # ROW 2
    [315, 875],
    [540, 875],
    [780, 875],
    # ROW 3
    [315, 1100],
    [540, 1100],
    [780, 1100],
]

tile_size = 69

confirm_button = [530, 1350]

event_info_x = [87, 393]
event_info_y = [90, 128]

confirm_button_row_x = [87, 393]
confirm_button_row_y = [428, 474]


class DetectAntiMacro:
    def is_mode_active(self, frame):
        event_info = frame[
                     event_info_y[0]:event_info_y[1],
                     event_info_x[0]:event_info_x[1]
                     ]
        confirm_button_row = frame[
                             confirm_button_row_y[0]:confirm_button_row_y[1],
                             confirm_button_row_x[0]:confirm_button_row_x[1]
                             ]
        event_info_avg_color = [event_info[:, :, i].mean() for i in range(event_info.shape[-1])]
        confirm_button_row_avg_color = [confirm_button_row[:, :, i].mean() for i in range(confirm_button_row.shape[-1])]
        if event_info_min_blue < event_info_avg_color[0] < event_info_max_blue \
                and event_info_min_green < event_info_avg_color[1] < event_info_max_green \
                and event_info_min_red < event_info_avg_color[2] < event_info_max_red \
                and confirm_button_row_min_blue < confirm_button_row_avg_color[0] < confirm_button_row_max_blue \
                and confirm_button_row_min_green < confirm_button_row_avg_color[1] < confirm_button_row_max_green \
                and confirm_button_row_min_red < confirm_button_row_avg_color[2] < confirm_button_row_max_red:
            return True
        return False


class ResolveAntiMacro(threading.Thread):
    frame = None

    def __init__(self, frame):
        self.frame = frame
        threading.Thread.__init__(self)

    def run(self):
        anti_macro_popup = crop_original_frame(self.frame)

        target = cv2.cvtColor(cv2.resize(anti_macro_popup[
                              expected_number_y_min:expected_number_y_max,
                              expected_number_x_min:expected_number_x_max
                              ], (69, 69)), cv2.COLOR_BGR2GRAY)

        tiles = [
            cv2.cvtColor(
                anti_macro_popup[
                p[1]:p[1] + tile_size,
                p[0]:p[0] + tile_size
                ],
                cv2.COLOR_BGR2GRAY
            ) for p in tiles_coordinates
        ]
        # print(distances)
        for i in range(len(tiles)):
            m = self.mse (target, tiles[i])
            # s = ssim(target, tiles[i])
            if m < 5610:
                mobile.initTouch()
                mobile.actionDuringTouch(
                    tiles_position_on_mobile[i][0] + random.randint(20, 40),
                    tiles_position_on_mobile[i][1] + random.randint(20, 40),
                )
                mobile.clearTouch()
        sleep(0.1)
        mobile.initTouch()
        mobile.actionDuringTouch(
            confirm_button[0] + random.randint(20, 40),
            confirm_button[1] + random.randint(20, 40),
        )
        mobile.clearTouch()

    def mse(self, target, tile):
        # the 'Mean Squared Error' between the two images is the
        # sum of the squared difference between the two images;
        # NOTE: the two images must have the same dimension
        err = np.sum((target.astype("float") - tile.astype("float")) ** 2)
        err /= float(target.shape[0] * target.shape[1])

        # return the MSE, the lower the error, the more "similar"
        # the two images are
        return err


def crop_original_frame(frame):
    return frame[y_min:y_max, x_min:x_max]
