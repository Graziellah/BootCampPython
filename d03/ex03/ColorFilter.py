class ColorFilter:
    @staticmethod
    def invert(array):
        dimension = array.shape
        for i in range(dimension[0]):
            for j in range(dimension[1]):
                r,g,b = array[i][j]
                array[i][j] = (255 - r, 255 - g, 255 - b)
        return array
    @staticmethod
    def to_blue(array):
        dimension = array.shape
        for i in range(dimension[0]):
            for j in range(dimension[1]):
                r,g,b = array[i][j]
                array[i][j] = (255, 255,b)
        return array
    @staticmethod
    def to_green(array):
        dimension = array.shape
        for i in range(dimension[0]):
            for j in range(dimension[1]):
                r,g,b = array[i][j]
                array[i][j] = (255, g, 255)
        return array
    @staticmethod
    def to_red(array):
        dimension = array.shape
        for i in range(dimension[0]):
            for j in range(dimension[1]):
                r,g,b = array[i][j]
                array[i][j] = (r, 255, 255)
        return array