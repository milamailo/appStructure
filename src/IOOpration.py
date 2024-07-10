def readFromTxt(filePath):
    """
    Reads lines from a text file and returns them as a list of strings.

    :param filePath: The path to the text file to be read.
    :return: A list of strings, each representing a line from the file.
    """
    mode = "r"
    strList = []
    try:
        with open(filePath, mode) as file:
            strList = file.readlines()
    except FileNotFoundError:
        print("The file was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

    return strList

