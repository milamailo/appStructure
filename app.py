from src.FileToList import strToDictList
from src.IOOpration import readFromTxt
from src.ListPrinter import dictPrint

def main():
    empStrList = readFromTxt("./data/employee_data.txt")
    empDictList = strToDictList(empStrList)
    dictPrint(empDictList)


if __name__ == "__main__":
    main()