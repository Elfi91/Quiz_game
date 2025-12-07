def show_feedback(message: str) -> None:
    '''
    Returns formatted feedback to the user.
    '''
    symbol: str = "*"*30
    print(f"""
{symbol}
{message}
{symbol}
""")
    
def show_question(question: str) -> None: 
    '''
    Displays the question and answer options.
    '''
    print(question)

def collect_user_answer() -> str:
    '''
    This function solely handles taking the user's input.
    ''' 
    return input("Enter your choice: ")

def print_question_indicator(current_question_value: int, total_questions_value: int) -> None:
    '''
    """Prints the current question number relative to the total number of questions."""
    '''
    print("------------------------------")
    print(f"Question {current_question_value} of {total_questions_value}")
    print("------------------------------")