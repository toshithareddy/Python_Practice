testSet = {"Dheeraj",100,True,"Toshi",100,"Laurence"} # Duplicate values are removed
testSet.add("New")
testSet.remove(100)
testSet.pop() # removes random values
val = ("Dheeraj" in testSet) # returns true if value is present
print(testSet)
print(val)