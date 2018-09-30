from src.mobile import Mobile
from src.barrels_detector import BarrelsDetector
from time import sleep
import random


class Merge:
    mobile = None
    barrels_detector = None
    # X/Y
    elements = [
        # ROW 1
        [200, 370],
        [430, 370],
        [650, 370],
        [875, 370],
        # ROW 2
        [200, 640],
        [430, 640],
        [650, 640],
        [875, 640],
        # ROW 3
        [200, 930],
        [430, 930],
        [650, 930],
        [875, 930],
        # ROW 4
        [200, 1220],
        [430, 1220],
        [650, 1220],
        [875, 1220],
        # ROW 5
        [200, 1500],
        [430, 1500],
        [650, 1500],
        [875, 1500],
    ]

    distance_from_final_position_1 = 50
    distance_from_final_position_2 = 30
    distance_from_final_position_3 = 10

    max_level = 7
    position_under_remove_confirm_button = 14

    def __init__(self):
        self.mobile = Mobile()
        self.barrels_detector = BarrelsDetector()

    def find_pairs(self, frame):
        waiting_for_pair = {}
        pairs_to_merge = []
        barrel_per_position = self.barrels_detector.types_per_position(frame)
        for barrel_position, barrel_level in enumerate(barrel_per_position):
            if barrel_level >= self.max_level:
                self.remove_barrel(barrel_position)
                continue

            if barrel_level not in waiting_for_pair:
                waiting_for_pair[barrel_level] = []
            waiting_for_pair[barrel_level].append(barrel_position)

            if len(waiting_for_pair[barrel_level]) == 2:
                pairs_to_merge.append(waiting_for_pair[barrel_level])
                waiting_for_pair[barrel_level] = []

        return pairs_to_merge

    def remove_barrel(self, position_to_remove):
        element_position = self.elements[position_to_remove]
        self.mobile.initTouch()
        self.mobile.actionDuringTouch(
            element_position[0] - self.distance_from_final_position_1 + random.randint(0, 10),
            element_position[1] - self.distance_from_final_position_1 + random.randint(0, 10)
        )
        self.mobile.clearTouch()
        self.mobile.initTouch()
        self.mobile.actionDuringTouch(
            element_position[0] - self.distance_from_final_position_1 + random.randint(0, 10),
            element_position[1] - self.distance_from_final_position_1 + random.randint(0, 10)
        )
        self.mobile.clearTouch()
        sleep(0.2)

        place_to_confirm = self.elements[self.position_under_remove_confirm_button]
        self.mobile.initTouch()
        self.mobile.actionDuringTouch(
            place_to_confirm[0] - self.distance_from_final_position_1 + random.randint(0, 10),
            place_to_confirm[1] - self.distance_from_final_position_1 + random.randint(0, 10)
        )
        self.mobile.clearTouch()

    def process_mode(self, frame):
        pairs = self.find_pairs(frame)
        for pair in pairs:
            self.mobile.initTouch()
            element_position_1 = self.elements[pair[0]]
            element_position_2 = self.elements[pair[1]]
            self.mobile.actionDuringTouch(
                element_position_1[0] + random.randint(0, 10),
                element_position_1[1] + random.randint(0, 10)
            )

            self.mobile.actionDuringTouch(
                element_position_2[0] - self.distance_from_final_position_1 + random.randint(0, 10),
                element_position_2[1] - self.distance_from_final_position_1 + random.randint(0, 10)
            )

            self.mobile.actionDuringTouch(
                element_position_2[0] - self.distance_from_final_position_2 + random.randint(0, 10),
                element_position_2[1] - self.distance_from_final_position_2 + random.randint(0, 10)
            )

            self.mobile.actionDuringTouch(
                element_position_2[0] - self.distance_from_final_position_3 + random.randint(0, 10),
                element_position_2[1] - self.distance_from_final_position_3 + random.randint(0, 10)
            )

            self.mobile.actionDuringTouch(
                element_position_2[0] + random.randint(0, 10),
                element_position_2[1] + random.randint(0, 10)
            )

            self.mobile.clearTouch()

            # random touch to avoid cheat detector

            self.mobile.initTouch()
            self.mobile.actionDuringTouch(0, random.randint(200, 1000))
            self.mobile.clearTouch()
