
#testList = [50,100,"Laurence","Hello",50,100,True]
#a,b,c,d,e,f,g = testList # assining variables should be perfect that is no.of variables = no.of values
#testList.insert(2,"john")
#testList.append("End") #  adding values
#testList.remove(100)
#testList.pop() # removes last value and will remove particular value if we give related index within the pop()
#val = testList.pop()
#testList[0] = "New" # updating value according to indexed value
#del testList[1]
#testList.clear() # removes entire list
#print(testList[:3]) # returns back values from index 0 to 2
#print(testList.index("john")) # returns index of the given value,if there are same values with different index then it returns thr first assigned index
#print(testList)
#print(testList[2])
#print(c)
#print(len(testList))
#print(testList[-1]) # returns the last value
#print(testList[1:3]) # returns indexed values 1,2 but not 3

#val = ("john" in testList) # if value is present in list then true else false
#val = ("j.john" in testList)
#print(val)

testList = ["Laurence","World","Hello","World"]
#testList.sort() # sorts according to alphabet
testList.reverse()
copyList = testList.copy()
copyList.append("Neww")
print(copyList)
print(testList)
