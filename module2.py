#modules
#user defined modules
'''
import module1
print(module1.number)
print(module1.string)
module1.greet()
'''


###
import module1 as m
print(m.number)
print(m.string)
m.greet()
# when i run this by commenting above and below code . first run module 1
#it gives Module1 as output after runing the module2 it gives 100 , python
#and hello worls as output
'''
#when alone running this Module2  without running the module 1 the o/p is
Module1
100
python
hello world!!! since we are importing module 1

if i want to print'module1' when rumning module1 and when running module2 it prints the above
print statments run the print statements for individual respected files i.e even though i import the
module 1 in module2 should print the statements thst belong to module2.. we use

if __name__ == "__main__": # python built name for that file
     main()
'''

'''
###
from module1 import greet , number
print(number)
greet()
'''
