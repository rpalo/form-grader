"""Form to be graded"""
import numpy as np

from block import Block

class Form:
    """Form to be graded"""
    def __init__(self, image, threshold=.05):
        """Assume image is a grayscale image.
        TODO: automatically detect for color images
        """
        self.rows = []
        self.image = image
        self.threshold = threshold
    
    def layout(self, row_lines, col_lines):
        """Builds up self.rows full of 'blocks'.
        row_lines: vector of row edge locations
        col_lines: vector of col edge locations
        
        returns: self
        """
        for i in range(len(row_lines[:-1])):
            self.rows.append([])
            for j in range(len(col_lines[:-1])):
                self.rows[-1].append(Block(
                    self.image,
                    col_lines[j],
                    col_lines[j + 1],
                    row_lines[i],
                    row_lines[i + 1]
                ))
        return self

    @classmethod
    def from_dict(cls, inputs):
        """Builds a form object from a config dictionary.
        Adding one to row and col count because the number of edges
        is 1 + number of rows/cols.
        TODO: Consider making a builder option or checking for
        specific keys and making super good error messages.
        """
        row_lines = np.linspace(
            inputs["row_start"],
            inputs["row_end"],
            inputs["row_count"] + 1,
            dtype=np.int32
        )
        col_lines = np.linspace(
            inputs["col_start"],
            inputs["col_end"],
            inputs["col_count"] + 1,
            dtype=np.int32
        )
        return Form(inputs["image"]).layout(row_lines, col_lines)

    def marked(self, boxes):
        """Returns the index of the first box that is marked in the
        given row.

        This is better than max right now because it allows us to find
        a blank row.
        """
        # for ind, box in enumerate(boxes):
        #     if box.black_pixel_ratio() >= self.threshold:
        #         return ind, box.black_pixel_ratio()
        # return -1  # Return -1 if no mark above threshold is found
        return [box.black_pixels() for box in boxes]

    def read(self):
        """Reads each row to detect which value has been marked."""
        return [self.marked(row) for row in self.rows]
