import numpy as np
class NpArray:
    def __init__(self) -> None:
        self.arr = np.array(0)

    def genarateArr(self,size):
        self.arr = np.random.randint(-15,15,size)
        self.display()

    def display(self):
        print(self.arr)

    def replaceMin(self):
        m = np.min(self.arr,axis=None)
        self.arr = np.where(self.arr != m,self.arr,0)
        print(f"minimum value = {m}\nNew Array: ")
        self.display()

if __name__ == "__main__":
    n = NpArray()
    for i in range(2):
        print(f"\n*************** Test-{i+1} *****************")
        print("original array")
        n.genarateArr((5,5))
        n.replaceMin()