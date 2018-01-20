"""Block of pixels"""

import numpy as np

class Block:
    """Block of pixels"""
    def __init__(self, image, x1, x2, y1, y2):
        self.image = image
        self.pixels = self.image[x1:x2, y1:y2]

    def average(self):
        """Returns average grayscale value for its pixels"""
        return np.mean(self.pixels)

    def black_pixels(self):
        pixlist = self.pixels[20:-20, 20:-20].flatten()
        return len(pixlist < .01)

    def black_pixel_ratio(self):
        return self.black_pixels()/self.pixels.size

    def sum(self):
        return np.sum(self.pixels[20:-20, 20:-20])
