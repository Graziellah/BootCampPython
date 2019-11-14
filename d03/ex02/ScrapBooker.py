import numpy as np
import cv2
from PIL import Image

class ScrapBooker:
    @staticmethod
    def crop(array, dimensions, prosition=(0,0)):
        arrayDim = array.shape
        if arrayDim[0] > dimensions[0] and arrayDim[1] > dimensions[1]:
            return array[0:dimensions[0], 0:dimensions[1]]
        else:
            raise ValueError('Given dimensions are bigger than image dimensions')
    @staticmethod
    def thin(array, n, axis):
        pixel = array.shape
        copy = np.copy(array)
        print('ez',copy.shape[0])
        for i in range (copy.shape[0]):
            for j in range(copy.shape[1]):
                if axis == 1 and i == n :
                    copy[i,j] = (0, 0, 0)
                elif axis == 0 and j == n :
                    copy[i,j] = (0, 0, 0)
        return copy

    @staticmethod
    def juxtapose(array, n, axis):
        dimension = array.shape
        coeffH  = int(dimension[0]  / n)
        coeffL  = int(dimension[1]  / n)
        finalImage = np.array(Image.new('RGB',(dimension[0],dimension[1]), color='white'))
        resized_image = cv2.resize(array,(coeffL, coeffH))
        h1, w1 = resized_image.shape[:2]
        for i in range(n):
            if axis == 1:
                array[coeffH :coeffH + h1 , coeffL * i :coeffL * i + w1 ] = resized_image
            else:
                array[coeffH * i :coeffH * i + h1 , coeffL :coeffL + w1 ] = resized_image
        return array