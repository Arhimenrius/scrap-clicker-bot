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

    def detect_types_per_position(self, frame):
        average_color_by_element = list(range(0, 20))
        for element_id, element in enumerate(self.elements_positions):
            cropped = frame[element[1][0]:element[1][1], element[0][0]:element[0][1]]
            average_color_by_element[element_id] = [cropped[:, :, i].mean() for i in range(cropped.shape[-1])]

    def type1(self):
        pass

    def type2(self):
        pass

    def type3(self):
        pass

    def type4(self):
        pass

    def type5(self):
        pass

    def type6(self):
        pass

    def type7(self):
        pass

    def type8(self):
        pass

    def type9(self):
        pass

    def type10(self):
        pass
