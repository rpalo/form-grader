from skimage import io
import numpy as np

import sys

image = io.imread(sys.argv[1])

print(np.mean(image))
