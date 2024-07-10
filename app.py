from src.FileToList import strToDictList
from src.IOOpration import readFromTxt
from src.ListPrinter import dictPrint
from src.onlineRawData import onlineRequest

def main():
    # empStrList = readFromTxt("./data/employee_data.txt")
    # empDictList = strToDictList(empStrList)
    # dictPrint(empDictList)
    htmlText = onlineRequest("https://www.python.org/about/")
    print(htmlText)



if __name__ == "__main__":
    main()