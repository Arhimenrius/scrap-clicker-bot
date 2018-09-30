import numpy

class BarrelsDetector:
    barrel_height = 28  # 68 if crop full barrel
    barrel_width = 42

    y_offset = 20
    x_beginning = 108
    y_beginning = 85 + y_offset

    x_space_between_barrels = 33
    y_space_between_barrels = 66  # 26 if crop full barrel

    x_elements = [1, 2, 3, 4]
    y_elements = [1, 2, 3, 4, 5]

    # Rmin/max, Gmin/max, Bmin/max
    color_of_levels = [
        [[95, 105], [100, 113], [95, 105]],  # 0
        [[75, 85], [80, 90], [75, 85]],  # 1
        [[155, 165], [235, 245], [235, 245]],  # 2
        [[80, 90], [53, 63], [0, 10]],  # 3
        [[213, 223], [215, 225], [212, 222]],  # 4
        [[92, 102], [55, 65], [33, 43]],  # 5
        [[133, 143], [122, 132], [112, 122]],  # 6
        [[205, 215], [182, 192], [80, 90]],  # 7
        [[62, 72], [160, 170], [65, 75]],  # 8
        [[195, 205], [198, 208], [195, 205]],  # 9
        [[90, 100], [93, 103], [90, 100]],  # 10
    ]

    # [elementId => [x => [min, max], y => [min, max]]
    elements_positions = numpy.zeros((20, 2, 2), dtype=numpy.uint16)

    def __init__(self):
        element_index = 0
        for y_element in self.y_elements:
            for x_element in self.x_elements:
                self.elements_positions[element_index] = list(range(0, 2))

                self.elements_positions[element_index] = [
                    [
                        self.x_beginning
                        + (self.x_space_between_barrels * (x_element - 1))
                        + (self.barrel_width * (x_element - 1)),
                        self.x_beginning
                        + (self.x_space_between_barrels * (x_element - 1))
                        + (self.barrel_width * x_element),
                    ],
                    [
                        self.y_beginning
                        + (self.y_space_between_barrels * (y_element - 1))
                        + (self.barrel_height * (y_element - 1)),
                        self.y_beginning
                        + (self.y_space_between_barrels * (y_element - 1))
                        + (self.barrel_height * y_element),
                    ]
                ]
                element_index = element_index + 1

    def find_average_colors_per_position(self, frame):
        average_colors = list(range(0, 20))
        for element_id, element in enumerate(self.elements_positions):
            cropped = frame[element[1][0]:element[1][1], element[0][0]:element[0][1]]
            average_colors[element_id] = [cropped[:, :, i].mean() for i in range(cropped.shape[-1])]

        return average_colors

    def detect_type_per_position(self, average_colors):
        level_per_position = numpy.zeros(20, dtype=numpy.uint8)
        for position_id, average_color in enumerate(average_colors):
            for level, color_of_level in enumerate(self.color_of_levels):
                if color_of_level[2][0] < average_color[0] < color_of_level[2][1] \
                        and color_of_level[1][0] < average_color[1] < color_of_level[1][1] \
                        and color_of_level[0][0] < average_color[2] < color_of_level[0][1]:
                    level_per_position[position_id] = level
                    break

        return level_per_position

    def types_per_position(self, frame):
        average_colors = self.find_average_colors_per_position(frame)
        return self.detect_type_per_position(average_colors)
