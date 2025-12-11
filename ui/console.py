def show_feedback(message: str) -> None:
    '''Prints a formatted feedback message to the console.'''
    symbol: str = "*"*30
    print(f"""
{symbol}
{message}
{symbol}
""")
    
def show_question(question: str) -> None: 
    '''Prints the question and options to the console.'''
    print(question)

def collect_user_answer() -> str:
    '''Prompts the user and captures their raw input/choice.''' 
    return input("Enter your choice: ")

def print_question_indicator(current_question_value: int, total_questions_value: int) -> None:
    '''Displays the current question number relative to the total number of questions.'''
    print("------------------------------")
    print(f"Question {current_question_value} of {total_questions_value}")
    print("------------------------------")

def validate_choice(choice: str) -> bool:
    '''Checks if the user's input is a valid option (A, B, C, or D).'''
    choice_tmp = choice.upper().strip()
    if choice_tmp in ("A", "B", "C", "D"): #== "A" or choice.tmp == "B" or choice.tmp == "C" or choice.tmp == "D":
        return True
    else: 
        return False
    
def get_updated_counter(counter: int, user_input: str) -> int:
    '''Increments or decrements the question counter based on user input (Next/Previous).'''
    if user_input.upper().strip() == "P":
        if counter > 0:
            return counter -1
        else:
            return counter
    else:
        return counter +1

    
def get_current_question_number(value: int) -> int:
    '''Converts the current zero-based index to a one-based number for display.'''
    return value + 1