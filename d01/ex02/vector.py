class Vector:
    def __init__(self, initialValue):
        self.values = []
        self.size = 0
        self.initValues(initialValue)

    def initValues(self, initialValue):
        if isinstance(initialValue, int):
            self.size = 3
            for i in range(0, 3):
                self.values.append(float(i))
        elif isinstance(initialValue, list):
            for elem in initialValue:
                if not isinstance(elem, float):
                    print("Is not float", elem)
                    return
            self.size = len(initialValue)
            self.values = self.values + initialValue
        elif isinstance(initialValue, tuple) and len(initialValue)== 2:
            for i in range(initialValue[0], initialValue[1]):
                self.values.append(float(i))
            self.size = len(self.values)
        print("slef", self.values, self.size)

    def __add__(self, other):
        sumValue = []
        if isinstance(other, Vector):
            print('is vector')
        else:
            for i in range(0, self.size):
                result = self.values[i]+ other
                sumValue.append(result)
            return Vector(sumValue)

    def __radd__(self, other):
        return Vector.__add__(self, other)
    
    def __sub__(self, other):
        sumValue = []
        if isinstance(other, Vector):
            print('is vector')
        else:
            for i in range(0, self.size):
                result = self.values[i] - other
                sumValue.append(result)
            return Vector(sumValue)

    def __rsub__(self, other):
        return self.__sub__(other)
    
    def __mul__(self, other):
        sumValue = []
        if isinstance(other, Vector):
            print('is vector')
        else:
            for i in range(0, self.size):
                result = self.values[i] * other
                sumValue.append(result)
            return Vector(sumValue)

    def __rmul__(self, other):
        return Vector.__mul__(self, other)
    
    def __truediv__(self, other):
        sumValue = []
        if isinstance(other, Vector):
            print('is vector')
        else:
            for i in range(0, self.size):
                result = self.values[i] * other
                sumValue.append(result)
            return Vector(sumValue)

    def __rtruediv__(self, other):
        return Vector.__truediv__(self, other)

    def __str__(self):
        return "Vector " +  str(self.values)
    
    def __repr__(self):
        return {
            'values': self.values,
            'size': self.size
        }


