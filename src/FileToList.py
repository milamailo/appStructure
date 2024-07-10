import re

def strToDictList(strList):
    """
    Converts a list of strings into a list of dictionaries. Each string represents employee data
    and is split into individual fields based on delimiters (comma, dash, pipe, or whitespace).
    The resulting dictionaries use a predefined set of headers as keys.

    :param strList: List of strings, each representing an employee's data.
    :return: List of dictionaries, each containing the employee's data.
    """
    # Define the header for the employee dictionary
    header = ["id", "first_name", "last_name", "position", "department", "salary"]
    empList = []

    # Iterate over each string in the list
    for row in strList:
        # Split the string into individual fields based on the delimiters
        empInfo = re.split(r'[,\-|\s]+', row)
        # Create a dictionary by zipping the header with the employee info
        empDict = dict(zip(header, empInfo))
        # Append the dictionary to the employee list
        empList.append(empDict)

    return empList