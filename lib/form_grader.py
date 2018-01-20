"""Testing things out"""
import sys

from matplotlib import pyplot as plt
from skimage import io
from skimage.color import rgb2gray
from skimage.exposure import equalize_hist

import block
from form import Form

image = io.imread(sys.argv[1])
image_gray = rgb2gray(image)
image_sharp = equalize_hist(image_gray)
config = {
    "row_start": 541,
    "row_end": 2207,
    "row_count": 28,
    "col_start": 820,
    "col_end": 1230,
    "col_count": 7,
    "image": image_gray
}
f = Form.from_dict(config)
print(f.read())
io.imshow(image_gray)
plt.show()


