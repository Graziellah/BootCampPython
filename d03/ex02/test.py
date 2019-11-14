from ScrapBooker import ScrapBooker
import sys
sys.path.append('../ex01')

from ImageProcessor import ImageProcessor

try:
    img = ImageProcessor()
    arr = img.load('../ex01/42AI.png')
    #newImage = ScrapBooker.crop(arr, (100,100))
    #newImage = ScrapBooker.thin(arr, 100, 0)
    newImage = ScrapBooker.juxtapose(arr, 3, 0)
    #newImage = ScrapBooker.
    img.display(newImage)

except ValueError as err:
    print(err)