L = [4,5,1,2,9,7,10,8]
print("Original List:", L)

count = 0

for i in L:
    count = count + 1

print("\nsum = ", count )

avg = count/len(L)
print("average is ", avg)

L.sort()

print("Sorted list:", L)

print("\nSmallest element is", L[0])

print("\nLargest element is: ", L[-1])