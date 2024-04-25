import inspect
import logging

logger = logging.getLogger(__name__)


class MyObject:
    """
    A general-purpose object class template.
    """
    count = 0  # Initialize a class attribute to track the count of objects.

    def __init__(self, name: str,
                 number: int,
                 logical_operator: bool,
                 other_object: object):
        """
        Initialize the MyObject with specified attributes.
        Parameters:
            name (str): The name of the object.
            number (int): A numeric identifier for the object.
            logical_operator (bool): A boolean value representing a logical property of the object.
            other_object (object): Another object related to this instance.
        """
        self.name = name
        self.number = number
        self.logical_operator = logical_operator
        self.other_object = other_object
        MyObject.count += 1  # Increment the class counter each time an object is created

    def __str__(self):
        """
        Return a string representation of the object with all its details.
        Returns:
            str: Formatted string containing all the object's attributes.
        """
        other_object_repr = str(self.other_object) if self.other_object else "None"
        return (f"New Template Object:\n"
                f"Object Name ID: {self.name}\n"
                f"Object Number: {self.number}\n"
                f"Object Logical Operator: {self.logical_operator}\n"
                f"Object Encapsulated Object: {other_object_repr}\n")

    @property
    def info_summary(self):
        """
        Return a summary description of the object.
        Returns:
            str: A formatted string summary of the object.
        """
        return f"{self.name} | Number: {self.number} | Logic: {self.logical_operator}"

    @classmethod
    def number_of_objects(cls):
        """
        A class method to track how many instances of MyObject have been created.
        Returns:
            str: Information about how many objects exist.
        """
        return f"There are {cls.count} objects."

    def update_number(self, new_number):
        """
        Update the number attribute of the object.
        Parameters:
            new_number (int): The new number to set.
        """
        self.number = new_number
        logger.info(f"Updated object number to {new_number} for {self.name}")

    @staticmethod
    def some_action(argument_1: int,
                    argument_2: float,
                    some_text_data: str) -> list:
        """
        Perform calculations based on the inputs and log the process.

        This function combines two numeric arguments by addition, appends the result along with
        the original arguments and additional text data to a list, which is then returned. Throughout
        the function's execution, actions are logged.

        Parameters:
            argument_1 (int): The first numeric argument.
            argument_2 (float): The second numeric argument, which is added to the first.
            some_text_data (str): Additional text data to be included in the resulting list.

        Returns:
            list: A list containing a tuple of the first argument, the result of the addition, and the text data.

        Raises:
            Exception: Captures and logs any exceptions that occur during the function's execution.
        """
        function_name = inspect.currentframe().f_code.co_name
        log_message = f"Running function -> {function_name}"
        logger.info(log_message)
        print(log_message)  # Used for development stage

        new_objects = []

        try:
            # Example
            new_calculations = argument_1 + argument_2
            new_objects.append((argument_1, new_calculations, some_text_data))

            log_message = f"Successfully Performed -> {new_objects}"
            logger.info(log_message)
            print(log_message)  # Used for development stage

        except Exception as e:
            log_message_error = f"Error occurred: {str(e)}"
            logger.error(log_message_error)
            print(log_message_error)  # Used for development stage

        return new_objects
