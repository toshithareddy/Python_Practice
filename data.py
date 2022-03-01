# integer type
a = 5
# string type
a = "5"
# boolean type
a = True
print(type(a))
# LISTS type
testList = [50,"50",True] # order of values can be changed
print(testList)
print(testList[1]) # printing value according to index
print(len(testList))
print(type(testList))
# Tuple type
testTuple = (50,"50",True) # order of values cannot be changed
print(testTuple)
print(testTuple[1]) # printing value according to index
print(len(testTuple))
print(type(testTuple))
# Test Set
testset = {50,"50",50,"100",True} # duplicate values are deleted
print(testset)
#print(testset[1]) # printing value according to index
print(len(testset))
print(type(testset))
# Dictionary type
testDic = {"first":50,"second":"100","third":True,"a":50,"b":"50"}# dont take duplicate values {"first":50,"second":"100","third":True,"a":50,"a":"Last"}
print(testDic)
print(len(testDic))
print(type(testDic))

