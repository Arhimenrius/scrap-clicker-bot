import numpy


class BarrelsDetector:
    barrel_height = 68
    barrel_width = 42

    x_beginning = 108
    y_beginning = 85

    x_space_between_barrels = 33
    y_space_between_barrels = 26

    x_elements = [1, 2, 3, 4]
    y_elements = [1, 2, 3, 4, 5]

    # Rmin/max, Gmin/max, Bmin/max
    color_of_levels = [
        [[63, 71], [73, 81], [64, 72]],
        [[130, 138], [205, 213], [209, 213]],
        [[103, 111], [82, 90], [26, 34]],
        [[204, 212], [197, 205], [173, 181]],
        [[111, 119], [91, 99], [62, 70]],
        [[112, 120], [106, 114], [93, 101]],
        [[179, 187], [167, 175], [50, 58]],
        [[56, 64], [137, 145], [59, 67]],
        [[202, 210], [212, 220], [192, 200]],
        [[102, 110], [116, 124], [102, 110]],
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
        level_per_position = list(range(20))
        for position_id, average_color in enumerate(average_colors):
            for level, color_of_level in enumerate(self.color_of_levels):
                if color_of_level[2][0] < average_color[0] < color_of_level[2][1] \
                        and color_of_level[1][0] < average_color[1] < color_of_level[1][1] \
                        and color_of_level[0][0] < average_color[2] < color_of_level[0][1]:
                    level_per_position[position_id] = level + 1

        return level_per_position

    def types_per_position(self, frame):
        average_colors = self.find_average_colors_per_position(frame)
        return self.detect_type_per_position(average_colors)
