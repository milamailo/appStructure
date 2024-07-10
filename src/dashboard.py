import textwrap

from src.FileToList import strToDictList
from src.IOOpration import readFromTxt
from src.ListPrinter import dictPrint
from src.UserInputOpration import askQuestions
from src.onlineRawData import onlineRequest
from src.searchPage import search

def menu():
    """
    Displays a menu with options for file operations, HTML source search, and an exit option.
    The user can select an option to perform the corresponding operation.
    """
    while True:
        # Display menu options
        print("Menu:")
        print("1. File Operation")
        print("2. HTML Source Search")
        print("3. Option 3")
        print("4. Exit")

        # Get user choice
        choice = input("Please select an option (1-4): ")

        # Match the user choice with corresponding actions
        match choice:
            case "1":
                print("You selected File Operation")
                # Read employee data from a file
                empStrList = readFromTxt("./data/employee_data.txt")
                # Convert the data to a list of dictionaries
                empDictList = strToDictList(empStrList)
                # Print the employee data as a formatted table
                dictPrint(empDictList)
                print("Press any key to go back to Dashboard")
                input()
            case "2":
                # Ask user for URL and text to search
                questions = [
                    "Please type the url of the web page: ",
                    "Please type the text to lookup: "
                ]
                QA = askQuestions(questions)
                print("Raw Data 'HTML Search'")
                # Get URL and search text from the user's answers
                url = QA.get("Please type the url of the web page: ")
                text_to_search = QA.get("Please type the text to lookup: ")
                # Fetch HTML content from the given URL
                htmlText = onlineRequest(url)
                # Search for the specified text within the HTML content
                result = search(htmlText, text_to_search)
                # Wrap the result to a specified width (e.g., 80 characters)
                wrapped_result = textwrap.fill(result, width=80)
                # Print the search result
                print("Founded Sentence/Paragraph:")
                print(wrapped_result)
                print("Press any key to go back to Dashboard")
                input()
            case "3":
                print("You selected Option 3")
                print("Press any key to go back to Dashboard")
                input()
            case "4":
                # Exit the menu
                print("Exiting the App. Goodbye!")
                break
            case _:
                # Handle invalid options
                print("Invalid option, please try again.")