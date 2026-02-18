import numpy as np

def createArrays():
    arr1 = np.array([1, 2, 3, 4])
    arr2 = np.array([4, 3, 2, 1])
    return arr1, arr2

def addArrays(arr1,arr2):
    return np.add(arr1, arr2)

def subtractArrays(arr1, arr2):
    return np.subtract(arr1, arr2)

#print opperations
if __name__ == "__main__":
    arr1, arr2 = createArrays()
    print("Numpy Array 1", arr1)
    print("Numpy Array 2", arr2)
    print("Numpy adding", addArrays(arr1, arr2))
    print("Numpy subtracting", subtractArrays(arr1, arr2))