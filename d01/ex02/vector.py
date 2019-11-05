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
            for i in self.values:
                result = self.values + other
                sumValue.append(result)
            return Vector(sumValue)


