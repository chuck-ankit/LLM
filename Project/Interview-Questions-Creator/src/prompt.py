   # Define the prompt  template
prompt_template = """
    You are an expert in creating exam questions based on coding materials and documentation.
    Your goal is to prepare engaging and comprehensive questions for exams, covering each concept thoroughly.
    You will achieve this by asking questions about the text provided below:

    ---------
    {text}
    ---------

    Create a set of questions that will effectively prepare coders and programmers for their tests.
    Ensure that all important information is covered without omitting any key details.

    Questions:
    """

    # Define the refine template
refine_template = """
    You are an expert in creating exam questions based on coding materials and documentation.
    Your goal is to prepare engaging and comprehensive questions for exams, covering each concept thoroughly.
    You will achieve this by asking questions about the text provided below:

    ---------
    {text}
    ---------

    Create a set of questions that will effectively prepare coders and programmers for their tests.
    Ensure that all important information is covered without omitting any key details.

    Now, refine the questions to make them more challenging and thought-provoking. Consider including:

    - Multiple-choice questions
    - True/false statements
    - Short answer questions
    - Problem-solving scenarios
    - Code debugging tasks

    Refined Questions:
    """