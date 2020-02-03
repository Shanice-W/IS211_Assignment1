#!/usr/bin/env python
# coding: utf-8

# In[20]:


class ListDivideException(Exception):
    pass

class ZeroDivide(Exception):
      pass

   
def listDivide(numbers, divide=2):
    try: 
        if not isinstance(numbers, list):
            raise ListDivideException
            
        if divide == 0:
            raise ZeroDivide
            
        divisiblenumbers = []
        if len(numbers) == 0:
            print(0)
        else: 
            for x in numbers:
                if x%divide == 0:
                    divisiblenumbers.append(x)
                
            print(len(divisiblenumbers))
        
    except ListDivideException:
        print("Type Error: First parameter must be a list")
    except ZeroDivide:
        print("Value Error: Divide value cannot be zero")
 

def ListDivideTest(numbers, divide=2):
    try: 
        if not isinstance(numbers, list):
            raise ListDivideException
            
        if divide == 0:
            raise ZeroDivide
            
        divisibles = []
        if len(numbers) == 0:
            return 0
        else: 
            for x in numbers:
                if x%divide == 0:
                    divisiblenumbers.append(x)
                    
    except ListDivideException:
        print("Type Error: First parameter must be a list")
    except ZeroDivide:
        print("Value Error: Divide value cannot be zero")
    except Exception as ex:
        print(str(ex))
     
listDivide([1,2,3,4,5])
listDivide([2,4,6,8,10])
listDivide([30, 54, 63,98, 100], divide=10)
listDivide([])
listDivide([1,2,3,4,5], 1)


testListDivide([1,2,3,4,5])
testListDivide('dog')
testListDivide([30, 54, 63,98, 100], divide=0)

