def askQuestions(questions):
    """
    Asks a series of questions and stores the answers in a dictionary.

    :param questions: A list of questions to ask.
    :return: A dictionary with questions as keys and user answers as values.
    """
    answers = {}
    for question in questions:
        answers[question] = input(question)
    return answers
