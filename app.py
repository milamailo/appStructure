from src.FileToList import strToDictList
from src.IOOpration import readFromTxt
from src.ListPrinter import dictPrint
from src.onlineRawData import onlineRequest
from src.searchPage import search

def main():
    """
    Main function to demonstrate various operations:
    1. Reading employee data from a file.
    2. Converting the data to a list of dictionaries.
    3. Printing the dictionaries in a formatted table.
    4. Making an online request to fetch HTML content.
    5. Searching for a specific text within the HTML content.
    """
    # Uncomment the following lines to read and process employee data from a file
    # empStrList = readFromTxt("./data/employee_data.txt")
    # empDictList = strToDictList(empStrList)
    # dictPrint(empDictList)

    # Fetch HTML content from a URL
    htmlText = onlineRequest("https://www.python.org/about/")

    # Uncomment to print the fetched HTML content
    # print(htmlText)

    # Search for a specific text within the HTML content
    result = search(htmlText, "Python can be easy to pick up whether you're a first time")
    print(result)

if __name__ == "__main__":
    main()
