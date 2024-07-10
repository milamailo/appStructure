import re
def search(source, text_to_search):
    """
    Searches for the first occurrence of text_to_search in the source and cleans up HTML tags.

    :param source: The source string to be searched.
    :param text_to_search: The text to search for.
    :return: The cleaned text of the first line containing text_to_search.
    """
    result = None
    sourceToList = split_by_newline(source)
    for element in sourceToList:
        if text_to_search in element:
            result = element
            break
    return cleanUp(result)

def split_by_newline(input_string):
    """
    Splits the input string by new lines and returns a list of non-empty, trimmed strings.

    :param input_string: The input string to be split.
    :return: A list of non-empty, trimmed strings split by new lines.
    """
    lines = input_string.split('\n')

    # Filter out empty strings and trim each line
    non_empty_trimmed_lines = [line.strip() for line in lines if line.strip() != '']

    return non_empty_trimmed_lines

def cleanUp(text):
    """
    Removes HTML tags from the given text.

    :param text: The input text with HTML tags.
    :return: The cleaned text without HTML tags.
    """
    if text is None:
        return None
    # Remove HTML tags using regular expression
    clean_text = re.sub(r'<.*?>', '', text)
    return clean_text