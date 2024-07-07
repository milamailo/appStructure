def readFromTxt(filePath):
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

