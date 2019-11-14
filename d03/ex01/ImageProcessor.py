import matplotlib.image as mpimg
import numpy as np
import matplotlib.pyplot as plt


class ImageProcessor:
    def __init__(self):
        self.image = None
        self.imageArray = []
    def load(self, path):
        img = mpimg.imread(path)
        self.imageArray = img
        dim = img.shape
        print("Loading image of dimensions ", dim[0], " x ", dim[1] )
        return img
    def display(self, img):
        if img.dtype == np.float32 or img.dtype == np.uint8: 
            if img.dtype == np.float32:
                img = (img * 255).astype(np.uint8)
            plt.imshow(img)
            plt.show()
