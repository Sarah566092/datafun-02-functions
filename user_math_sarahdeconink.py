"""
Purpose: This script will explore mathematical functions in the math module.

Author: Sarah DeConink
Date: 5/16/2023

Domain: Food

Use math funcions to determine what is needed in a bakery

"""

import math

from util_datafun_logger import setup_logger
logger, logname = setup_logger(__file__)

def get_cake_area(length, width):
    
    # Use a try / except / finally block when something 
    # could go wrong
    logger.info(f"The cake dimensions are (length= {length}inches by width= {width}inches)")

    try: 
        cake_area = length * width
        logger.info(f"The cake area to frost is {cake_area} square inches")
        return cake_area
    except Exception as ex:
        logger.error(f"Error: {ex}")
        return None

# Call some functions and execute code!
if __name__ == "__main__":

    logger.info("Explore some functions in the math module that could be good for bakery business")
    logger.info(f"math.comb(8,2) = {math.comb(8,2)}")
    logger.info(f"math.perm(8,2) = {math.perm(8,2)}")
    logger.info(f"math.comb(5,2) = {math.comb(5,2)}")
    logger.info(f"math.perm(5,2) = {math.perm(5,2)}")
    logger.info(f"math.mod(6) = {math.modf(6)}")
    logger.info("")

    logger.info("TRY: Call get_cake_area() function with a different values.")
    get_cake_area(3,2)
    get_cake_area(5,8)
    get_cake_area(9,13)
    get_cake_area('five','eight')
    logger.info("")
        
    # Read log file and print it to the terminal
    with open(logname, 'r') as file_wrapper:
        print(file_wrapper.read())

#Write another function that calls a function from the math module
def get_special_order_invoice(number_cupcakes, number_quiches, number_danishes):
    
    # Use a try / except / finally block when something 
    # could go wrong
    logger.info(f"Special Order: # of cupcakes= {number_cupcakes}, # of quiches= {number_quiches}, # of danishes= {number_danishes})")

    try:
        total_bill = math.fsum([2.56 * number_cupcakes, 4.89 * number_quiches, 3.19 * number_danishes])
        logger.info(f"Your bill is ${total_bill:.2f}")
        return total_bill
    except Exception as ex:
        logger.error(f"Error: {ex}")
        return None

# Call some functions and execute code!
if __name__ == "__main__":
    
    logger.info("TRY: Call get_special_order_invoice() function with a different values.")
    get_special_order_invoice(10, 4, 9)
    get_special_order_invoice(0, 1, 30)
    get_special_order_invoice(20, 20, 20)
    logger.info("")
        
    # Read log file and print it to the terminal
    with open(logname, 'r') as file_wrapper:
        print(file_wrapper.read())

# Write another function that adds tax to an order
def tax_on_order(total_bill, tax_rate_as_decimal):
    order_with_tax = total_bill * (1 + tax_rate_as_decimal)
    logger.info(f"If your food order is ${total_bill}, then your total with tax is ${order_with_tax:.2f}")
    return order_with_tax

# Call some functions and execute code!
if __name__ == "__main__":
    
    logger.info("TRY: Call tax_on_order() function with different values.")
    tax_on_order(100, .11)
    tax_on_order(350, .05)
    tax_on_order(20, .1)
    tax_on_order(89, .30)
    logger.info("")
        
    # Read log file and print it to the terminal
    with open(logname, 'r') as file_wrapper:
        print(file_wrapper.read())


# Write another function that suggests a tip
def tip_suggestion(order_with_tax):
    if order_with_tax <= 50:
        tip_rate = .2
        order_with_tip = order_with_tax * (1 + tip_rate)
        logger.info(f"Your food order with {tip_rate * 100}% tip should be ${order_with_tip}")
    else:
        tip_rate = .18
        order_with_tip = order_with_tax * (1 + tip_rate)
        logger.info(f"Your food order with {tip_rate * 100}% tip should be ${order_with_tip}")
    return order_with_tip    

# Call some functions and execute code!
if __name__ == "__main__":
    
    logger.info("TRY: Call tip_on_order_() function with different values.")
    tip_suggestion(100)
    tip_suggestion(288)
    tip_suggestion(50)
    tip_suggestion(20)
    logger.info("")
        
    # Read log file and print it to the terminal
    with open(logname, 'r') as file_wrapper:
        print(file_wrapper.read())
