import inspect
import logging

logger = logging.getLogger(__name__)


def some_function(argument_1: int,
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
