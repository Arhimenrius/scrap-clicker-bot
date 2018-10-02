import src.mobile as mobile
from src.text_detector import detect_text
import threading
import random
from time import sleep
import logging

frame_ad_button_y_min = 8
frame_ad_button_y_max = 50
frame_ad_button_x_min = 378
frame_ad_button_x_max = 420

mobile_ad_button_x = 1020
mobile_ad_button_y = 90

frame_opened_ad_y_min = 140
frame_opened_ad_y_max = 265
frame_opened_ad_x_min = 87
frame_opened_ad_x_max = 393

button_min_red = 75
button_max_red = 85
button_min_green = 145
button_max_green = 155
button_min_blue = 150
button_max_blue = 160

opened_ad_min_red = 160
opened_ad_max_red = 170
opened_ad_min_green = 160
opened_ad_max_green = 170
opened_ad_min_blue = 133
opened_ad_max_blue = 143

bonus_name_y_min = 275
bonus_name_y_max = 305
bonus_name_x_min = 95
bonus_name_x_max = 390

allowed_bonuses = ['Faster Barrels']

mobile_confirm_button_x = 750
mobile_confirm_button_y = 1230

mobile_decline_button_x = 350
mobile_decline_button_y = 1230


def is_mode_active(frame):
    ad_button = crop_ad_button(frame)
    ad_button_average_color = [ad_button[:, :, i].mean() for i in range(ad_button.shape[-1])]

    opened_ad = crop_opened_ad(frame)
    opened_ad_average_color = [opened_ad[:, :, i].mean() for i in range(opened_ad.shape[-1])]

    if opened_ad_min_blue < opened_ad_average_color[0] < opened_ad_max_blue \
            and opened_ad_min_green < opened_ad_average_color[1] < opened_ad_max_green \
            and opened_ad_min_red < opened_ad_average_color[2] < opened_ad_max_red:
        return True

    if button_min_blue < ad_button_average_color[0] < button_max_blue \
            and button_min_green < ad_button_average_color[1] < button_max_green \
            and button_min_red < ad_button_average_color[2] < button_max_red:
        mobile.initTouch()
        mobile.actionDuringTouch(
            mobile_ad_button_x + random.randint(5, 10),
            mobile_ad_button_y + random.randint(5, 10)
        )
        mobile.clearTouch()
        return True

    return False


class ResolveAd(threading.Thread):
    frame = None

    def __init__(self, frame):
        self.frame = frame
        threading.Thread.__init__(self)

    def run(self):
        bonus_text_image = self.frame[bonus_name_y_min:bonus_name_y_max, bonus_name_x_min:bonus_name_x_max]
        try:
            bonus_text = detect_text(bonus_text_image).strip()
            logging.info(bonus_text)
            if bonus_text in allowed_bonuses:
                mobile.initTouch()
                mobile.actionDuringTouch(
                    mobile_confirm_button_x + random.randint(10, 20),
                    mobile_confirm_button_y + random.randint(10, 20)
                )
                mobile.clearTouch()
                sleep(32)
                # leave ad
                mobile.click_back_button()
            else:
                mobile.initTouch()
                mobile.actionDuringTouch(
                    mobile_decline_button_x + random.randint(10, 20),
                    mobile_decline_button_y + random.randint(10, 20)
                )
                mobile.clearTouch()
                sleep(0.5)
        except ValueError:
            pass
        except IndexError:
            pass
        pass


def crop_opened_ad(frame):
    return frame[frame_opened_ad_y_min:frame_opened_ad_y_max, frame_opened_ad_x_min:frame_opened_ad_x_max]


def crop_ad_button(frame):
    return frame[frame_ad_button_y_min:frame_ad_button_y_max, frame_ad_button_x_min:frame_ad_button_x_max]
