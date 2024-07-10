from src.FileToList import strToDictList
from src.IOOpration import readFromTxt
from src.ListPrinter import dictPrint
from src.dashboard import menu
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

    menu()

if __name__ == "__main__":
    main()
