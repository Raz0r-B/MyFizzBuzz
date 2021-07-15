'''
Created by Brandon

A fun exercise, probably already famous, but made famous to me by Tom Scott @ https://youtu.be/QPZ0pIK_wsc


This is my interpretation, created completely independently  

The inspiration for my code and layout is to offer ease of customization and readability

'''


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def fizzBuzz(fizz, buzz, rangeMax): 
    response= []

    # Set range for iterations to play through
    for i in range(1,rangeMax+1):
        response= []
        #Set Fizz Parameter
        if i % fizz == 0:
            response.append('Fizz')
        
    
        if i % buzz == 0:
            response.append('Buzz')
    
        
        if len(response) == 0: print (i)
        else: print(''.join(response))

 #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~       

fizzBuzz(fizz = 3, buzz = 3, rangeMax = 100)