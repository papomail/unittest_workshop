def add(a,b):
    return a + b

def substract(a,b):
    return a - b 

def multiply(a,b):
    return a ** b

def divide(a,b):
    if b == 0:
        raise ValueError('Cannot divide by 0')
    return a/b






def complicated_function(a,b,c,d,e,f):
    the_value=multiply( substract(add(a,b),divide(d,c)), e )
    print(f'The value you need is {the_value}')
    

complicated_function(5,6,5,8,1,3)
