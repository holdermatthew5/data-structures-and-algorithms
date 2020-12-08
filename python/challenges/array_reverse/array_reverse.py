def main(arr):
  return arr[::-1]

newArr = main([1,2,3])

# stretch goal

def mainB(arr):
  secondArr = []
  for i in arr:
    secondArr.insert(0,i)

newArrB = mainB([1,2,3])