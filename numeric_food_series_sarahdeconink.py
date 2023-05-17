'''
Purpose: Create a class that inherits everything from NumericSeries and adds
attributes and/or behavior specific to Food. 

If you don't need to add specialized attributes or behavior, 
you can just use the original NumericSeries class directly. 
No subclassing required.

We get all of our parent's attributes and methods for free (no coding required).

Food adds:

- a meal attribute

Author of derived class: Sarah DeConink
Date 5/16/23

'''

# From the name of the module (the file name without .py), import the class we want to inherit from
from numeric_series import NumericSeries

# From the util_datafun_logger module, import the setup_logger function
from util_datafun_logger import setup_logger


class NumericFoodSeries(NumericSeries):
    """
    A class representing a numeric series customized for counting food calories in a meal.

    (Additional) Attributes:
       meal (string): the meal of the day
    """

    def __init__(self, name, units, data, meal):
        """
        Initialize the object when first created using the arguments passed in.
        Every class needs an __init__ method to construct a new object.

        @args:
            self (object): the object being created that will hold the real data
            name (str): a short name for this list of numeric data
            units (str): the units in which the data is measured
            data (list): the list of numeric data to be held by the object
            meal (str): the meal of the day

        """

        # First, initialize the parent (super) class with parent's attributes
        # By calling the super constructor method
        super().__init__(name, units, data)

        # Then, initialize our additional specialized attributes
        self.meal = meal

    def __str__(self):
        """
        Return a string representation of the instantiated object.
        The two underscores before and after indicate this is a special method.
        Every class needs a __str__ method that returns a string representation of the object.
        Be sure to use self.attribute_name so you use the object's attribute, not a local variable! 

        Returns:
            str: a string representation of the instantiated object
        """
        str = f"NumericFoodSeries with name={self.name}, units={self.units}, meal={self.meal}, and {len(self.data)} data points: {self.data}"
        return str




if __name__ == "__main__":
    # If we're running this script (instead of using it in another class or script), 
    # Run some code to try our class

    # First, setup logging
    logger, logname = setup_logger(__file__)

    # Create an object by calling the constructor 
    # The constructor method is always the name of the class
    # pass in the information required by the __init__ method defined in the class

    name1 = "Week 1 Journal"
    units1 = "calories"
    data1 = [120, 250, 200, 300]
    meal1 = "Breakfast"

    object1 = NumericFoodSeries(name1, units1, data1, meal1)

  
    name2 = "Week 1 Journal"
    units2 = "calories"
    data2 = [350, 450, 180, 500, 650, 390, 230]
    meal2 = "Lunch"

    object2 = NumericFoodSeries(name2, units2, data2, meal2)

    
    # Create another object 

   
    name3 = "Week 1 Journal"
    units3 = "calories"
    data3 = [600, 890, 1200, 800, 1000, 1230]
    meal3 = "Dinner"

    object3 = NumericFoodSeries(name3, units3, data3, meal3)

    # log the objects created
    logger.info(f"Created: {object1}")
    logger.info(f"Created: {object2}")
    logger.info(f"Created: {object3}")

    object_list = [object1, object2, object3]

    # Loop through our objects and get some statistics
    # Rather than using a built-in function and passing in our data
    # we call methods directly on our objects
    # Why? It's just another way to organize and reuse code. 
    # We encapusulate (wrap up) the attributes and associated methods into a resuable class. 
    # Write the class once, and use it many times. 
    # We'll see this a lot when we use dataframes to hold tables of data. 
    # Many popular libraries provide reusuable classes. 
    # It's a powerful way to organize code when dealing with many objects of the same type.

    for object in object_list:
        logger.info(object)
        logger.info(f"Count: {object.count()}")
        logger.info(f"Sum: {object.sum()}")
        logger.info(f"Mean: {object.mean()}")
        logger.info(f"Median: {object.median()}")
        logger.info("------------------")

    # Read log file and print it to the terminal
    with open(logname, 'r') as file_wrapper:
      print(file_wrapper.read())