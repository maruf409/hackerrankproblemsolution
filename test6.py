n = int(input("Enter number of elements : "))
lst = []
# iterating till the range
for i in range(0, n):
    ele = str(input())

    lst.append(ele)  # adding the element

print(len(lst))
