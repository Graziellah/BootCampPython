from ColorFilter import ColorFilter
import sys
sys.path.append('../ex01')

from ImageProcessor import ImageProcessor

try:
    img = ImageProcessor()
    arr = img.load('../ex01/42AI.png')
    newImage = ColorFilter.invert(arr)
    #newImage = ColorFilter.to_blue(arr)
    #newImage = ColorFilter.to_green(arr)
    #newImage = ColorFilter.to_red(arr)
    img.display(newImage)

except ValueError as err:
    print(err)