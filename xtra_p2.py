"""
Purpose: 

Practice writing functions using positional and keyword arguments.
Practice logging functions using the util_datafun_logger module
Log each time the function is called (along with its arguments)
Log the result of each function just before you return the result

Author of Edits: Sarah DeConink
    Many functions were copied and modified to edit this script

 ----------------------------------------------------------
 UNIT TESTS BELOW - SPECIFY CORRECT BEHAVIOR
 ----------------------------------------------------------

>>> sum_two(1,2)
3

>>> sum_two("hello"," world")
'hello world'

>>> sum_rectangle_list( [1,1,3,3] )
8

>>> transform_using_keyword_args_with_default_values()
'bea'

>>> transform_using_keyword_args_with_default_values(reverse=True)
'aeb'

>>> transform_using_keyword_args_with_default_values(input="hello", reverse=True)
'leh'

>>> sum_any_using_args(1,1,1,2)
5

>>> sum_any_with_keyword_arguments_kwargs(a=1,b=2,c=3)
6

@uses doctest - to verify our functions are correct
"""

import doctest

from util_datafun_logger import setup_logger
logger, logname = setup_logger(__file__)


# Add functions to get the unit tests to pass 
# Log each time the function is called (along with its arguments)
# Log the result of each function just before you return the result

def sum_two(first, second):
    """Return the sum of any two arguments."""
    logger.info(f"CALLING sum_two({first},{second})")

    sum = first + second

    logger.info(f"RETURNING {sum}")
    return sum

def sum_rectangle_list(list_rectangle):
    """Return the sum of four numbers in a list."""
    logger.info(f"CALLING sum_rectangle_list({list_rectangle})")

    sum = 0
    for value in list_rectangle:
        sum = sum + value
        
    logger.info(f"RETURNING {sum}")
    return sum

def sum_any_using_args(*args):
    """Return the sum of numbers, using built-in *args."""
    logger.info(f"CALLING sum_any_using_args({args})")
    sum = 0
    for x in args:
        sum += x  # Use the popular and concise version of sum = sum + x

    logger.info(f"RETURNING {sum}")
    return sum

def sum_any_with_keyword_arguments_kwargs(**kwargs):
    """Return the sum of numbers, using built-in keyword args, **kwargs."""
    logger.info(f"CALLING sum_any_with_keywords({kwargs})")
    sum = 0
    for value in kwargs.values():  # use values() - name doesn't matter
        sum += value  # Use the popular and concise version of sum = sum + x
    
    logger.info(f"RETURNING {sum}")
    return sum



# Fix this function to get just the first 3 letters (possibly reversed)
def transform_using_keyword_args_with_default_values(input="bearcat", reverse=False):
    '''Return a string with just the first 3 letters of input string. 
    If reverse is True, reverse the first 3 letters. 
    If reverse is omitted or False, return the first 3 letters reversed. 
    @kwargs:
        input: a string, default "bearcat"
        reverse: a boolean, default False'''
    
    s = f"CALLING transform_using_keyword_args_with_default_values(input={input}, reverse={reverse})"
    logger.info(s)

    result = input[:3:1]
    if reverse:
            result = input[2::-1]
        
    logger.info(f"RETURNING {result}")
    return result


if __name__ == "__main__":

    # -------------------------------------------------------------
    # Call some functions and execute code!
    # Nothing below here needs to change
    # -------------------------------------------------------------

    transform_using_keyword_args_with_default_values()
    transform_using_keyword_args_with_default_values(reverse=True)
    transform_using_keyword_args_with_default_values(input="hello", reverse=True)

    logger.info("===========================================================")
    logger.info("Running doctest.testmod() function to unit test our code")
    logger.info("===========================================================")

    # Run doctest and log the results

    doctest_result = doctest.testmod()
    if doctest_result.failed == 0:
        logger.info("All tests passed!")
    else:
        logger.error(f"{doctest_result.failed} tests failed!")

    logger.info("Script complete. More info in the log file.")
        
    # Read log file and print it to the terminal
    with open(logname, 'r') as file_wrapper:
        print(file_wrapper.read())