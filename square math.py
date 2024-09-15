def squareItOut(l):
    ll = []
    for i in l:
        ll.append(i**2)
    return locals

li = [1,2,3,4,5,6,7,8,9,10]
print("Original List", li)

resultList = squareItOut(li)
print("Squared list is ", resultList)