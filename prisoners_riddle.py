import numpy as np

'''
- 100 prisoners numbered 1 to 100
- Paper with their numbers are randoly placed in 100 boxes in a room
- Each prisoner may enter the room one at a time and checl 50 boxes
- They must leave the room exactly as they foudn it and can't communicate with others after
- If all 100 find their number they will all be freed; of even one fails they will all be executed.

Find a strategy that puts their chances to around 1/3
'''

def randomSelect(boxes: dict, prisonerNum: int):
  #selectedBoxes is the boxes the prisoner has decided to check (50 chosen randomly)
  selectedBoxes = np.random.choice(list(boxes.keys()), 50, replace=False)
  for boxNum in selectedBoxes:
    if prisonerNum == boxes[boxNum]:
      return True
  print("randomSelect:", prisonerNum, "did not find their number.")
  return False
  
def loopSelect(boxes: dict, prisonerNum: int):
  #select random box like 48, check value inside
  #if value does not match prisoner number, then the value number if the number for the next box to open
  #after many checks, if a loop completes, then open a box at random and start new loop
  counter = 1
  boxNum = prisonerNum
  while counter <= 50:
    if(prisonerNum == boxes[boxNum]):
      return True
    counter += 1
    boxNum = boxes[boxNum]
  print("loopSelect:", prisonerNum, "did not find their number.")

  while (prisonerNum != boxes[boxNum]):
    counter += 1
    boxNum = boxes[boxNum]
  print("counter", counter)
  return False

def testMethod(method):
  boxes = dict()
  papers = np.random.permutation(np.arange(1,101, dtype=np.int8))
  for i in range(1, 101):
    boxes[i] = int(papers[i-1])
  win = True
  for prisonerNum in range(1, 101):
    if (not method(boxes, prisonerNum)):
      win = False
      break
  return win

if(__name__ == "__main__"):
  if testMethod(randomSelect):
    print("randomSelect passed.")
  else:
    print("randomSelect has failed.")
  print()
  if testMethod(loopSelect):
    print("loopSelect passed.")
  else:
    print("loopSelect has failed.")