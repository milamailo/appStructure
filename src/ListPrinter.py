def dictPrint(dictList):
    """
    Prints a list of dictionaries in a formatted table with aligned columns.

    :param dictList: The list of dictionaries to be printed.
    """
    # Determine the maximum width for each column
    widths = {}
    for emp in dictList:
        for key, value in emp.items():
            widths[key] = max(widths.get(key, 0), len(str(value)))

    header = ' | '.join(str(key).ljust(widths[key]) for key in emp)
    print(header)
    print("-" * len(header))

    # Print each employee's details with aligned columns
    for emp in dictList:
        row = ' | '.join(str(emp[key]).ljust(widths[key]) for key in emp)
        print(row)