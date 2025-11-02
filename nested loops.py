#nested loops = loop inside a loop
#for every iteration of the outer loop all the iterations of the inner loop

for i in range(1,4): # outer 1,2,3
    print(f"{i}n th time:")
    for j in range(1,3):  #inner 1,2
        print(j)
        
#output
'''
1n th time:
1
2
2n th time:
1
2
3n th time:
1
2
'''
matrix = [[1, 2], [3, 4]]

for row in matrix:
    for element in row:
        print(element)

'''o/p:
1
2
3
4
''' 
matrix = [[1,2] ,[3,4]]
s = 0
for i in matrix :
    #s = 0
    for ele in i :
        s+= ele
        #print(s)
print(s) 
'''
o/p:
1
3
4
10
'''

matrix = [[1,2] ,[3,4]]
#s = 0
for i in matrix :
    s = 0
    for ele in i :
        s+= ele
        print(s)
#print(s) #o/p - 1,3,3,7


matrix = [[1,2] ,[3,4]]
s = 0
for i in matrix :
    #s = 0
    for ele in i :
        s+= ele
        print(s)
#print(s) #o/p - 1,3,6,10


matrix = [[1,2] ,[3,4]]
#s = 0
for i in matrix :
    s = 0
    for ele in i :
        s+= ele
        #print(s)
print(s) #o/p - 7



'''Keep taking input repeatedly.

Stop when user enters 0.

Keep track of last number entered before 0.

Maintain a running sum of all numbers entered '''

s = 0
while True:
    n = int(input())
    s +=n
    if n == 0:
        print(s)
        break
