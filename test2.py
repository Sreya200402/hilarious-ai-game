"""
#migration hackerrank
n = int(input())
lst = list(map(int,input().split()))
fre = {}
for i in lst:
    if i in fre:
        fre[i] += 1
    else:
        fre[i] = 1
max_fre = 0
for c in fre.values():
    if c > max_fre:
        max_fre = c
        
b_type = None
for m in fre:
    if fre[m] == max_fre:
        if b_type is None or m < b_type:
            b_type = m
print(b_type)
"""

#student grading
n = int(input())
lst = []
for i in range(n):
    lst.append(int(input()))
for i in lst:
    if i < 38 or i % 5 < 3:
        print(i)
    else:
        print(i + 5 - i% 5)


#or output in terms of list
n = int(input())
lst = []
for i in range(n):
    lst.append(int(input()))

result = []
for i in lst:
    if i < 38 or i % 5 < 3:
        result.append(i)
    else:
        result.append(i + 5 - i % 5)

print(result)
