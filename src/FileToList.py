import re

def strToDictList(strList):
    newStrList = list(strList)
    header = ["id","first_name","Last_name","position","department","salary"]
    empList = []

    for row in newStrList:
        empInfo = re.split(r'[,\-|\s]+', row)
        empDict = dict(zip(header,empInfo))
        empList.append(empDict)

    return empList
