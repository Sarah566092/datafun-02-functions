"""

Purpose: Illustrate the built-in statistics module. This is modified from Module 1 easy_stats

Author of Edits: Sarah DeConink
Date: 5/16/2023

Domain: Food
Y-values: Hot Dog sales at a food truck on a given day
X-values: Number of condiments available at the food truck for the hot dogs

VS Code Menu / View / Command Palette / Python Interpretor
Must be 3.10 or greater to get the correlation and linear regression.

Uses only Python Standard Library modules.

@ uses statistics module for descriptive stats
@ uses sys module for checking Python version

"""
import statistics 
import sys  

from util_datafun_logger import setup_logger
logger, logname = setup_logger(__file__)

# Descriptive: Univariant Data for number of hot dog sales at food truck on a given day..................................

# univariant data (one varabile, many readings)
uni_data = [
    5,
    11,
    14,
    19,
    25,
    31,
    37,
    39,
    44,
    49,
    55,
    63,
    69
]
logger.info("hot dog sales on different days = " + str(uni_data))

# Descriptive: Averages and measures of central tendency

mean = statistics.mean(uni_data)
median = statistics.median(uni_data)
mode = statistics.mode(uni_data)

# log use variable colon formatting to avoid unnecessary digits (e.g. .2f)

logger.info(f"mean   = {mean:.2f}")  
logger.info(f"median = {median:.2f}")
logger.info(f"mode   = {mode:.2f}")

# Descriptive: Measures of spread

var = statistics.variance(uni_data)
stdev = statistics.stdev(uni_data)
lowest = min(uni_data)
highest = max(uni_data)
range_1 = highest - lowest

# changed to f-strings and use 2 decimal places (like we did above)
logger.info(f"var    = {var:.2f}")
logger.info(f"stdev  = {stdev:.2f}")
logger.info("lowest = " + str(lowest))
logger.info("highest= " + str(highest))
logger.info("range = " + str(range_1))


# Descriptive: Univariant Data.........................

# the number of hot dog sales on a given day depending on how many condiments are available
xtimes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
yvalues = uni_data

# if the lists are not the same size,
# log an error and quit the program
if len(xtimes) != len(yvalues):
    logger.error("ERROR: The related sets are not the same size.")
    logger.error(f"      {len(xtimes)}!={len(yvalues)}")
    quit()

# check the Python version before using the correlation function
logger.warn("Correlation requires Python version 3.10 or greater.")
logger.warn(f"Your version is {sys.version_info.major}.{sys.version_info.minor}")

# if the Python version is too old, we can quit now
if sys.version_info.minor < 10:
    logger.error("Please update Python to 3.10 or greater")
    logger.error("or use View / Command Palette / Python: Select Interpreter")
    logger.error("to get a newer one.")
    quit()

# If we're still here, use the correlation function from the statistics module
xx_corr = statistics.correlation(xtimes, xtimes)
xy_corr = statistics.correlation(xtimes, yvalues)

# log the information 
logger.info("Here's some data on hot dog sales depending on how many condiments are availble on a food truck:")
logger.info(f"Number of condiments today:{xtimes}")
logger.info(f"Hot Dog Sales today:{yvalues}")
logger.info(f"correlation between condiments and condiments = {xx_corr:.2f}")
logger.info(f"correlation between condiments and hot dog sales = {xy_corr:.2f}")

# Calculate slope and intercept of a line


# Call linear_regression() function -
# and get back 2 values: slope and intercept
# describing the 'best fit' line through the data
slope, intercept = statistics.linear_regression(xtimes, yvalues)

# Choose an x value off in the future (future x)
future_x = 15

# Extend the line out into the unknown future
# and read the value (of future y)
future_y = round(slope * future_x + intercept)

logger.info("Here's some bivariant data (2 variables, together):")
logger.info(f"x:{xtimes}")
logger.info(f"y:{yvalues}")
logger.info("Calculate the slope and intercept of a best fit straight line:")
logger.info(f"   slope = {slope:.2f}")
logger.info(f"   intercept = { intercept:.2f}")
logger.info("Let's use our best fit line to PREDICT a future value.")
logger.info(f"   If we provide 15 condiments on the food truck = {future_x:d},")
logger.info(f"   we predict the value of hot dog sales will be { future_y:d}.")
logger.info("15 condiments is a lot!!!")
logger.info("Remember to close the app. Control c (or d or z maybe) to close it.")


# Use built-in open() function to read log file and print it to the terminal
with open(logname, 'r') as file_wrapper:
    print(file_wrapper.read())