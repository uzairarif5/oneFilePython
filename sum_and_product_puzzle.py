'''
Two integers m and n between 2 and 50 (inclusive) are chosen. The sum of the integers is given to Sam and the product is given to Prudence. They then have this dialogue:

P: I don't know your sum, Sam
S: I knew you didn't
P: Now I know your sum
S: And now I know your product

What are m and n?

startNum: 2 (you can change this for fun)
endNum: 50 (you can change this for fun)
'''


def printSumProductTable(startNum, endNum):
  productsNum = dict()
  
  for r in range(startNum*2, (endNum*2)+1):
    print(r,"\t|", end="\t")
    for c in range(startNum, (r//2)+1):
      curP = c*(r-c)
      print(curP, end="\t")
      if curP in productsNum:
        productsNum[curP] += 1
      else:
        productsNum[curP] = 1
    print()
  print()

  sumWithUniqueProduct = set()
  for r in range(startNum*2, (endNum*2)+1):
    print(r,"\t|", end="\t")
    containsOne = False
    for c in range(startNum, (r//2)+1):
      print(productsNum[c*(r-c)], end="\t")
      if productsNum[c*(r-c)] == 1:
        containsOne = True
    if containsOne:
      print()
    else:
      sumWithUniqueProduct.add(r)
      print("\tCONTAINS NO ONE!!!")
  print()
      
  productsNum2 = dict()
  for r in sorted(list(sumWithUniqueProduct)):
    print(r,"\t|", end="\t")
    for c in range(startNum, (r//2)+1):
      curP = c*(r-c)
      print(curP, end="\t")
      if curP in productsNum2:
        productsNum2[curP] += 1
      else:
        productsNum2[curP] = 1
    print()
  print()

  for r in sorted(list(sumWithUniqueProduct)):
    print(r,"\t|", end="\t")
    numOfOnes = 0
    for c in range(startNum, (r//2)+1):
      print(productsNum2[c*(r-c)], end="\t")
      if productsNum2[c*(r-c)]==1:
        numOfOnes += 1
    if numOfOnes == 1:
      print("| ONLY ONE 1!!!",end="")
    print()
  print()

printSumProductTable(2, 50)

