#input formatting
#int , float , bool , str , list , tuple ,dict , set

#int()

   a = int(input())
   
#float()
   
  a = float(input())

#str()
  
   a = input().strip()

#list[]

   a = input().split() #strings list
   
   a = list(map(int , input().split()))

# tuple()

   q = tuple(input().split())
   
   q = tuple(map(int , input().split()))

#dict

   d = eval(input()) # dict with proper syntax

#set

   inp = set(input().split())

   int_input = set(map(int , input().split())
