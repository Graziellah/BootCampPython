import numpy as np

class NumPyCreator:
    def __init__(self):
        self.array = None
    def from_list(self, data, dtype=None):
        if isinstance(data,list):
            a = np.array(data)
            print(a)
    def from_tuple(self, data, dtype=None):
        if isinstance(data,tuple):
            a = np.array(data, dtype=dtype)
            print(a)
    def from_iterable(self,data, dtype=None):
        for i in data:
            i+=1
        print(i)
        a = np.arange(i, dtype=dtype)
        print(a), 
    def from_shape(self,data, value=0, dtype=None):
        a = np.full(data, value, dtype=dtype)
        print(a)
    def random(self,data,dtype=None):
        a = np.random.rand(data[0],data[1], dtype=dtype)
        print(a)
    def identity(self,data,dtype=None):
        a = np.identity(data, dtype=dtype)
        print(a)




npc = NumPyCreator()
npc.from_list([[1,2,3],[6,3,4]])
npc.from_tuple(("a", "b", "c"))
npc.from_iterable(range(5))
shape=(3,5)
npc.from_shape(shape, 8)
npc.random(shape)
npc.identity(4)