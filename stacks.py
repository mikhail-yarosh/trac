#!/bin/python3

h1 = [3, 2, 1, 1, 1]
h2 = [4, 3, 2]
h3 = [1, 1, 4, 1]

def stackSum( stack ):
  sum = 0
  for i in stack:
    sum += i 
  return sum

def getSumsDict( stack ):
  stackSum = 0
  stackSums = {}
  stackSteps = 0
  for i in stack[::-1]:
    stackSteps +=1
    stackSum += i
    stackSums[stackSteps] = stackSum
  return stackSums

def main():
  # Decided to use dictionary just because it provides more functionality (as a stack height as a pizzas number to stay in each stack)
  h1Sums = getSumsDict(h1)
  h2Sums = getSumsDict(h2)
  h3Sums = getSumsDict(h3)
  matchHeights = 0

  if list(h1Sums.values())[-1] == list(h2Sums.values())[-1] == list(h3Sums.values())[-1]: 
    return(list(h1Sums.values())[-1])

  for key in h3Sums:
    if h3Sums[key] in list(h2Sums.values()):
      if h3Sums[key] in list(h1Sums.values()):
        matchHeights = h3Sums[key]
  print(matchHeights)

main()
