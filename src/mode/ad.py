import src.mobile as mobile
import cv2

frame_ad_button_y_min = 8
frame_ad_button_y_max = 50
frame_ad_button_x_min = 378
frame_ad_button_x_max = 420

mobile_ad_button_x = 1020
mobile_ad_button_y = 85

button_min_red = 75
button_max_red = 85
button_min_green = 145
button_max_green = 155
button_min_blue = 150
button_max_blue = 160

# mobile_ad_button_x

def is_mode_active(frame):
    cropped = frame[frame_ad_button_y_min:frame_ad_button_y_max, frame_ad_button_x_min:frame_ad_button_x_max]

    average_color = [cropped[:, :, i].mean() for i in range(cropped.shape[-1])]
    print(average_color)
    cv2.imshow('ad', cropped)
    cv2.waitKey(1)
