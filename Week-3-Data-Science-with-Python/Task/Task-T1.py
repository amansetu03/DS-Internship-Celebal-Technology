import numpy as np
class NpArray:
    def __init__(self) -> None:
        self.arr = np.array(0)

    def genarateArr(self,size):
        self.arr = np.random.randint(-10,15,size)
        self.display()

    def display(self):
        print(self.arr)

    def findSum(self):
        s = np.sum(self.arr,axis=1)
        print("sum of each row: ",s)
if __name__ == "__main__":
    n = NpArray()
    for i in range(3):
        print(f"\n*************** Test-{i+1} *****************")
        n.genarateArr((4,4))
        n.findSum()