#examples of decorators along with high functions and closures 
from functools import wraps #decorators for decorators
#additional decorator lib can be imported to be used with iur custom made decorators 

# first class functions : 
# assign functions to objects (variables) so that the variables can be used as the functions would be used : 
from fileinput import filename
import logging
from time import time


def square(x):
    return x*x

f=square
print(square)
print(f(5))

#variable f has got the same functionality as the square function , DO NOT add parenthesis () to the function as python will try running the function



# Higher-order functions:  functions that take other functions as paramaters 

#example
def my_map(func, arg_list):
    result =[]
    for i in arg_list:
         result.append(func(i))
    return result

#the my_map function will take a different function (e.g math function) and get applied to the argument list .


# closures:
# closure is a record storing a function together with the environment 
# definition : A closure is an inner function that remembers and has access to variables in the local scope in which it was created even after the outer function has finished executing it 
# example:
def outer_function(msg):
    message = msg
    
    def inner_function():
        print(message)
    return inner_function
#note that we are returning inner_function without executing it

hi_func = outer_function('Hi')
hello_func =outer_function('Hello')

#calling the variables as functions , hi_func will have access to the functions of outer_function and will return the inner function with saved variable from outer function without having a direct access to the variable 
hi_func()

#example 2 HTML tag:

def html_tag(tag):
      
    def wrap_text(msg):
        print(f'<{tag}> {msg} <{tag}>')

    return wrap_text
#note that we are returning wrp_text without executing it

html_tag_h1 =html_tag('h1') # we can create a dedicated tag variable and then re-use it as much as possible
html_tag_p =html_tag('p')

html_tag_h1('this is H1 tag in HTML')
html_tag_h1('this is ANOTHER H1 tag')

# decorators:
# a function that takes another function as na arg, adds additional functionality and returns another function,. All of this without altering the source code of the original function  

# example of a decorator in use : 

def decorator_function(original_function):
    def wrapper_function():
        print('wrapper executed this before {}.'.format(original_function.__name__))
        return original_function()
    return wrapper_function

@decorator_function
def display():
    print('dsiplay function ran')

#a different way of invoking the decorator function but in a different syntax :
# display = decorator_function(display)


# example of a decorator class (based off decorator function example

class decorator_class(object):
    
#initialise the class
    def __init__ (self, original_function):
        self.original_function = original_function

#call the class so that it can be used as a decorator
    def __call__(self, *args, **kwargs):
#the class can take any number of positional or keyword params with *args **kwrags
        print('call method executed THIS before the function {}'.format(self.original_function.__name__))
        return self.original_function(*args, **kwargs)

#we call a decorated class in the same way as decorated function
@decorator_class
def display_info(name, age):
    print(f'display function ran with the following arguments ({name}, {age}) ')

# display_info ()
#or
# display=decorator_class()


#common uses for decorators : 
# EXAMPLE 1 - logging
def log_function(original_function):
    import logging
    logging.basicConfig(filename='{}.log'.format(original_function.__name__), level=logging.INFO)
    
    @wraps(original_function) #additional built in decorators added to custom made docorators 
    def wrapper_2 (*args, **kwargs):
        logging.info(
            'Ran with args: {} and kwargs {}'.format(args,kwargs))
        return original_function(*args, **kwargs)
    return wrapper_2
    
    
#EXAMPLE 2 - timing the run time of the function , wrapper captures the start time (t1) tuns the OG function and then captures the difference betwee launch and closing time (t2). the time it took to process the funcion is generated and the OG function is returned 
#for test purposes a time delay might need to be added (time.sleep(5)) in the OG function
def my_timer_function(original_function):
    import time
    
    @wraps(original_function) #additional built in decorators added to custom made docorators 
    def wrapper_3(*args, **kwargs):
        t1=time.time()
        result=original_function(*args,**kwargs)
        t2 =time.time()-t1
        print(f'{original_function.__name__} ran in : {t2} sec.')
        return result
    
    return wrapper_3


#example of the OG function we are testing the decorators against 

import time #needed for a edge test case for @my_timer_function 
 
@my_timer_function
@log_function
 
def display_info2(name, age):
    time.sleep(2)
    print(f'display function ran with the following arguments ({name}, {age}) ')


display_info2('raf', 39)
#it is possible to stack multiple functions, one on top of another , need to: from functools import wraps and add wraps decorators to our custom made decorators so that when custom made docorators are stacked the correct info gets logged